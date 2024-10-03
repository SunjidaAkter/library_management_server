from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.BorrowViewSet, basename='borrow')

urlpatterns = [
    path('', include(router.urls)),
    # Custom route for borrowing a book (with `pk` in the URL)
    path('borrow/<int:pk>/', views.BorrowViewSet.as_view({'post': 'create'}), name='borrow-book'),
]