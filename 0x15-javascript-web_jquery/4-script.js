$(document).ready(function(){
    $("DIV#toggle_header").click(function() {
        classCheck = $("header").hasClass("red");
        if (classCheck) {
            $("header").removeClass("red").addClass("green");
        } else {
            $("header").removeClass("green").addClass("red");
        }
    });
});
