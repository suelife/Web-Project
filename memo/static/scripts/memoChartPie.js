$(document).ready(function () {
   
    date = { "s_date": "2000-01-01", "e_date": "9999-12-31" }
        
    // function desc. :初始化運動時間區間查詢的日期選擇器並建立事件
    // parameter : 
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/05
    $(".date").datepicker({
        showOn: "button",
        buttonImage: "/static/images/calender.png",
        buttonImageOnly: true,
        dateFormat: "yy-mm-dd",

    }).change(function () {
        if($(this).val()){date[$(this).attr("id")] = $(this).val()}
        else{
            if($(this).attr("id") == "s_date")
                date["s_date"]= "2000-01-01"
            else if($(this).attr("id") == "e_date")  
                date["e_date"]= "9999-12-31"
        }
        $("#myPieChart").remove();
        getChartData();
    })


    // function desc. :初始化運動時間區間查詢的日期選擇器並建立事件
    // parameter : 
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/05
    function getChartData() {
        var clabels = ['待辦事項','完成','封存','過期'];
        var cdata = [];
        var colors = [];

        $.get(`../chartdata/${date.s_date}/${date.e_date}/`, function (datas) {
            
            cdata = $.parseJSON(datas)

        colors =['#4efeb3','#97cbff','#eac100',' #ff5809']
        $("#Pie").append('<canvas id="myPieChart" height="275"></canvas>')
        // Set new default font family and font color to mimic Bootstrap's default styling
        // Set new default font family and font color to mimic Bootstrap's default styling
        Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
        Chart.defaults.global.defaultFontColor = '#292b2c';
    
        // Pie Chart Example
        var ctx = $("#myPieChart");
        var myPieChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: clabels,
                datasets: [{
                    data: cdata,
                    backgroundColor: colors
                }],
            },
        });
    })
    
        
    }
    getChartData();
    

})

   

