from re import M
from django.urls import path, include
from store.views import *

urlpatterns = [
    path('get_nam/', get_nam, name='get_nam'),
    path('get_quy/<int:nam>/', get_quy, name='get_quy'),
    path('all/', get_thanh_pho, name='get_thanh_pho'),
    path('all/<int:sanpham_id>/', filter1, name='filter1'),
    path('all/<int:sanpham_id>/nam/<int:nam_id>/', filter2, name='filter2'),
    path('all/<int:sanpham_id>/quy/<int:quy_id>/', filter3, name='filter3'),
    path('all/nam/<int:nam_id>/', filter4, name='filter4'),
    path('all/quy/<int:quy_id>/', filter5, name='filter5'),
    path('all/tp/<str:cuahang>/', get_cua_hang, name='get_cua_hang'),
    path('all/tp/<str:cuahang>/<int:sanpham_id>/', filter6, name='filter6'),
    path('all/tp/<str:cuahang>/<int:sanpham_id>/nam/<int:nam_id>/', filter7, name='filter7'),
    path('all/tp/<str:cuahang>/<int:sanpham_id>/quy/<int:quy_id>/', filter8, name='filter8'),
    path('all/tp/<str:cuahang>/nam/<int:nam_id>/', filter9, name='filter9'),
    path('all/tp/<str:cuahang>/quy/<int:quy_id>/', filter10, name='filter10'),
]