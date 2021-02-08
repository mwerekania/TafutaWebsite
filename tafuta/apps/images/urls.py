from django.urls import path
from . import views

app_name = 'tafuta.apps.images'
urlpatterns = [
    path('create/', views.image_create, name='create'),
]