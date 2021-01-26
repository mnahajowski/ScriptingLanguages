$(function () {
    $("#tags").autocomplete({
        source: myData,
        minLength: 2
    });
});

