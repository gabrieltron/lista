function newli() {
    var afazer = $("#todo").val();
    $("#todo").val('');
    var atual =  $("#sortable1").html();
    if (afazer != null && afazer != "")
    $("#sortable1").html(atual + "<li class=\"collection-item\">" + afazer + "</li>");
}

$(function() {
  $("#sortable1, #sortable2, #sortable3, #sortable4").sortable( {
    items: "li:not(.ui-state-disabled)"
  });
  $("#sortable1, #sortable2, #sortable3, #sortable4").sortable( {
    connectWith: ".connectedSortable"
  });

  $("#sortable1 li, #sortable2 li, #sortable3 li, #sortable4 li").disableSelection();

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

});
