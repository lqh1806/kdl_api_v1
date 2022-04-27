from re import M
from django.urls import path, include
from giaodien.views import *

urlpatterns = [
    path('giaodien/sale/', sale, name='giaodien_sale'),
    path('giaodien/sale/<int:id_sp>/<int:id_nam>/<int:id_quy>/' ,get_sale_filter, name='get_sale_filter'),
]