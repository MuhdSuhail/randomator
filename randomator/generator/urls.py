from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.signup_user, name='signup'),
    path('change_password/', views.change_password, name='change_password'),
    path('generate_password/', views.generate_password, name="generate_password"),
    path('password/', views.password, name="password"),
    path('save_password/', views.save_password, name="save_password"),
    path('saved_items/', views.saved_items, name="saved_items")
]
