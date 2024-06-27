from django.urls import path
from . import views

app_name = "accounts"

urlpatterns =  [
    path('login/', views.login_user, name = 'login'),  # accounts/
    path('logout/', views.logout_user, name = 'logout'),  # accounts/
    path('register/', views.register_user, name = 'register'),  # accounts/
]