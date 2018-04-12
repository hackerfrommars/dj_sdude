  // password detail with js function
  $('#change_password').click(function(){
  $('#change_password').fadeIn(function(){

    $("#password_detail").fadeIn();
  });
});

  $(".close").click(function(){
  $("#password_detail").fadeOut(100);
  
});


// search ajax
    $(".chosen-select").fadeIn().chosen();

//end