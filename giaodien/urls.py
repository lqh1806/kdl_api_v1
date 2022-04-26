from re import M
from django.urls import path, include
from giaodien.views import *

urlpatterns = [
    path('', index, name='index'),
]