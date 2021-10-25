from django.urls import path
from .views import register,user_logout,user_login,user_profile


urlpatterns = [
    path("register/",register,name="register"),
    path("logout/",user_logout,name="logout"),
    path("login/",user_login,name="login"),
    path("update/<int:id>/",user_profile,name="profile"),
  
] 