from . import views
from django.urls import path

urlpatterns = [
    path("user", views.user_POST, name="sign_up"),
    path("login", views.login_POST, name="sign_in"),
    path("mypage", views.mypage_GET, name="mypage_get"),
]
