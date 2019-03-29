from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),
    path('market/', views.products_page, name='market_page'),
    path('market/add-user-fertiliser/', views.add_user_fertiliser, name='add_user_fertiliser'),
]

