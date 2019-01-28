$(document).ready(function () {

    date = { "s_date": "2000-01-01", "e_date": "9999-12-31" }


    // function desc. :自動產生顏色
    // parameter : 
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/10
    function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }


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
        if ($(this).val()) { date[$(this).attr("id")] = $(this).val() }
        else {
            if ($(this).attr("id") == "s_date")
                date["s_date"] = "2000-01-01"
            else if ($(this).attr("id") == "e_date")
                date["e_date"] = "9999-12-31"
        }
        getChartData();
    })


    // function desc. :初始化運動時間區間查詢的日期選擇器並建立事件
    // parameter : 
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/05
    function getChartData() {
        var clabels = [];
        var ccount = [];
        var csum = []
        var colors = [];

        $.getJSON(`../chartdata/${date.s_date}/${date.e_date}/`, function (datas) {
            // datas = $.parseJSON(datas)
            $.each(datas, function (idx, data) {
                clabels.push(data["sportid__name"])
                ccount.push(data["dcount"])
                csum.push(data["dsum"])

                colors.push(getRandomColor())

            })
            console.log(clabels)
            // Set new default font family and font color to mimic Bootstrap's default styling
            // Set new default font family and font color to mimic Bootstrap's default styling
            Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
            Chart.defaults.global.defaultFontColor = '#292b2c';
            
            // Bar Chart 
            new Chart($("#myBarChart"), {
                type: 'bar',
                data: {
                    scaleStartValue: 0,
                    labels: clabels,
                    datasets: [
                        {
                            backgroundColor: colors,
                            data: ccount
                        }
                    ]
                },
                options: {
                    legend: { display: false },

                    scales: {
                        xAxes: [{

                            display: true,
                            ticks: {
                                fontSize: 8
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                stepSize: 1

                            },
                        }],


                    },
                    hover: { mode: 'single' },

                },
            });


            // Pie Chart 
            new Chart($("#myPieChart"), {
                type: 'doughnut',
                data: {
                    labels: clabels,
                    datasets: [{
                        backgroundColor: colors,
                        data: csum,
                    }],
                },

            })
        });




    }
    getChartData();


})



