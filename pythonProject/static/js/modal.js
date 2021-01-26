var anchors = document.getElementsByClassName("open-AddBookDialog");
var myValue = -1;
for (var i = 0; i < anchors.length; i++) {
    var anchor = anchors[i];
    anchor.onclick = function () {
        var alt = $(this).attr("alt");
        myValue = alt;
        document.getElementById('id01').style.display = 'block'
    }
}