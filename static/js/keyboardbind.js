
//driver
// keycode 65 = a A
// keycode 68 = d D
// keycode 83 = s S
// keycode 87 = w W

//servo
// keycode 37 = Left
// keycode 38 = Up
// keycode 39 = Right
// keycode 40 = Down

document.onkeydown = function (event) {
    var e = event || window.event;
    var keyCode = e.keyCode || e.which;
    switch (keyCode) {
        //driver
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
        //servo
        case 38:
            $("#up").click();
            break;
        case 40:
            $("#down").click();
            break;
        case 37:
            $("#left").click();
            break;
        case 39:
            $("#right").click();
            break;
        default:
            break;
    }
}

document.onkeyup = function (event) {
    var e = event || window.event;
    var keyCode = e.keyCode || e.which;
    switch (keyCode) {
        //driver
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
        //servo
        case 38:
            $("#reset").click();
            break;
        case 40:
            $("#reset").click();
            break;
        case 37:
            $("#reset").click();
            break;
        case 39:
            $("#reset").click();
            break;
        default:
            break;
    }
}


