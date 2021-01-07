from django.urls import path

from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='products-list-create'),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
    }), name='products-detail'),
    path('user', UserAPIView.as_view()),
]