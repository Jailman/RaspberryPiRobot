
$(function() {
    var htmlStr;
    $.ajax({
        url: "/power",
        async: false,
        success: function(htmlString) {
            htmlStr = htmlString;
            // $("#status").html(htmlStr);
            if (htmlStr == 'off') {
                $('#power').attr('src', "/static/btimg/off.png");
            };
            if (htmlStr == 'on') {
                $('#power').attr('src', "/static/btimg/on.png");
            };
        },
    });
});


function changeImage() {
    element = document.getElementById('power');
    if (element.src.match("on")) {
        $.get('/power/off')
        element.src = "/static/btimg/off.png";
        // $("#status").html("off");
    } else {
        $.get('/power/on')
        element.src = "/static/btimg/on.png";
        // $("#status").html("on");
    }
}

