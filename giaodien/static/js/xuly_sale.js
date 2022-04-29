$(document).ready(function () {
  console.log('Hello')
  sp_combo_box = $('#sp-combo-box');
  nam_combo_box = $('#nam-combo-box');
  quy_combo_box = $('#quy-combo-box');

  $.ajax({
    method: 'GET',
    url: 'http://127.0.0.1:8000/sale/get_sp/',
  }).done(function (data) {
    for (i in data) {
      sp_combo_box.append(
        "<option value = '" +
          data[i].DIM_KEY +
          "'>" +
          data[i].MIEUTA +
          '</option>'
      );
    }
  });

  $.ajax({
    method: 'GET',
    url: 'http://127.0.0.1:8000/sale/get_nam/',
  }).done(function (data) {
    for (i in data) {
      nam_combo_box.append(
        "<option value = '" +
          data[i].DIM_KEY +
          "'>" +
          data[i].LONG_DESCRIPTION +
          '</option>'
      );
    }
  });

  $('#nam-combo-box').change(function () {
    $(this)
      .find(':selected')
      .each(function () {
        nam_to_bind = $(this).val();
        if (nam_to_bind != 0) {
          quy_combo_box.find('option').remove();
          quy_combo_box.append(
            "<option value = '0'>" + 'Tất cả các quý' + '</option>'
          );
          quy_combo_box.removeAttr('disabled');
          $.ajax({
            method: 'GET',
            url: 'http://127.0.0.1:8000/sale/get_quy/' + nam_to_bind,
          }).done(function (data) {
            for (i in data) {
              quy_combo_box.append(
                "<option value = '" +
                  data[i].DIM_KEY +
                  "'>" +
                  data[i].LONG_DESCRIPTION +
                  '</option>'
              );
            }
          });
        } else {
          quy_combo_box.find('option').remove();
          quy_combo_box.append(
            "<option value = '0'>" + 'Tất cả các quý' + '</option>'
          );
          quy_combo_box.attr('disabled', 'disabled');
        }
      });
  });
  getData('http://127.0.0.1:8000/sale/all/');

  $('button').click(function(){
    id_sp = $('#sp-combo-box').val();
    id_nam = $('#nam-combo-box').val();
    id_quy = 0;
    id_quy = $('#quy-combo-box').val();
    if(id_sp == 0 && id_nam == 0){
      getData('http://127.0.0.1:8000/sale/all/');
    }
    if(id_sp == 0 && id_nam != 0 && id_quy == 0){
      var url = 'http://127.0.0.1:8000/sale/all/nam/' + id_nam + '/'; 
      getData(url);
    }
    if(id_sp == 0 && id_nam != 0 && id_quy != 0){
      var url = 'http://127.0.0.1:8000/sale/all/quy/' + id_quy + '/'; 
      getData(url);
    }
    if(id_sp != 0 && id_nam == 0){
      var url = 'http://127.0.0.1:8000/sale/all/' + id_sp + '/'; 
      getData(url);
    }
    if(id_sp != 0 && id_nam != 0 && id_quy == 0){
      var url = 'http://127.0.0.1:8000/sale/all/' + id_sp + '/nam/' + id_nam + '/';;
      getData(url);
    }
    if(id_sp != 0 && id_nam != 0 && id_quy != 0){
      var url = 'http://127.0.0.1:8000/sale/all/' + id_sp + '/quy/' + id_quy + '/';; 
      getData(url);
    }
  });


  $("#table-sale").on('click', 'tbody tr', function(){
    $(this).toggleClass("show")
    if($(this).hasClass('show')){

      id_sp = $('#sp-combo-box').val();
      id_nam = $('#nam-combo-box').val();
      id_quy = 0;
      id_quy = $('#quy-combo-box').val();
      var id_tr = encodeURIComponent($(this).attr('id'))
      if(id_sp == 0 && id_nam == 0){
        getDetailData('http://127.0.0.1:8000/sale/all/bang/' + id_tr + '/', $(this).attr('class'))
      }
      if(id_sp == 0 && id_nam != 0 && id_quy == 0){
        getDetailData('http://127.0.0.1:8000/sale/all/bang/' + id_tr + '/nam/' + id_nam + '/', $(this).attr('class'))
      }
      if(id_sp == 0 && id_nam != 0 && id_quy != 0){
        getDetailData('http://127.0.0.1:8000/sale/all/bang/' + id_tr + '/quy/' + id_quy + '/', $(this).attr('class'))
      }
      if(id_sp != 0 && id_nam == 0){
        getDetailData('http://127.0.0.1:8000/sale/all/bang/' + id_tr + '/' + id_sp + '/', $(this).attr('class'))
      }
      if(id_sp != 0 && id_nam != 0 && id_quy == 0){
        getDetailData('http://127.0.0.1:8000/sale/all/bang/' + id_tr + '/' + id_sp + '/nam/' + id_nam + '/', $(this).attr('class'))
      }
      if(id_sp != 0 && id_nam != 0 && id_quy != 0){
        getDetailData('http://127.0.0.1:8000/sale/all/bang/' + id_tr + '/' + id_sp + '/quy/' + id_quy + '/', $(this).attr('class'))
      }
    }
    else{
      $("#table-sale tbody ").find("tr.children").remove();
    }
  });
});

function getData(url){
  $('table tbody').find('tr').remove();
  $('table tbody').append("<tr>" +
  "<td colspan='2'></td>" +
  "<td>Số lượng</td>" +
  "<td class='pr-5'>Tổng tiền</td>" + 
  "<td>Số lượng</td>" + 
  "<td class='pr-5'>Tổng tiền</td>" + 
  "<td>Số lượng</td>" + 
  "<td class='pr-5'>Tổng tiền</td>" + 
"</tr>")
    $.ajax({
    method: 'GET',
    url: url,
  }).done(function (data) {
     for(let i = 0; i < data.length; i++){
      if(i == data.length - 1){
        if(data[i].KHACHHANG_DIMENSION == 'BuuDien'){
          $('table tbody').append(
            "<tr id = '" + data[i].VANPHONGDAIDIEN_DIMENSION + "' class = '" + data[i].VANPHONGDAIDIEN_DIMENSION.replace(/ /g,'') + "' >" +
            "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "<td>0</td>" +
            "<td class = 'pr-5'>0</td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "</tr>"
          );
        }
        else{
         $('table tbody').append(
          "<tr id = '" + data[i].VANPHONGDAIDIEN_DIMENSION + "' class = '" + data[i].VANPHONGDAIDIEN_DIMENSION.replace(/ /g,'') + "' >" +
           "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
           "<td>0</td>" +
           "<td class = 'pr-5'>0</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "</tr>"
         );
        }
       }
       else{
        if(data[i].VANPHONGDAIDIEN_DIMENSION == data[i+1].VANPHONGDAIDIEN_DIMENSION){
          var tongSL = data[i].SOLUONG + data[i+1].SOLUONG;
          var tongTien = data[i].TONGTIEN + data[i+1].TONGTIEN;
           $('table tbody').append(
            "<tr id = '" + data[i].VANPHONGDAIDIEN_DIMENSION + "' class = '" + data[i].VANPHONGDAIDIEN_DIMENSION.replace(/ /g,'') + "' >" +
             "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
             "<td>" + data[i].SOLUONG + "</td>" +
             "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
             "<td>" + data[i+1].SOLUONG + "</td>" +
             "<td class = 'pr-5'>" + data[i+1].TONGTIEN + "</td>" +
             "<td>" + tongSL + "</td>" +
             "<td class = 'pr-5'>" + tongTien + "</td>" +
             "</tr>"
           );
           i++;
        }
        else if(data[i].KHACHHANG_DIMENSION == 'BuuDien'){
          $('table tbody').append(
            "<tr id = '" + data[i].VANPHONGDAIDIEN_DIMENSION + "' class = '" + data[i].VANPHONGDAIDIEN_DIMENSION.replace(/ /g,'') + "' >" +
            "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "<td>0</td>" +
            "<td class = 'pr-5'>0</td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "</tr>"
          );
        }
        else{
         $('table tbody').append(
          "<tr id = '" + data[i].VANPHONGDAIDIEN_DIMENSION + "' class = '" + data[i].VANPHONGDAIDIEN_DIMENSION.replace(/ /g,'') + "' >" +
           "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
           "<td>0</td>" +
           "<td class = 'pr-5'>0</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "</tr>"
         );
        }
       }
     }
  });
}

function getDetailData(url, class_name){
    const words = class_name.split(' ');
    row = $('tr.' + words[0]);
    $.ajax({
    method: 'GET',
    url: url,
  }).done(function (data) {
     for(let i = 0; i < data.length; i++){
      if(i == data.length - 1){
        if(data[i].KHACHHANG_DIMENSION == 'BuuDien'){
          row.after(
            "<tr class = 'children'>" +
            "<td colspan='2' style='color:blue;'>" + data[i].LONG_DESCRIPTION + "&emsp;</td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "<td>0</td>" +
            "<td class = 'pr-5'>0</td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "</tr>"
          );
        }
        else{
          row.after(
          "<tr class = 'children'>" +
           "<td colspan='2' style='color:blue;'>" + data[i].LONG_DESCRIPTION + "&emsp;</td>" +
           "<td>0</td>" +
           "<td class = 'pr-5'>0</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "</tr>"
         );
        }
       }
       else{
        if(data[i].VANPHONGDAIDIEN_DIMENSION == data[i+1].VANPHONGDAIDIEN_DIMENSION){
          var tongSL = data[i].SOLUONG + data[i+1].SOLUONG;
          var tongTien = data[i].TONGTIEN + data[i+1].TONGTIEN;
            row.after(
            "<tr class = 'children'>" +
             "<td colspan='2' style='color:blue;'>" + data[i].LONG_DESCRIPTION + "&emsp;</td>" +
             "<td>" + data[i].SOLUONG + "</td>" +
             "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
             "<td>" + data[i+1].SOLUONG + "</td>" +
             "<td class = 'pr-5'>" + data[i+1].TONGTIEN + "</td>" +
             "<td>" + tongSL + "</td>" +
             "<td class = 'pr-5'>" + tongTien + "</td>" +
             "</tr>"
           );
           i++;
        }
        else if(data[i].KHACHHANG_DIMENSION == 'BuuDien'){
          row.after(
            "<tr class = 'children'>" +
            "<td colspan='2' style='color:blue;'>" + data[i].LONG_DESCRIPTION + "&emsp;</td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "<td>0</td>" +
            "<td class = 'pr-5'>0</td>" +
            "<td>" + data[i].SOLUONG + "</td>" +
            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
            "</tr>"
          );
        }
        else{
          row.after(
          "<tr class = 'children'>" +
           "<td colspan='2' style='color:blue;'>" + data[i].LONG_DESCRIPTION + "&emsp;</td>" +
           "<td>0</td>" +
           "<td class = 'pr-5'>0</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "<td>" + data[i].SOLUONG + "</td>" +
           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
           "</tr>"
         );
        }
       }
     }
  });
}

// function getDataCbBox(url){
//   $('table tbody').find('tr').remove();
//   $('table tbody').append("<tr>" +
//   "<td colspan='2'></td>" +
//   "<td>Số lượng</td>" +
//   "<td class='pr-5'>Tổng tiền</td>" + 
//   "<td>Số lượng</td>" + 
//   "<td class='pr-5'>Tổng tiền</td>" + 
//   "<td>Số lượng</td>" + 
//   "<td class='pr-5'>Tổng tiền</td>" + 
// "</tr>")
//   $.ajax({
//   method: 'GET',
//   url: url,
// }).done(function (data) {
//    for(let i = 0; i < data.length; i++){
//      if(i == data.length - 1){
//       if(data[i].KHACHHANG_DIMENSION == 'BuuDien'){
//         $('table tbody').append(
//           "<tr>" +
//           "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
//           "<td>" + data[i].SOLUONG + "</td>" +
//           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//           "<td>0</td>" +
//           "<td class = 'pr-5'>0</td>" +
//           "<td>" + data[i].SOLUONG + "</td>" +
//           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//           "</tr>"
//         );
//       }
//       else{
//        $('table tbody').append(
//          "<tr>" +
//          "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
//          "<td>0</td>" +
//          "<td class = 'pr-5'>0</td>" +
//          "<td>" + data[i].SOLUONG + "</td>" +
//          "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//          "<td>" + data[i].SOLUONG + "</td>" +
//          "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//          "</tr>"
//        );
//       }
//      }
//      else{
//       if(data[i].VANPHONGDAIDIEN_DIMENSION == data[i+1].VANPHONGDAIDIEN_DIMENSION){
//         var tongSL = data[i].SOLUONG + data[i+1].SOLUONG;
//         var tongTien = data[i].TONGTIEN + data[i+1].TONGTIEN;
//          $('table tbody').append(
//            "<tr>" +
//            "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
//            "<td>" + data[i].SOLUONG + "</td>" +
//            "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//            "<td>" + data[i+1].SOLUONG + "</td>" +
//            "<td class = 'pr-5'>" + data[i+1].TONGTIEN + "</td>" +
//            "<td>" + tongSL + "</td>" +
//            "<td class = 'pr-5'>" + tongTien + "</td>" +
//            "</tr>"
//          );
//          i++;
//       }
//       else if(data[i].KHACHHANG_DIMENSION == 'BuuDien'){
//         $('table tbody').append(
//           "<tr>" +
//           "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
//           "<td>" + data[i].SOLUONG + "</td>" +
//           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//           "<td>0</td>" +
//           "<td class = 'pr-5'>0</td>" +
//           "<td>" + data[i].SOLUONG + "</td>" +
//           "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//           "</tr>"
//         );
//       }
//       else{
//        $('table tbody').append(
//          "<tr>" +
//          "<td colspan='2'>" + data[i].VANPHONGDAIDIEN_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
//          "<td>0</td>" +
//          "<td class = 'pr-5'>0</td>" +
//          "<td>" + data[i].SOLUONG + "</td>" +
//          "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//          "<td>" + data[i].SOLUONG + "</td>" +
//          "<td class = 'pr-5'>" + data[i].TONGTIEN + "</td>" +
//          "</tr>"
//        );
//       }
//      }
//    }
// });
// }






