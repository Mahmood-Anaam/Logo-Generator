from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path('text2logogenerate/', views.Text2LogoGenerate,name="text2logogenerate"),
    path("", views.home),
]