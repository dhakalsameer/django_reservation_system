from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.create_reservation, name='create'),
    path('edit/<int:pk>/', views.update_reservation, name='update'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete'),

    # 🔑 Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
