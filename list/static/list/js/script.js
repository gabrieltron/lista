function newli() {
    var afazer = $("#todo").val();
    $("#todo").val('');
    var atual =  $("#sortable1").html();
    if (afazer != null && afazer != "")
      $("#sortable1").html(atual + "<li class=\"collection-item\">" + afazer + "</li>");
}

function newrow() {
    var row = $("#newrow").val();
    $("#newrow").val('');
    var atual = $("#rows").html();
    if (row != null && row != "")
      $("#rows").html(atual + "<ul id=\"sortable1\" class=\"connectedSortable collection col s3\">"
        +"<li class=\"ui-state-default ui-state-disabled collection-header\"><h5>" + row + "</h5></li>"
        +"</ul>")
}

$(function() {
  $("#sortable1, #sortable2").sortable( {
    items: "li:not(.ui-state-disabled)",
    connectWith: ".connectedSortable",
  });

  $("#rows, #rows1").sortable( {
    connectWith: ".rows",
  });

  $("#sortable1 li, #sortable2 li, #sortable3 li, #sortable4 li").disableSelection();
  $("#rows, #rows1").disableSelection();

  $("#btn1").click(function() {
    newli();
  });

  $("input#todo").keypress(function(e) {
    if(e.which == 13) {
      newli();
    }
  });

  $("#btn2").click(function() {
    $("#sortable4 li").not(".ui-state-disabled").remove();
  });

  $("#btn3").click(function() {
    newrow();
  });

  $("input#newrow").keypress(function(e) {
    if(e.which == 13) {
      newrow();
      window.alert($("#rows ul").length);
    }
  });

});
