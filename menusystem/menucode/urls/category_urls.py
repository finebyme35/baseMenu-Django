from django.urls import path
from menucode.views import category_views as views

urlpatterns = [
    path('', views.getCategorys, name="categorys"),
    path('create/', views.createCategorys, name="category-create"),
    path('<str:pk>/', views.getCategory, name="category"),
    path('update/<str:pk>/', views.updateCategorys, name="category-update"),
    path('delete/<str:pk>/', views.deleteCategory, name="category-delete"),
]