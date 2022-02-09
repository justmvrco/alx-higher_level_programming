$(document).ready(function () {
    $.ajax({
        url: "https://fourtonfish.com/hellosalut/?lang=fr",
        type: "GET",
        datatype: "json",
    })
    .done(function( json ){
        $("DIV#hello").text(json.hello);
    })
});
