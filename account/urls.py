from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),#create a path to index page (index is function which is mentioned in the views)
]