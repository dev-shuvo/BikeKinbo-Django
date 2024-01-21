from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("services/", services, name="services"),
    path("about/", about, name="about"),
]