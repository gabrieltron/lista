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
    }
  });

});
