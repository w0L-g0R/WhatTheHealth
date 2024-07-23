from django.contrib import admin
from django.urls import path, re_path
from src.what_the_health import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("login", views.login),
    re_path("signup", views.signup),
    re_path("validate-token", views.validate_token),
]
