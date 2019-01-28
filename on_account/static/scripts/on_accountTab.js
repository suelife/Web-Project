$(document).ready(function () {
    checkmoney = false
    userid = ""
    
    // 抓取userid
    $.get("/on_account/catch/", function (data) {
        userid = data
    })
    
    loadTodo()
    setcreatedialog()
    setupdatedialog()

    // 刪除資料
    $('#myDataTalbe').on('click', 'button:nth-child(2)', function () {
        var id = $(this).parents('tr').find('td:nth-child(1)').attr("id")
        var r = confirm("確定要刪除嗎??")
        if (r == true) {
            $.ajax({
                'url': '/api/on_accountapi/' + id + '/',
                'type': 'DELETE',
                success: function (data) {
                    alert('刪除成功!!');
                }
            }).done(function (data) {
                loadTodo()
            })
        }
    })

    // 修改資料
    $('#myDataTalbe').on('click', 'button:nth-child(1)', function () {
        tbid = $(this).parents('tr').find('td:nth-child(1)').attr("id")
        var tbIOtype = $(this).parents('tr').find('td:nth-child(2)').attr("id")
        var moneyre = /\d+/
        var tbmoney = $(this).parents('tr').find('td:nth-child(2)').text()
        var tbmoneyre = tbmoney.match(moneyre)
        var tbspendtype = $(this).parents('tr').find('td:nth-child(3)').text()
        var tbremark = $(this).parents('tr').find('td:nth-child(4)').text()

        var IOtype = $("#IOtypeup")          // 取得該tag
        var money = $("#moneyup")            // 取得該tag
        var spendtype = $("#spendtypeup")    // 取得該tag
        var remark = $("#remarkup")          // 取得該tag
        IOtype.val(tbIOtype)
        money.val(parseInt(tbmoneyre[0]))
        spendtype.val(tbspendtype)
        remark.val(tbremark)
        $("#dialog-form-update").dialog("open");
    })

    // 新增資料
    function create() {
        console.log(`userid: ${userid}`)
        var IOtype = $("#IOtype")          // 取得該tag
        var money = $("#money")            // 取得該tag
        var spendtype = $("#spendtype")    // 取得該tag
        var remark = $("#remark")          // 取得該tag
        var datas = {
            "IOtype": IOtype.val(),
            "money": parseInt(money.val()),
            "spendtype": spendtype.val(),
            "remark": remark.val(),
            "userid": userid
        };
        var r = confirm("確定要新增嗎??")
        if (r == true) {
            $.post('/api/on_accountapi/', datas, function (data) {
                loadTodo()
            })
        }
    }

    // 修改資料
    function update() {
        console.log(tbid)
        var IOtype = $("#IOtypeup")          // 取得該tag
        var money = $("#moneyup")            // 取得該tag
        var spendtype = $("#spendtypeup")    // 取得該tag
        var remark = $("#remarkup")          // 取得該tag
        var datas = {
            "IOtype": IOtype.val(),
            "money": parseInt(money.val()),
            "spendtype": spendtype.val(),
            "remark": remark.val()
        };
        var r = confirm("確定要修改嗎??")
        if (r == true) {
            $.ajax({
                'url': '/api/on_accountapi/' + tbid + '/',
                'type': 'PUT',
                'data': datas,
                success: function (data) {
                    alert('修改成功!!');
                }
            }).done(function (data) {
                loadTodo()
            })
        }
    }

    // 讀取所有資料
    function loadTodo() {
        $.getJSON('/api/on_accountapi/', function (datas) {
            // settable
            var table = $("#myDataTalbe").DataTable({
                retrieve: true,
                searching: true, //關閉filter功能
                columnDefs: [{
                    targets: [4],
                    orderable: false,
                }],
                "order": [[0, "desc"]],   //控制列排序方式(第一列降序排列)
                // stateDuration: true,
                "pagingType": "full_numbers",

                // 中文化界面顯示
                language: {
                    "sProcessing": "處理中...",
                    "sLengthMenu": "顯示 _MENU_ 項結果",
                    "sZeroRecords": "沒有匹配結果",
                    "sInfo": "顯示第 _START_ 至 _END_ 項結果，共 _TOTAL_ 項",
                    "sInfoEmpty": "顯示第 0 至 0 項結果，共 0 項",
                    "sInfoFiltered": "(由 _MAX_ 項結果過濾)",
                    "sInfoPostFix": "",
                    "sSearch": "搜索:",
                    "sUrl": "",
                    "sEmptyTable": "表中數據為空",
                    "sLoadingRecords": "載入中...",
                    "oPaginate": {
                        "sFirst": "首頁",
                        "sPrevious": "上一頁",
                        "sNext": "下一頁",
                        "sLast": "末頁"
                    },
                }
            });
            table.rows().remove()
            var tb = $('#myDataTalbe');
            var docFrag = $(document.createDocumentFragment())
            $.each(datas, function (idx, on_account) {
                if (userid == on_account.userid) {
                    var retime = /\d{2}:\d{2}:\d{2}/
                    var time = on_account.date
                    var timere = time.match(retime);
                    var redate = /\d{4}-\d{2}-\d{2}/
                    var date = on_account.date
                    var datere = date.match(redate);
                    console.log(`userid: ${userid}`)
                    console.log(`on_account: ${on_account.userid}`)
                    var cell1 = $('<td id=' + on_account.id + '></td>').text(datere[0] + " " + timere[0])
                    if (on_account.IOtype == "outlay") {
                        var cell2 = $('<td id=' + on_account.IOtype + '></td>').text("-" + on_account.money)
                    }
                    else {
                        var cell2 = $('<td></td>').text(on_account.money)
                    }
                    var cell3 = $('<td></td>').text(on_account.spendtype)
                    var cell4 = $('<td></td>').text(on_account.remark)
                    var cell5 = $('<td></td>').html('<button class="btn btn-primary"><i class="fas fa-user-edit"></i></button><button class="btn btn-danger"><i class="far fa-trash-alt"></i></button>')
                    for (var i = 0, max = datas.length; i < max; i++) {
                        if (i / 2 == 0) {
                            var row = $('<tr></tr>').append([cell1, cell2, cell3, cell4, cell5])
                        }
                        else {
                            var row = $('<tr></tr>').append([cell1, cell2, cell3, cell4, cell5])
                        }
                    }
                    table.row.add(row).draw()
                }
            })
        })
    }

    // 設定dialog
    function setcreatedialog() {
        $(function () {
            var dialog
            var IOtype = $("#IOtype")          // 取得該tag
            var money = $("#money")            // 取得該tag
            var spendtype = $("#spendtype")    // 取得該tag
            var remark = $("#remark")          // 取得該tag

            dialog = $("#dialog-form").dialog({
                autoOpen: false,
                closeOnEscape: false,
                height: 590,
                width: 385,
                dialogClass: "no-close",
                resizable: false,         // 調整dialog大小
                modal: true,              // 僅能操作dialog介面
                buttons: {
                    "確定": function () {
                        console.log(`收支類型: ${IOtype.val()}`)
                        console.log(`金額: ${money.val()}`)
                        console.log(`消費類型: ${spendtype.val()}`)
                        console.log(`備註: ${remark.val()}`)
                        if (checkmoney) {
                            create()
                            alert('新增成功!!');
                            checkmoney = false
                            $(this).dialog("close");
                            setval()
                        }
                        else {
                            alert("請輸入金額")
                        }
                    },
                    "取消": function () {
                        $(this).dialog("close");
                        setval()
                    }
                }
            });

            $("#buttonSubmit").click(function () {
                $("#dialog-form").dialog("open");
            });
        });
    }

    function setupdatedialog() {
        $(function () {
            var dialog
            var IOtype = $("#IOtypeup")          // 取得該tag
            var money = $("#moneyup")            // 取得該tag
            var spendtype = $("#spendtypeup")    // 取得該tag
            var remark = $("#remarkup")          // 取得該tag

            dialog = $("#dialog-form-update").dialog({
                autoOpen: false,
                closeOnEscape: false,
                height: 590,
                width: 385,
                dialogClass: "no-close",
                resizable: false,         // 調整dialog大小
                modal: true,              // 僅能操作dialog介面
                buttons: {
                    "確定": function () {
                        console.log(tbid)
                        console.log(`收支類型: ${IOtype.val()}`)
                        console.log(`金額: ${money.val()}`)
                        console.log(`消費類型: ${spendtype.val()}`)
                        console.log(`備註: ${remark.val()}`)
                        if (checkmoney) {
                            update()
                            checkmoney = false
                            $(this).dialog("close");
                        }
                        else if (money.val()) {
                            update()
                            checkmoney = false
                            $(this).dialog("close");
                        }
                        else {
                            alert("請輸入金額")
                        }
                    },
                    "取消": function () {
                        $(this).dialog("close");
                    }
                }
            });
        });
    }

    // 檢查是否輸入金額create
    $("#money").focusout(function () {
        var money = $("#money")
        if (money.val() != "") {
            if (isNaN(money.val())) {
                $("#showerror").html("<i class='fas fa-exclamation-triangle'></i>必須輸入數字")
            }
            else {
                checkmoney = true
                $("#showerror").text(" ")
            }
        }
        else {
            $("#showerror").html("<i class='fas fa-exclamation-triangle'></i>請輸入金額")
        }
    })

    // 檢查是否輸入金額update
    $("#moneyup").focusout(function () {
        var money = $("#moneyup")
        if (money.val() != "") {
            if (isNaN(money.val())) {
                $("#showerrorup").html("<i class='fas fa-exclamation-triangle'></i>必須輸入數字")
            }
            else {
                checkmoney = true
                $("#showerrorup").text(" ")
            }
        }
        else {
            $("#showerrorup").html("<i class='fas fa-exclamation-triangle'></i>請輸入金額")
        }
    })

    // 依照收支類型變換消費類型選項(create)
    $("#IOtype").change(function () {
        // 避免重複選擇
        var sel = $(this).val()
        if (sel == "income") {
            $("#spendtype").children().remove()
            $("#spendtype").append("<option value=''>無</option>")
        }
        else {
            $("#spendtype").children().remove()
            $("#spendtype").append("<option value='食'>食</option><option value='衣'>衣</option><option value='住'>住</option><option value='行'>行</option><option value='育'>育</option><option value='樂'>樂</option><option value='其他'>其他</option>")
        }
    })

    // 依照收支類型變換消費類型選項(update)
    $("#IOtypeup").change(function () {
        // 避免重複選擇
        var sel = $(this).val()
        if (sel == "income") {
            $("#spendtypeup").children().remove()
            $("#spendtypeup").append("<option value=''>無</option>")
        }
        else {
            $("#spendtypeup").children().remove()
            $("#spendtypeup").append("<option value='食'>食</option><option value='衣'>衣</option><option value='住'>住</option><option value='行'>行</option><option value='育'>育</option><option value='樂'>樂</option><option value='其他'>其他</option>")
        }
    })

    // 重設各項value
    function setval() {
        var IOtype = $("#IOtype")          // 取得該tag
        var money = $("#money")            // 取得該tag
        var spendtype = $("#spendtype")    // 取得該tag
        var remark = $("#remark")          // 取得該tag

        IOtype.get(0).selectedIndex = 0
        money.val("")
        $("#spendtype").children().remove()
        $("#spendtype").append("<option value='食'>食</option><option value='衣'>衣</option><option value='住'>住</option><option value='行'>行</option><option value='育'>育</option><option value='樂'>樂</option><option value='其他'>其他</option>")
        spendtype.get(0).selectedIndex = 0
        remark.val("")
    }
})

