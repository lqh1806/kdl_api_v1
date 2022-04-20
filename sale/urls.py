from django.urls import path, include
from sale.views import *

urlpatterns = [
    path('buudien/', buudien, name='buudien'),
    path('dulich/', dulich, name='dulich'),
    path('dulich/<int:sanpham_id>/', dulich_filter1, name='dulich_filter1'),
    path('dulich/<int:sanpham_id>/<int:year_id>/', dulich_filter2, name='dulich_filter2'),
    path('dulich/<int:sanpham_id>/<int:quarter_id>/', dulich_filter3, name='dulich_filter3'),
    path('dulich/<int:year_id>/', dulich_filter4, name='dulich_filter4'),
    path('dulich/<int:quarter_id>/', dulich_filter5, name='dulich_filter5'),
    path('buudien/<int:sanpham_id>/', buudien_filter1, name='buudien_filter1'),
    path('buudien/<int:sanpham_id>/<int:year_id>/', buudien_filter2, name='buudien_filter2'),
    path('buudien/<int:sanpham_id>/<int:quarter_id>/', buudien_filter3, name='buudien_filter3'),
    path('buudien/<int:year_id>/', buudien_filter4, name='buudien_filter4'),
    path('buudien/<int:quarter_id>/', buudien_filter5, name='buudien_filter5'),
    path('tp/dulich/<str:city_name>/', tp_dulich_filter, name='tp_dulich_filter'),
    path('tp/dulich/<str:city_name>/<int:sanpham_id>', tp_dulich_filter1, name='tp_dulich_filter1'),
    path('tp/dulich/<str:city_name>/<int:sanpham_id>/<int:year_id>', tp_dulich_filter2, name='tp_dulich_filter2'),
    path('tp/dulich/<str:city_name>/<int:sanpham_id>/<int:quarter_id>', tp_dulich_filter3, name='tp_dulich_filter3'),
    path('tp/dulich/<str:city_name>/<int:year_id>', tp_dulich_filter4, name='tp_dulich_filter4'),
    path('tp/dulich/<str:city_name>/<int:quarter_id>', tp_dulich_filter5, name='tp_dulich_filter5'),

    path('tp/buudien/<str:city_name>/', tp_buudien_filter, name='tp_buudien_filter'),
    path('tp/buudien/<str:city_name>/<int:sanpham_id>', tp_buudien_filter1, name='tp_buudien_filter1'),
    path('tp/buudien/<str:city_name>/<int:sanpham_id>/<int:year_id>', tp_buudien_filter2, name='tp_buudien_filter2'),
    path('tp/buudien/<str:city_name>/<int:sanpham_id>/<int:quarter_id>', tp_buudien_filter3, name='tp_buudien_filter3'),
    path('tp/buudien/<str:city_name>/<int:year_id>', tp_buudien_filter4, name='tp_buudien_filter4'),
    path('tp/buudien/<str:city_name>/<int:quarter_id>', tp_buudien_filter5, name='tp_buudien_filter5'),
]