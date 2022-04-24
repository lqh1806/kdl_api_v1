
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse

# Create your views here.

# lấy ra tổng sản phẩm bán được của từng thành phố
def get_thanh_pho(request):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
group by ltcv.cuahang_dimension""")
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)

def get_cua_hang(request, cuahang):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
group by ltcv.cuahang_dimension""", [cuahang])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)    

def thanhpho_id(request, sanpham_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension, ltcv.soluong 
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
and ltcv.mathang_dimension = %s """ , [sanpham_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)

def cuahang_id(request, cuahang, sanpham_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.mathang_dimension = %s
group by ltcv.cuahang_dimension """ , [cuahang, sanpham_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)    

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]    