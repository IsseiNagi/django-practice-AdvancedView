from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Items
from django.http import Http404


# Create your views here.


def item_list(request):
    items = Items.objects.all()
    items = get_list_or_404(Items, pk__gt=2)  # pkが2より大きいものの指定。なければ404になる
    return render(request, 'store/item_list.html', context={
        'items': items
    })


# サーバーエラーテスト用
# def item_list(request):
#     items = Items.objects.all()
#     return render(request, 'store/itemlist.html', context={
#         'items': items
#     })


def item_detail(request, id):
    if id == 0:
        raise Http404
    # item = Items.objects.filter(pk=id).first()
    item = get_object_or_404(Items, pk=id)  # g~_or_404のテスト用 存在しないidだと404が出る

    # idでitemを取得できなかったらリストにリダイレクトさせる
    if item is None:
        return redirect('store:item_list')
    return render(request, 'store/item_detail.html', context={
        'item': item
    })


def to_google(request):
    return redirect('https://www.google.com')


# templateをrenderするのではなく、app_name=storeのurlname=item_detailにリダイレクトさせる
def one_item(request):
    # id=1を引数で渡してitem_detail関数の実行
    return redirect('store:item_detail', id=1)


def page_not_found(request, exception):
    return render(request, 'store/404.html', status=404)  # 404をステータスにとらないと、アクセスログに200と表示されてしまう
    # return redirect('store:item_list')  # 強制的にリストページにリダイレクトさせる


def server_error(request):
    return render(request, 'store/500.html', status=500)
