$(document).ready(function () {
    $.ajax({
        url: "https://swapi-api.hbtn.io/api/films/?format=json",
        type: "GET",
        datatype: "json",
    })
    .done(function( json ){
        data = json.results;
        for (let i = 0; i < data.length; i++) {
            $("UL#list_movies").append("<li>" + data[i].title + "</li>");
        }
    })
});
