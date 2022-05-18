
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
and ltcv.thoigian_dimension in (select year from thoigian_dimension_view) 
group by ltcv.cuahang_dimension
order by ltcv.cuahang_dimension""")
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)

def get_cua_hang(request, cuahang):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.thoigian_dimension in (select year from thoigian_dimension_view) 
group by ltcv.cuahang_dimension""", [cuahang])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)    

def filter1(request, sanpham_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension, sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
and ltcv.mathang_dimension = %s
and ltcv.thoigian_dimension in (select year from thoigian_dimension_view) 
group by ltcv.cuahang_dimension
order by ltcv.cuahang_dimension """ , [sanpham_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)

def filter2(request, sanpham_id, nam_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension, sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
and ltcv.mathang_dimension = %s
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension
order by ltcv.cuahang_dimension """ , [sanpham_id, nam_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)    

def filter3(request, sanpham_id, quy_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension, sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
and ltcv.mathang_dimension = %s
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension
order by ltcv.cuahang_dimension """ , [sanpham_id, quy_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)     

def filter4(request, nam_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension, sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension
order by ltcv.cuahang_dimension """ , [nam_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)   

def filter5(request, quy_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension, sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv
where ltcv.cuahang_dimension in(select dim_key from cuahang_dimension_view chv where chv.level_name = 'TONG_CUAHANG')
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension
order by ltcv.cuahang_dimension """ , [quy_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)     

def filter6(request, cuahang, sanpham_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.mathang_dimension = %s
and ltcv.thoigian_dimension in (select year from thoigian_dimension_view) 
group by ltcv.cuahang_dimension """ , [cuahang, sanpham_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)    

def filter7(request, cuahang, sanpham_id, nam_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.mathang_dimension = %s
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension """ , [cuahang, sanpham_id, nam_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)     

def filter8(request, cuahang, sanpham_id, quy_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.mathang_dimension = %s
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension """ , [cuahang, sanpham_id, quy_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)      

def filter9(request, cuahang, nam_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension """ , [cuahang, nam_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)     

def filter10(request, cuahang, quy_id):
    with connection.cursor() as cursor:
        cursor.execute("""select ltcv.cuahang_dimension ,sum(ltcv.soluong) as soluong
from luutru_cube_view ltcv, cuahang_dimension_view chv
where ltcv.cuahang_dimension = chv.dim_key and chv.level_name = 'CUAHANG' and chv.TENTP = %s
and ltcv.thoigian_dimension = %s
group by ltcv.cuahang_dimension """ , [cuahang, quy_id]) 
        res = dictfetchall(cursor)
    return JsonResponse(res, safe=False)       
    
def get_nam(request):
    with connection.cursor() as cursor:
        cursor.execute("""select dim_key, long_description
from thoigian_dimension_view
where level_name = 'NAM'""")
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)  

def get_quy(request, nam):
    with connection.cursor() as cursor:
        cursor.execute("""select dim_key, long_description
from thoigian_dimension_view
where year = %s""", [nam])
        res = dictfetchall(cursor)
    
    return JsonResponse(res, safe=False)  

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]    