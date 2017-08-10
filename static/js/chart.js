$(function() {
    //声明报表对象  
    var chart = new Highcharts.Chart({

        chart: {
            //将报表对象渲染到层上  
            renderTo: 'xchart',
            //设置背景透明
            //backgroundColor: 'rgba(255,255,90,0.7)'  
        },
        //设定报表对象的初始数据  
        series: [{
            data: [29.9, 31.2, 32.2, 33.5, 34.6, 33.4, 32.1, 31.3, 30.9, 30.8, 29.6, 28.1]
        }],
        title: { text: '<b style="color:red;font-size:1.3em">温湿度</b>' },
        subtitle: { text: 'Source: www.karachiwarship.top' },
        credits: { enabled: false },
        xAxis: {
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
        jQuery.getJSON('./cgi-bin/get_temp_humi.py', null, function(data) {
            //为图表设置值  
            chart.series[0].setData(data);
        });
        //使用JQuery从后台获取时间JSON格式的数据
        jQuery.getJSON('./cgi-bin/get_temp_humi.py', null, function(categories) {
            //为图表设置值  
            chart.categories[0].setData(categories);
        });

    }


    $(document).ready(function() {
        //每隔3秒自动调用方法，实现图表的实时更新  
        window.setInterval(getForm, 3000);

    });


});