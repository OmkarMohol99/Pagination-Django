from django.urls import path
from . import views

urlpatterns = [
    path('su/', views.signupView, name='signup_url'),
    path('li/', views.signinView, name='signin_url'),
    path('lo/', views.logoutView, name='logout_url')
]