from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('account/login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    path('account/logout/',
        auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
        name='logout'),

    path('account/signup', views.sign_up, name="signup"),
]
