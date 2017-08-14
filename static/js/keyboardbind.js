
document.onkeydown = function (event) {
    var e = event || window.event;
    var keyCode = e.keyCode || e.which;
    switch (keyCode) {
        case 87:
            $("#robot_up").click();
            break;
        case 83:
            $("#robot_down").click();
            break;
        case 65:
            $("#robot_left").click();
            break;
        case 68:
            $("#robot_right").click();
            break;
        default:
            break;
    }
}

document.onkeyup = function (event) {
    var e = event || window.event;
    var keyCode = e.keyCode || e.which;
    switch (keyCode) {
        case 87:
            $("#robot_stop").click();
            break;
        case 83:
            $("#robot_stop").click();
            break;
        case 65:
            $("#robot_stop").click();
            break;
        case 68:
            $("#robot_stop").click();
            break;
        default:
            break;
    }
}
