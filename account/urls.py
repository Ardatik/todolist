from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.LoginUser, name='login'),
    path('registration/', views.RegistrationUser, name='registration'),
    path('logout/', views.LogoutUser, name='logout')
]
