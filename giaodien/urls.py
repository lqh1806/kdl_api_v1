from re import M
from django.urls import path, include
from giaodien.views import *

urlpatterns = [
    path('giaodien/sale/', sale, name='sale'),
    path('giaodien/store/', store, name='store'),
]