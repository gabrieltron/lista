function newli() {
    var afazer = $("#todo").val();
    $("#todo").val('');
    var atual =  $("#sortable1").html();
    if (afazer != null && afazer != "")
      $("#sortable1").append("<li class=\"collection-item\">" + afazer + "</li>");
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
    url: "updateRows/",
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
  $("#sortable1, #sortable2").sortable( {
    items: "li:not(.ui-state-disabled)",
    connectWith: ".connectedSortable",
    start: function(event, ui) {
      $(ui.item).css('border', '1px solid #e3e4e5');
    },
    stop: function(event, ui) {
      $(ui.item).css('border', 'none');
      $(ui.item).css('border-top', '1px solid #e3e4e5');
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
    newli();
  });

  $("input#todo").keypress(function(e) {
    if(e.which == 13) {
      newli();
    }
  });

  $("#btn2").click(function() {
    var last = $("ul").last();
    $(last).find('li:not(:first)').remove();
  });

  $("#btn3").click(function() {
    newrow();
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
