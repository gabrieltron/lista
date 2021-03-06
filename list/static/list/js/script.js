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
				$("ul").first().append("<li class=\"item\"><div class=\"collection-item\">" + afazer + "</div><i class=\"material-icons remove\">remove_circle_outline</i></li>");
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

function deleteRow(row) {
	var csrftoken = getCookie('csrftoken');
	$.ajax({
		type: 'POST',
		url: 'deleteRow/',
		data: {
			csrfmiddlewaretoken: csrftoken,
			row: row
		},
		dataType: 'json'
	});
}

function updateItems(dest_row) {
	var item_names = [];
	$(dest_row).find(".collection-item").each(
		function() {
			item_names.push($(this).text());
		}
	);
	var dest_name = $(dest_row).find(".collection-header").text();

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

function getPermission() {
	var csrftoken = getCookie('csrftoken');
	var number_rows = $('ul').length;
	var permission;
	$.ajax({
		async: false,
		type: 'POST',
		url: 'checkPermission/',
		data: {
			csrfmiddlewaretoken: csrftoken,
			number_rows: number_rows
		},
		dataType: 'json',
		success: function(data) {
			if (data.permission) {
				permission = true;

			} else {
				alert("Seu plano atual não permite mais colunas");
				permission = false;
			}
		}
	});
	return permission;
}

function newrow(name) {
	var csrftoken = getCookie('csrftoken');
	var allowed = getPermission();
	if (allowed) {
		$.ajax({
			type: "POST",
			url: "createRow/",
			data: { csrfmiddlewaretoken: csrftoken,
					name: name
				  },
			dataType: 'json',
			success: function(data) {
				if (data.exist) {
					alert("Já existe uma coluna com esse nome");
				} else {
					$("#newrow").val('');
					$("#rows").append("<ul class=\"connectedSortable\">"
						+"<li class=\"ui-state-disabled\"><div class='collection-header'><h5>" + name + "</h5></div><i class='material-icons remove-row'>remove_circle_outline</i></li>"
						+"</ul>");
					$(".connectedSortable").sortable( {
						items: "li:not(.ui-state-disabled)",
						connectWith: ".connectedSortable"
					});
				}
			}
		});
	}
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
	$(".connectedSortable").sortable( {
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
				deleteItem(bfr_row, $(ui.item).children(".collection-item").text());
			}
		}
	});

	$(document).ready(function(){
		// the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
		$('.modal').modal({
			ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
				$('.carousel').carousel();
      		}
		});
	});

	$("#rows").sortable( {
		items: 'ul',
		connectWith: "#rows",
		stop: function(event, ui) {
			updateRows();
		}
	});

	$(".collection-header").disableSelection();

	$(".add-remove").on('click', '.btn1', function() {
		var afazer = $("#todo").val();
		$("#todo").val('');
		if ($('.connectedSortable').length == 0) {
			alert("Nenhuma coluna disponível!");
		}
		else if (afazer != null && afazer != "")  
			newli(afazer);
	});

	$(".add-remove").on('keypress', '#todo', function(e) {
		if(e.which == 13) {
			var afazer = $("#todo").val();
			$("#todo").val('');
			if ($('.connectedSortable').length == 0) {
				alert("Nenhuma coluna disponível!");
			}
			else if (afazer != null && afazer != "")
				newli(afazer);
		}
	});

	$(".add-remove").on('click', '#btn3', function() {
		var name = $("#newrow").val();
		if (name != null && name != "")
			newrow(name);
	});

	$(".add-remove").on('keypress', '#newrow', function(e) {
		if(e.which == 13) {
			e.preventDefault();
			var name = $("#newrow").val();
			if (name != null && name != "")
				newrow(name);
		}
	});

	$(".lists").on('click', '.remove', function() {
		var item = $(this).parent().find(".collection-item").text();
		var row = $(this).parent().parent().find(".collection-header").text();
		$(this).parent().remove();
		deleteItem(row, item);
	});

	$(".lists").on('click', '.remove-row', function() {
		var row = $(this).parent().children(".collection-header").text();
		$(this).parent().parent().remove();
		deleteRow(row);
	});

	$(".add-remove").on('click', '#logoff', function() {
		var csrftoken = getCookie('csrftoken');
		$.ajax({
			type: 'POST',
			url: 'logoff/',
			data: {
				csrfmiddlewaretoken: csrftoken
			},
			dataType: 'json'
		});
	});

	$("#pagar").on('click', function() {
		var csrftoken = getCookie('csrftoken');
		$.ajax({
			type: 'POST',
			url: 'upgradeUser/',
			data: {
				csrfmiddlewaretoken: csrftoken
			},
			dataType: 'json'
		});
	});
});
