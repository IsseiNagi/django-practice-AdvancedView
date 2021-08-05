from django.contrib import admin
from django.urls import path, include
from store import views  # アプリフォルダstoreにあるviewsをimoortしている

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('user/', include('user.urls')),
]

# handlerにviews.pyの関数を代入
handler404 = views.page_not_found
handler500 = views.server_error
