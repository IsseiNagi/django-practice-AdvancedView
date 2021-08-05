from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import UserForm, ProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.


def user_list(request):
    return render(request, 'user/user_list.html')


def index(request):
    return render(request, 'user/index.html')


def register(request):
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)

    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)  # バリデーションのためにDBに登録せずインスタンスを取り出す
        try:
            # バリデーションを実行
            validate_password(user_form.cleaned_data.get('password'), user)
        # 実行してエラーが出た場合の処理
        except ValidationError as e:
            # add_error：<フィールド名><エラー> フィールドにエラーを追加して返す
            user_form.add_error('password', e)
            return render(request, 'user/registration.html', context={
                'user_form': user_form,
                'profile_form': profile_form
            })
        user.set_password(user.password)  # パスワードが暗号化されて保存される
        user.save()
        profile = profile_form.save(commit=False)
        # commit=False DB上には保存しないで、モデルインスタンスを返す
        profile.user = user  # onetooneフィールドで紐づいているuserフォームにuserを入れる
        profile.save()
    return render(request, 'user/registration.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
    })


def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        # authenticateでユーザー名とパスワードが正しいか確認する
        user = authenticate(username=username, password=password)  # 正しければユーザーインスタンスを返す
        if user:
            # ユーザーが有効な場合
            if user.is_active:
                login(request, user)  # 第２引数にユーザーを指定してログインする
                return redirect('user:index')
            else:
                return HttpResponse('アカウントが有効ではありません')
        else:
            return HttpResponse('ユーザーが存在しません')
    return render(request, 'user/login.html', context={
        'login_form': login_form
    })


@login_required  # ログインしている時だけ実行させるデコレーター
def user_logout(request):
    logout(request)  # ログアウトはlogoutを使うだけ
    return redirect('user:index')


@login_required
def info(request):
    return HttpResponse('ログインしています')
