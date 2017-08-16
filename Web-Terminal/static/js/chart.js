$(function() {
    //声明报表对象  
    var chart = new Highcharts.Chart({

        chart: {
            //将报表对象渲染到层上  
            renderTo: 'temperature',
            //设置背景透明
            //backgroundColor: 'rgba(255,255,90,0.7)'  
        },
        //设定报表对象的初始数据  
        series: [{
            data: []
        }],
        title: { text: '<b style="color:red;font-size:1.3em">温度</b>' },
        subtitle: { text: 'Source: www.karachiwarship.top' },
        credits: { enabled: false },
        xAxis: {
            title:{text: 'Time'},
            categories: ['1:00', '1:05', '1:10', '1:15', '1:20', '1:25',
                '1:30', '1:35', '1:40', '1:45', '1:50', '1:55'
            ]
        },
        exporting: {
            url: 'http://export.hcharts.cn/'
        },
        yAxis: {
            title: {
                text: 'Temperature (\xB0C)',
                //color: '#808080'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '\xB0C'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },

    });

    function getForm() {
        //使用JQuery从后台获取温度JSON格式的数据  
        jQuery.getJSON('/get_temperature', null, function(data) {
            //为图表设置值  
            chart.series[0].setData(data);
        });
        jQuery.getJSON('/get_time', null, function(data) {
            //为图表设置值  
            chart.xAxis[0].setCategories(data);
        });

    }


    $(document).ready(function() {
        //每隔3秒自动调用方法，实现图表的实时更新  
        window.setInterval(getForm, 5000);

    });


});


$(function() {
    //声明报表对象  
    var chart = new Highcharts.Chart({

        chart: {
            //将报表对象渲染到层上  
            renderTo: 'humidity',
            //设置背景透明
            //backgroundColor: 'rgba(255,255,90,0.7)'  
        },
        //设定报表对象的初始数据  
        series: [{
            data: []
        }],
        title: { text: '<b style="color:red;font-size:1.3em">湿度</b>' },
        subtitle: { text: 'Source: www.karachiwarship.top' },
        credits: { enabled: false },
        xAxis: {
            title:{text: 'Time'},
            categories: ['1:00', '1:05', '1:10', '1:15', '1:20', '1:25',
                '1:30', '1:35', '1:40', '1:45', '1:50', '1:55'
            ]
        },
        exporting: {
            url: 'http://export.hcharts.cn/'
        },
        yAxis: {
            title: {
                text: 'Humidity (%)',
                //color: '#808080'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '%'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },

    });

    function getForm() {
        //使用JQuery从后台获取湿度JSON格式的数据  
        jQuery.getJSON('/get_humidity', null, function(data) {
            //为图表设置值  
            chart.series[0].setData(data);
        });
        jQuery.getJSON('/get_time', null, function(data) {
            //为图表设置值  
            chart.xAxis[0].setCategories(data);
        });

    }


    $(document).ready(function() {
        //每隔3秒自动调用方法，实现图表的实时更新  
        window.setInterval(getForm, 5000);

    });


});