from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse

# Create your views here.

def buudien(request):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as 
        soluong from 
        (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
        from ban_cube_view bcv 
        where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension in (select year from thoigian_dimension_view) and bcv.khachhang_dimension = 'BuuDien') x 
        group by x.vanphongdaidien_dimension
        order by x.vanphongdaidien_dimension""")
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False) 
    
def dulich(request):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong 
        from (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong 
        from ban_cube_view bcv where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension in (select year from thoigian_dimension_view) 
        and bcv.khachhang_dimension = 'DuLich') x 
        group by x.vanphongdaidien_dimension
        order by x.vanphongdaidien_dimension""")
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)   

def get_list_all(request):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as 
        soluong from 
        (select bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
        from ban_cube_view bcv 
        where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension in (select year from thoigian_dimension_view) and(bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')) x 
        group by x.vanphongdaidien_dimension, x.khachhang_dimension
        order by x.vanphongdaidien_dimension""")
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)     

#lấy sản phẩm theo id, không tính quý và năm của cả 2 loại khách hàng
def filter1(request, sanpham_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) 
        as soluong from (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong, bcv.khachhang_dimension     
        from ban_cube_view bcv where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension in (select year from thoigian_dimension_view)  and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
        and bcv.mathang_dimension = %s) x 
        group by x.vanphongdaidien_dimension,x.khachhang_dimension
        order by x.vanphongdaidien_dimension""", [sanpham_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)      

def filter2(request, sanpham_id, nam_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) 
        as soluong from (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong, bcv.khachhang_dimension     
        from ban_cube_view bcv where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension = %s  and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
        and bcv.mathang_dimension = %s) x 
        group by x.vanphongdaidien_dimension,x.khachhang_dimension
        order by x.vanphongdaidien_dimension""", [nam_id, sanpham_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False) 

def filter3(request, sanpham_id, quy_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) 
        as soluong from (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong, bcv.khachhang_dimension     
        from ban_cube_view bcv where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension = %s  and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
        and bcv.mathang_dimension = %s) x 
        group by x.vanphongdaidien_dimension,x.khachhang_dimension
        order by x.vanphongdaidien_dimension""", [quy_id, sanpham_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False) 

def filter4(request, nam_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) 
        as soluong from (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong, bcv.khachhang_dimension     
        from ban_cube_view bcv where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension = %s  and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
        ) x 
        group by x.vanphongdaidien_dimension,x.khachhang_dimension
        order by x.vanphongdaidien_dimension""", [nam_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False) 

def filter5(request, quy_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) 
        as soluong from (select bcv.vanphongdaidien_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong, bcv.khachhang_dimension     
        from ban_cube_view bcv where bcv.vanphongdaidien_dimension in 
        (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.level_name = 'BANG') 
        and bcv.thoigian_dimension = %s  and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
        ) x 
        group by x.vanphongdaidien_dimension,x.khachhang_dimension
        order by x.vanphongdaidien_dimension""", [quy_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False) 

def filter6(request, city_name):
    with connection.cursor() as cursor:
        cursor.execute("""select x.long_description,  x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong
from (select vpdd2.long_description, bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
from ban_cube_view bcv, vanphongdaidien_dimension_view vpdd2
where bcv.vanphongdaidien_dimension in (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.ten_bang_1 = %s)
and bcv.thoigian_dimension in (select year from thoigian_dimension_view) 
and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
and vpdd2.dim_key = bcv.vanphongdaidien_dimension) x
group by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension
order by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension""", [city_name])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False) 

def filter7(request, city_name, sanpham_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.long_description,  x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong
from (select vpdd2.long_description, bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
from ban_cube_view bcv, vanphongdaidien_dimension_view vpdd2
where bcv.vanphongdaidien_dimension in (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.ten_bang_1 = %s)
and bcv.thoigian_dimension in (select year from thoigian_dimension_view) 
and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
and bcv.mathang_dimension = %s
and vpdd2.dim_key = bcv.vanphongdaidien_dimension) x
group by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension
order by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension""", [city_name, sanpham_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)    

def filter8(request, city_name, sanpham_id, year_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.long_description,  x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong
from (select vpdd2.long_description, bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
from ban_cube_view bcv, vanphongdaidien_dimension_view vpdd2
where bcv.vanphongdaidien_dimension in (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.ten_bang_1 = %s)
and bcv.thoigian_dimension = %s
and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
and bcv.mathang_dimension = %s
and vpdd2.dim_key = bcv.vanphongdaidien_dimension) x
group by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension
order by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension""", [city_name, year_id, sanpham_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)     

def filter9(request, city_name, sanpham_id, quarter_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.long_description,  x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong
from (select vpdd2.long_description, bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
from ban_cube_view bcv, vanphongdaidien_dimension_view vpdd2
where bcv.vanphongdaidien_dimension in (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.ten_bang_1 = %s)
and bcv.thoigian_dimension = %s
and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
and bcv.mathang_dimension = %s
and vpdd2.dim_key = bcv.vanphongdaidien_dimension) x
group by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension
order by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension""", [city_name, quarter_id, sanpham_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)      

def filter10(request, city_name, year_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.long_description,  x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong
from (select vpdd2.long_description, bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
from ban_cube_view bcv, vanphongdaidien_dimension_view vpdd2
where bcv.vanphongdaidien_dimension in (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.ten_bang_1 = %s)
and bcv.thoigian_dimension = %s
and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
and vpdd2.dim_key = bcv.vanphongdaidien_dimension) x
group by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension
order by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension""", [city_name, year_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)     

def filter11(request, city_name, quarter_id):
    with connection.cursor() as cursor:
        cursor.execute("""select x.long_description,  x.vanphongdaidien_dimension, x.khachhang_dimension, sum(x.tongtien) as tongtien, sum(x.soluong) as soluong
from (select vpdd2.long_description, bcv.vanphongdaidien_dimension, bcv.khachhang_dimension, bcv.thoigian_dimension, bcv.tongtien, bcv.soluong
from ban_cube_view bcv, vanphongdaidien_dimension_view vpdd2
where bcv.vanphongdaidien_dimension in (select dim_key from vanphongdaidien_dimension_view vpdd where vpdd.ten_bang_1 = %s)
and bcv.thoigian_dimension = %s
and (bcv.khachhang_dimension = 'DuLich' or bcv.khachhang_dimension = 'BuuDien')
and vpdd2.dim_key = bcv.vanphongdaidien_dimension) x
group by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension
order by x.vanphongdaidien_dimension, x.long_description, x.khachhang_dimension""", [city_name, quarter_id])
        res = dictfetchall(cursor)

    return JsonResponse(res, safe=False)          

    
def get_sp(request):
    with connection.cursor() as cursor:
        cursor.execute("""select dim_key, mieuta
from mathang_dimension_view""")
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