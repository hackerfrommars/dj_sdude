$(".chosen-select").fadeIn().chosen();
$(".chosen-teacher").fadeIn().chosen();

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