from re import M
from django.urls import path, include
from store.views import *

urlpatterns = [
    path('thanhpho/', get_thanh_pho, name='get_thanh_pho'),
    path('thanhpho/<str:cuahang>/', get_cua_hang, name='get_cua_hang'),
    path('thanhpho/sanpham/<int:sanpham_id>/', thanhpho_id, name='thanhpho_id'),
    path('thanhpho/<str:cuahang>/<int:sanpham_id>/', cuahang_id, name='cuahang_id'),
]