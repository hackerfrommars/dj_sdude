var modal_i = document.getElementById("internship_info");

// Get the button that opens the modal_i
var btn_i = document.getElementById("show_more");

// Get the <span_i> element that closes the modal_i

// When the user clicks the button, open the modal_i 
btn_i.onclick = function() {
    modal_i.style.display = "block";
}


// When the user clicks anywhere outside of the modal_i, close it
window.onclick = function(event) {
    if (event.target == modal_i) {
        modal_i.style.display = "none";
    }
}
  // show more information about internship
//   var $ = jQuery;

//   $('#show_more').click(function(){
//   $('#show_more').fadeIn(function(){
//   console.log('show_more');

//     $("#internship_info").fadeIn();
//   });
// });

  $(".cancel").click(function(){
  modal_i.style.display = "none";
  
});

var hot_q = document.getElementById("hot_questions");
var top_q = document.getElementById("top_questions");


function hot() {
		hot_q.style.display = "block";
		document.getElementById("title").innerHTML = "HOT questions";
		top_q.style.display = "none";
		  console.log('show hot');


	
}
function tops() {
		top_q.style.display = "block";
		document.getElementById("title").innerHTML = "TOP questions";
		hot_q.style.display = "none";
	    console.log('show top');

	
}
