from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),#create a path to index page (index is function which is mentioned in the views)
]