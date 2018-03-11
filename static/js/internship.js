  // show more information about internship
  $('#show_more').click(function(){
  $('#show_more').fadeIn(function(){

    $("#internship_info").fadeIn();
  });
});

  $(".cancel").click(function(){
  $("#internship_info").fadeOut(100);
  
});