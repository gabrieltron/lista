function newli() {
    var afazer = $("#todo").val();
    $("#todo").val('');
    var atual =  $("#sortable1").html();
    if (afazer != null && afazer != "")
      $("#sortable1").append("<li class=\"collection-item\">" + afazer + "</li>");
}

function newrow() {
    var row = $("#newrow").val();
    $("#newrow").val('');
    var atual = $("#rows").html();
    if (row != null && row != "")
      $("#rows").html(atual + "<ul id=\"sortable1\" class=\"connectedSortable\">"
        +"<li class=\"ui-state-disabled collection-header\"><h5>" + row + "</h5></li>"
        +"</ul>")
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

function updateRows() {
  var rows = [];
  $(".collection-header").each(
    function(){
      rows.push($(this).text());
    }
  );

  var csrftoken = getCookie('csrftoken');

  $.ajax({
    type: "POST",
    url: "updateRows/",
    data: { csrfmiddlewaretoken: "csrftoken",
            rows:"rows"
          },
    dataType: "json",
    success: function() {
      window.alert("NOICE");
    }
  });
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
      newrow();
      updateRows();
    }
  });

});
