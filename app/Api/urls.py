from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("<slug:slug>", views.apiController, name="api-controller"),
]
