from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.note_create, name='note_create'),
    path('notes/edit/<int:pk>/', views.note_edit, name='note_edit'),
    path('notes/delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Routes d'authentification
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
