$(document).ready(function () {
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
          quy_combo_box.attr('disabled', 'disabled');
        }
      });
  });
});
