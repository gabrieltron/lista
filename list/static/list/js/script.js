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

  var allRows = [];
  $("#rows, #rows1").sortable( {
    connectWith: ".rows",
    update: function(event, ui) {
      if (this === ui.item.parent()[0]){
        $( "ul" ).each(function( index ) {
          allRows.push($(this).html());
        });
        window.alert(allRows);
        $(".lists").html("<div class=\"row rows ui-state-default\" id=\"rows1\">");
        for (i = 0; i < allRows.length; i++) {
          var atual =  $("#rows1").html();
          if (allRows[i] != '') {
            window.alert(allRows[i]);
            $("#rows1").append("<ul id=\"sortable1\" class=\"connectedSortable collection col s3\">" + allRows[i] +  "</ul>");
          }
        }
        $(".lists").append("</div>");
    }
    },
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
