$(document).ready(function () {
    console.log('Hello')
    sp_combo_box = $('#sp-combo-box');
  
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
  
    getData('http://127.0.0.1:8000/store/thanhpho/');

    $('button').click(function(){
      id_sp = $('#sp-combo-box').val();
      if(id_sp == 0){
        getData('http://127.0.0.1:8000/store/thanhpho/');
      }
      else{
        getData('http://127.0.0.1:8000/store/thanhpho/sanpham/' + id_sp + '/');
      }
    });


    $("#table-store").on('click', 'tbody tr', function(){
      $(this).toggleClass("show")
      if($(this).hasClass('show')){
        id_sp = $('#sp-combo-box').val();
        var id_tr = encodeURIComponent($(this).attr('id'))
        if(id_sp == 0){
            getDetailData('http://127.0.0.1:8000/store/thanhpho/' + id_tr + '/', $(this).attr('class'));
          }
          else{
            getDetailData('http://127.0.0.1:8000/store/thanhpho/'  + id_tr + '/' + id_sp + '/', $(this).attr('class'));
          }
      }
      else{
        $("#table-store tbody ").find("tr.children").remove();
      }
    });
});


function getData(url){
    $('table tbody').find('tr').remove();
      $.ajax({
      method: 'GET',
      url: url,
    }).done(function (data) {
       for(let i = 0; i < data.length; i++){
        $('table tbody').append(
          "<tr id = '" + data[i].CUAHANG_DIMENSION + "' class = '" + data[i].CUAHANG_DIMENSION.replace(/ /g,'') + "' >" +
            "<td>" + data[i].CUAHANG_DIMENSION + "&emsp;<i class='ti-control-play'></i></td>" +
            "<td>" + data[i].SOLUONG+ "</td>" +
          "</tr>"
        );
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
              row.after(
                "<tr class = 'children'>" +
                "<td style='color:blue;'>" + data[i].CUAHANG_DIMENSION + "&emsp;</td>" +
                "<td>" + data[i].SOLUONG + "</td>" +
                "</tr>"
            );
        }
    });
}