
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . views import UserViewSet
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user_account/', include('user_account.urls')),
    path('genre/', include('genre.urls')),
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path('borrow/', include('borrow.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('transaction/', include('transaction.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
