from django.urls import path, include

from . import views

app_name = 'StoreProducts'

urlpatterns = [
    path('', views.index, name='index')
]