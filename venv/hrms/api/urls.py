from django.urls import path

from . import views

urlpatterns = [
    path("getapi/", views.get_api, name="api")
]