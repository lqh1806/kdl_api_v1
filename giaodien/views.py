from django.shortcuts import render
from sale.views import *
# Create your views here.

def sale(request):
    # print('Count')
    # list_buudien = buudien(request)
    # list_dulich = dulich(request)
    # list_all = get_list_all(request)
    # # print(list_buudien)
    # # print(list_dulich)
    # list2_dulich = []
    # list2_all = []
    
    # for item_dulich in list_dulich:
    #     check = 0
    #     for item_buudien in list_buudien:
    #         if(item_dulich['VANPHONGDAIDIEN_DIMENSION'] in item_buudien.values()):
    #             check = 1
    #     if check == 0:
    #         list2_dulich.append(item_dulich)  

    # for item in list_all:
    #     check = 0
    #     for item_buudien in list_buudien:
    #         if(item['VANPHONGDAIDIEN_DIMENSION'] in item_buudien.values()):
    #             check = 1
    #     if check == 0:
    #         list2_all.append(item) 
        
    # return render(request, 'table.html', {'list_buudien': list_buudien, 'list_dulich': list_dulich, 'list2_dulich': list2_dulich, 'list_all': list_all, 'list2_all': list2_all})
    return render(request, 'table.html')

def get_sale_filter(request, id_sp, id_nam, id_quy):
    if(id_sp != 0 and id_nam == 0 and id_quy == 0):
        list_dulich = dulich_filter1(request, id_sp)
        list_buudien = buudien_filter1(request, id_sp)
        list_all = filter1(request, id_sp)
    print(list_dulich)
    print(list_buudien)
    list2_dulich = []
    list2_buudien = []
    list2_all = []
    
    for item_dulich in list_dulich:
        check = 0
        for item_buudien in list_buudien:
            if(item_dulich['VANPHONGDAIDIEN_DIMENSION'] in item_buudien.values()):
                check = 1
        if check == 0:
            list2_dulich.append(item_dulich)  

    for item_buudien in list_buudien:
        check = 0
        for item_dulich in list_dulich:
            if(item_buudien['VANPHONGDAIDIEN_DIMENSION'] in item_dulich.values()):
                check = 1
        if check == 0:
            list_dulich.append({'VANPHONGDAIDIEN_DIMENSION': item_buudien['VANPHONGDAIDIEN_DIMENSION'], 'TONGTIEN': 0, 'SOLUONG': 0})

    for item in list_all:
        check = 0
        for item_buudien in list_buudien:
            if(item['VANPHONGDAIDIEN_DIMENSION'] in item_buudien.values()):
                check = 1
        if check == 0:
            list2_all.append(item) 
        
    return render(request, 'table.html', {'list_buudien': list_buudien, 'list_dulich': list_dulich, 'list2_dulich': list2_dulich, 'list_all': list_all, 'list2_all': list2_all})