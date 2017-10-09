function newli(afazer) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
      type: 'POST',
      url: 'compareItem/',
      data: { text: afazer,
              csrfmiddlewaretoken: csrftoken
            },
      dataType: 'json',
      success: function(data) {
        if (data.exist) {
          alert("Já existe uma tarefa com esse nome!");
        } else {
          $("ul").first().append("<li class=\"collection-item\">" + afazer + "</li>");
          var row = $("ul").first();
          updateItems(row);
        }
      }
    });
}

function deleteItem(row, item) {
  var csrftoken = getCookie('csrftoken');
  $.ajax({
    type: 'POST',
    url: 'deleteItem/',
    data: { csrfmiddlewaretoken: csrftoken,
            row: row,
            item: item
          },
    dataType: 'json'
  });
}

function updateItems(dest_row) {
  var item_names = [];
  $(dest_row).children(".collection-item").each(
    function() {
      item_names.push($(this).text());
    }
  );

  var dest_name = $(dest_row).children(".collection-header").text();

  var csrftoken = getCookie('csrftoken');
  $.ajax({
    type: 'POST',
    url: 'updateLists/',
    data: { csrfmiddlewaretoken: csrftoken,
            item_names: item_names,
            dest_row: dest_name
          },
    dataType: 'json'
  });
}

function newrow(name) {
  var csrftoken = getCookie('csrftoken');

  $.ajax({
    type: "POST",
    url: "createRow/",
    data: { csrfmiddlewaretoken: csrftoken,
        name: name
          },
    dataType: 'json',
    success: function(data) {
      if (data.exist) {
        alert("Já existe uma coluna com esse nome")
      } else {
        $("#newrow").val('');
        var atual = $("#rows").html();
        $("#rows").html(atual + "<ul id=\"sortable1\" class=\"connectedSortable\">"
          +"<li class=\"ui-state-disabled collection-header\"><h5>" + name + "</h5></li>"
          +"</ul>")
      }
    }
  });
}

function updateRows() {
  var row_names = [];
  $(".collection-header").each(
    function(){
      row_names.push($(this).text());
    }
  );
  var csrftoken = getCookie('csrftoken');

  $.ajax({
    type: "POST",
    url: 'updateRows/',
    data: { csrfmiddlewaretoken: csrftoken,
            row_names: row_names
          },
    dataType: 'json'
  });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function() {
  var bfr_row = "";
  $("#sortable1, #sortable2").sortable( {
    items: "li:not(.ui-state-disabled)",
    connectWith: ".connectedSortable",
    start: function(event, ui) {
      $(ui.item).css('border', '1px solid #e3e4e5');
      bfr_row = $(ui.item).parent().find(".collection-header").text();
    },
    stop: function(event, ui) {
      $(ui.item).css('border', 'none');
      $(ui.item).css('border-top', '1px solid #e3e4e5');
      updateItems($(ui.item).parent());
      dest_row = $(ui.item).parent().find(".collection-header").text();
      if (dest_row != bfr_row) {
        deleteItem(bfr_row, $(ui.item).text());
      }
    }
  });

  $("#rows").sortable( {
    connectWith: ".rows",
    stop: function(event, ui) {
      updateRows();
    }
  });

  $("#sortable1 li, #sortable2 li").disableSelection();
  $("#rows").disableSelection();

  $("#btn1").click(function() {
    var afazer = $("#todo").val();
    $("#todo").val('');
    if (afazer != null && afazer != "")  
      newli(afazer);
  });

  $("input#todo").keypress(function(e) {
    if(e.which == 13) {
      var afazer = $("#todo").val();
      $("#todo").val('');
      if (afazer != null && afazer != "")
        newli(afazer);
    }
  });

  $("#btn2").click(function() {
    var last = $("ul").last();
    $(last).find('li:not(:first)').remove();
  });

  $("#btn3").click(function() {
      var name = $("#newrow").val();
      if (name != null && name != "")
        newrow(name);
  });

  $("input#newrow").keypress(function(e) {
    if(e.which == 13) {
      e.preventDefault();
      var name = $("#newrow").val();
      if (name != null && name != "")
        newrow(name);
    }
  });

});
