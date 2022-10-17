from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('sign-up/', views.signUp, name='sign-up'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-out/', views.signOut, name='sign-out'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
]
