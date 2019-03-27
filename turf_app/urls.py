from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),
    path('products/', views.products_page, name='products_page'),
    path('products/', views.add_user_fertiliser, name='add_user_fertiliser'),
]

