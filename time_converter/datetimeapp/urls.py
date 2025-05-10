from django.urls import path
from .views import index, get_time

urlpatterns = [
    path('', index, name='index'),
    path('get_time/', get_time, name='get_time'),
]