  // show more information about internship
  var $ = jQuery;

  $('#show_more').click(function(){
  $('#show_more').fadeIn(function(){
  console.log('show_more');

    $("#internship_info").fadeIn();
  });
});

  $(".cancel").click(function(){
  $("#internship_info").fadeOut(100);
  
});
var hot_q = document.getElementById("hot_questions");
var top_q = document.getElementById("top_questions");


function hot() {
	if (hot_q.style.display === "none") {
		hot_q.style.display = "block";
		document.getElementById("title").innerHTML = "HOT questions";
		top_q.style.display = "none";
		  console.log('show hot');


	} else {
		hot_q.style.display = "none";
				document.getElementById("title").innerHTML = "";

	}
}
function tops() {
	if (top_q.style.display === "none") {
		top_q.style.display = "block";
		document.getElementById("title").innerHTML = "TOP questions";
						hot_q.style.display = "none";
			  console.log('show top');


	} else {
		top_q.style.display = "none";
				document.getElementById("title").innerHTML = "";

	}
}
$('button').on('click', function(){
    $('button').removeClass('selected');
    $(this).addClass('selected');
      console.log('button selected');

});