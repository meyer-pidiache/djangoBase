"""djagoBase URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.cover),
    path("", include("apps.user.urls")),
    path("", include("apps.main.urls")),
]
