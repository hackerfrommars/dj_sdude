  // add syllabus
  $('#add_syl').click(function(){
  $('#add_syl').fadeIn(function(){

    $("#syllabuses").fadeIn();
    $(".chosen-teacher").fadeIn();
    $(".chosen-teacher").chosen();
  });
});
      // add assignments

  $('#add_ass').click(function(){
  $('#add_ass').fadeIn("slow",function(){

    $("#assignments").fadeIn();
    $(".chosen-teacher").fadeIn();
    $(".chosen-teacher").chosen();
  });
});

  // add quiz

  $('#add_quiz').click(function(){
  $('#add_quiz').fadeIn("slow",function(){

    $("#quizes").fadeIn();
    $(".chosen-teacher").fadeIn();
    $(".chosen-teacher").chosen();
  });
});

  // add midterm

  $('#add_mid').click(function(){
  $('#add_mid').fadeIn("slow",function(){

    $("#midterms").fadeIn();
    $(".chosen-teacher").fadeIn();
    $(".chosen-teacher").chosen();
  });
});

  // add final

  $('#add_fin').click(function(){
  $('#add_fin').fadeIn("slow",function(){

    $("#finals").fadeIn();
    $(".chosen-teacher").fadeIn();
    $(".chosen-teacher").chosen();
  });
});

  // add feedback

  $('#add_feed').click(function(){
  $('#add_feed').fadeIn("slow",function(){

    $("#feedbacks").fadeIn();
    $(".chosen-teacher").fadeIn();
    $(".chosen-teacher").chosen();
  });
});
//один общий cancel для всех окон add exams with javascript
$(".cancel").click(function(){
  $("#syllabuses").fadeOut(100);
  $("#assignments").fadeOut(100);
  $("#quizes").fadeOut(100);
  $("#midterms").fadeOut(100);
  $("#finals").fadeOut(100);
  $("#feedbacks").fadeOut(100);
  $(".chosen-teacher").fadeOut(8);
  $(".chosen-teacher").chosen("destroy");
});
//end of cancel add exams


// show exam
    var syl = document.getElementById("myfirst");
    var ass = document.getElementById("mysecond");
    var quiz = document.getElementById("mythree");
    var mid = document.getElementById("myfour");
    var fin = document.getElementById("myfive");
    var feed = document.getElementById("mysix");
    var tit = document.getElementById("mysix");


function first() {
    if (syl.style.display === "none") {
        syl.style.display = "block";
        document.getElementById("title").innerHTML = "Syllabus";
        ass.style.display = "none";
        quiz.style.display = "none";
        mid.style.display = "none";
        fin.style.display = "none";
        feed.style.display = "none";

    } else {
        syl.style.display = "none";
    }
}
function second() {
    if (ass.style.display === "none") {
        ass.style.display = "block";
        document.getElementById("title").innerHTML = "Assignment";
        syl.style.display = "none";
        quiz.style.display = "none";
        mid.style.display = "none";
        fin.style.display = "none";
        feed.style.display = "none";

    } else {
        ass.style.display = "none";
    }
}
function three() {
    if (quiz.style.display === "none") {
        quiz.style.display = "block";
        document.getElementById("title").innerHTML = "Quiz";
        ass.style.display = "none";
        syl.style.display = "none";
        mid.style.display = "none";
        fin.style.display = "none";
        feed.style.display = "none";

    } else {
        quiz.style.display = "none";
    }
}
function four() {
    if (mid.style.display === "none") {
        mid.style.display = "block";
        document.getElementById("title").innerHTML = "Midterm";
        ass.style.display = "none";
        quiz.style.display = "none";
        syl.style.display = "none";
        fin.style.display = "none";
        feed.style.display = "none";


    } else {
        mid.style.display = "none";
    }
}
function five() {
    if (fin.style.display === "none") {
        fin.style.display = "block";
        document.getElementById("title").innerHTML = "Final";
        ass.style.display = "none";
        quiz.style.display = "none";
        mid.style.display = "none";
        syl.style.display = "none";
        feed.style.display = "none";

    } else {
        fin.style.display = "none";
    }
}
function six() {
    if (feed.style.display === "none") {
        feed.style.display = "block";
        document.getElementById("title").innerHTML = "FeedBack";
        ass.style.display = "none";
        quiz.style.display = "none";
        mid.style.display = "none";
        fin.style.display = "none";
        syl.style.display = "none";

    } else {
        feed.style.display = "none";
    }
}


// search ajax
    $(".chosen-select").fadeIn().chosen();

//end