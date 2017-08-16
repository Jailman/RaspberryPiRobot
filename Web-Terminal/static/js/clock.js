$(document).ready(function() {

    // 创建两个变量，一个数组中的月和日的名称
    var monthNames = [ "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月" ]; 
    var dayNames= ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]

    // 创建一个对象newDate（）
    var newDate = new Date();
    // 提取当前的日期从日期对象
    newDate.setDate(newDate.getDate());
    //输出的日子，日期，月和年
    $('#Date').html(newDate.getFullYear() + " " + monthNames[newDate.getMonth()] + ' ' + newDate.getDate() + ' ' + dayNames[newDate.getDay()]);

    setInterval( function() {
        // 创建一个对象，并提取newDate（）在访问者的当前时间的秒
        var seconds = new Date().getSeconds();
        //添加前导零秒值
        $("#sec").html(( seconds < 10 ? "0" : "" ) + seconds);
    },1000);
    
    setInterval( function() {
        // 创建一个对象，并提取newDate（）在访问者的当前时间的分钟
        var minutes = new Date().getMinutes();
        // 添加前导零的分钟值
        $("#min").html(( minutes < 10 ? "0" : "" ) + minutes);
    },1000);
    
    setInterval( function() {
        // 创建一个对象，并提取newDate（）在访问者的当前时间的小时
        var hours = new Date().getHours();
        // 添加前导零的小时值
        $("#hours").html(( hours < 10 ? "0" : "" ) + hours);
    }, 1000);
    
}); 
