//init servo
var y=6.0;
var x=6.0;

//rise servo
function riseup(){
        y=y+0.1;
        $("#vtc").html(y.toFixed(1));
}

//down servo
function falldown(){
            y=y-0.1;
            $("#vtc").html(y.toFixed(1));
}

//right servo
function rightup(){
        x=x+0.1;
        $("#hrz").html(x.toFixed(1));
}

//left servo
function leftdown(){
            x=x-0.1;
            $("#hrz").html(x.toFixed(1));
}


$(function() {
    $("#vtc").html(y.toFixed(1));
    $("#hrz").html(x.toFixed(1));
    //reset button
    $("#reset").click(function() {
        y=6.0;
        $("#vtc").html(y.toFixed(1));
        x=6.0;
        $("#hrz").html(x.toFixed(1));
    });

    $("#up").mousedown(function() {
        var timer1=setInterval("riseup()", 100);
        $("#up").mouseup(function() {
            clearInterval(timer1);
        });   
    });   

    $("#down").mousedown(function() {
        var timer2=setInterval("falldown()", 100);
        $("#down").mouseup(function() {
            clearInterval(timer2);
        });   
    });   

    $("#right").mousedown(function() {
        var timer3=setInterval("rightup()", 100);
        $("#right").mouseup(function() {
            clearInterval(timer3);
        });   
    });   

    $("#left").mousedown(function() {
        var timer4=setInterval("leftdown()", 100);
        $("#left").mouseup(function() {
            clearInterval(timer4);
        });   
    });   
});