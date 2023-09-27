from django.urls import path

from . import views

urlpatterns = [
    path('lists/', views.ProductListAPIView.as_view()),
    path('<int:id>/', views.ProductDetailAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
    path('update/<int:id>/', views.ProductUpdateAPIView.as_view()),
    path('delete/<int:id>/', views.ProductDeleteAPIView.as_view()),
]
