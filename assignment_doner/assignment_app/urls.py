from django.urls import path
from .import views

urlpatterns = [
     path("", views.index, name="index"),
     path("otp", views.otp, name="otp"),
     path("about", views.about, name="about"),
     path("form", views.form, name="form"),
     path("index", views.index, name="index")
    
]