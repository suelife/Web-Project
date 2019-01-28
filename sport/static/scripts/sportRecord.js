$(document).ready(function () {
  
  var table = $("#dataTable").DataTable({ 
    "ordering" : true, 
    "columnDefs" : [{"targets":4, "type":"date"}], 
    "order": [[ 3, "desc" ]]
   });

  
  // function desc. :控制欄位只能輸入小數點與數字
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('keyup', 'input[name="weight"]', function () {
    $(this).val($(this).val().replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g, ''))
  })


  // function desc. :控制欄位只能輸入數字
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('keyup', 'input[name="duration"]', function () {
    $(this).val($(this).val().replace(/\D/g, ''))
  })


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
    table.draw();
  })


  // function desc. :日期區間-datatable filter
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/10/05
  $.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
      var min = moment($('#datepicker_from').val())
      var max = moment($('#datepicker_to').val())
      var date = moment(data[3])

      if (min && !isNaN(min)) {
        if (date < min) {return false}
      }
      if (max && !isNaN(max)) {
        if (date > max) {return false}
      }
      return true; 
  });


  // function desc. :計算出運動消耗熱量
  //                 運動項目消耗熱量（卡/公斤/小時）＊ 體重 ＊ 分鐘 / 60（分鐘換成小時）
  // parameter : tr (tr object)
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function multiplyCal(tr) {
    var num = ($(tr).find('td[name="unitcal"]').text()
      * $(tr).find('input[name="weight"]').val()
      * $(tr).find('input[name="duration"]').val()
      / 60)

    $(tr).find('input[name="cal"]').val(
      num.toFixed(0))
  }


  // function desc. :row下拉選單-運動項目列表選擇
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('change', 'select[name="sportid"]', function () {
    var tr = $(this).parents('tr')
    $.get("../../api/sportitem/" + $(this).val() + "/", function (data) {
      if (data.cal) {
        $(tr).find('td[name="unitcal"]').text(data.cal)
        multiplyCal(tr)
      }
    })
  })


  // function desc. :row體重變更
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('change', 'input[name="weight"]', function () {
    multiplyCal($(this).parents('tr'))
  })


  // function desc. :row運動時間變更
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('change', 'input[name="duration"]', function () {
    multiplyCal($(this).parents('tr'))
  })


  // function desc. :row點選新增增加一列
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('#add').click(function () {
    $('table > thead').append(trTemplate('new', ''))
  })


  // function desc. :row點選新增確認保存
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table > thead').on('click', '#create', function () {
    var tr = $(this).parents('tr')
    postSR(tr)
  })


  // function desc. :row編輯按鈕點選
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table > tbody').on('click', '#edit', function () {
    var tr = $(this).parents('tr')
    rowhtml = tr.html()
    cols = $(tr).find("td:lt(11)")
    datas = {}
    cols.each(function (idx, col) {
      datas[$(col).attr("name")] = $(col).text()
    });

    tr.html(trTemplate('edit', datas)).find('select[name="sportid"]').val(datas.sportid)
  })


  // function desc. :row編輯後點選確認更新
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table > tbody').on('click', '#check', function () {
    var tr = $(this).parents('tr')
    putSR(tr)
  })

  
  // function desc. :row點選刪除
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('click', '#delete', function () {
    var tr = $(this).parents("tr")

    if (confirm("您是否確認刪除？")) {
      deleteSR(tr)

    }
  })


  // function desc. :row點選取消編輯
  // parameter : 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  $('table').on('click', '#cancel', function () {
    var tr = $(this).parents('tr')
    if ($(tr).attr('name') == 'new')
      $(tr).remove()
    else
      $(tr).removeClass('table-active').html(rowhtml)
  })


  // function desc. :新增ajax
  // parameter : datas
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function postSR(tr) {

    var obj = $(tr).find('.put')
    var dts = $(tr).find('.datas,:selected')
    var datas = {}

    $(obj).each(function () {
      datas[$(this).attr('name')] = $(this).val()
    })

    $.ajax({
      'url': '/api/sportrecord/',
      'type': 'POST',
      'data': datas
    }).done(function (data) {
      $(dts).each(function () { data[$(this).attr('name')] = $(this).text() })

      var row = "<tr>" + trTemplate("normal", data) + "</tr>"
      table.row.add($(row)).draw();
      $(tr).remove()
      alert("新增成功" + data.id)
    })
  }


  // function desc. :table row的模板
  // parameter : type("normal","new","edit"),data
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function trTemplate(type, data) {
    var template = ""

    if (type == "normal") {
      var sdate = $.format.date(data.sdate, "yyyy-MM-dd")
      var mdate = $.format.date(data.mdate, "yyyy-MM-dd HH:mm:ss")
      template =
        `  <td name='id' hidden>${ data.id }</td>
              <td name='sportid' hidden>${ data.sportid }</td>
              <td name='sportname'>${ data.sportname }</td>
              <td name='sdate'>${ sdate }</td>
              <td name='duration'>${ data.duration }</td>
              <td name='weight'>${ data.weight }</td>
              <td name='unitcal' hidden>${ data.unitcal }</td>
              <td name='cal'>${ data.cal}</td>
              <td name='cuser' hidden>${ data.cuser }</td>
              <td name='cusername'>${ data.cusername }</td>
              <td name='mdate'>${ mdate }</td>
              <td><i id = 'edit' class='far fa-edit'></i></i><i id = 'delete' class='far fa-trash-alt' style='color: tomato;'></i></td>`
    }
    else if (type == "new") {
      var option = $("#template #sportid").html()
      var cuser = $("#template #cuser").text()
      var cusername = $("#template #cusername").text()

      template =
        `<tr class = "table-active" name="new">
                <td name='id' hidden ></td>
                <td>
                  <select name='sportid' class="put">
                    ${option}
                  </select>
                </td>
                <td><input name='sdate' type="date" class="put"></td>
                <td><input name='duration' type="text" class="put"></td>
                <td><input name='weight' type="text" class="put"></td>
                <td name='unitcal' hidden class="datas"></td>
                <td><input name='cal' type="text" class="put" readonly></td>
                <td name='cuser' hidden><input name='cuser' type="text" value = "${ cuser }" class="put" hidden></td>
                <td name='cusername' class="datas">${ cusername }</td>
                <td name='mdate'></td>
                <td><i id = "create" class="fas fa-plus-circle" style='color: Dodgerblue;'></i><i id = "cancel" class="fas fa-minus-circle" style='color: gold;'></i></td>
              </tr> `
    }
    else if (type == "edit") {
      option = $("#template #sportid").html()

      template =
        `<td name='id' hidden class="datas">${data.id}</td>
              <td>
                <select name='sportid' value=${data.sportid} class="put">
                  ${option}
                </select>
              </td>
              <td><input name='sdate' value="${ data.sdate}" type="date" class="put"></td>
              <td><input name='duration' value="${ data.duration}" type="text" class="put"></td>
              <td><input name='weight' value="${ data.weight}" type="text" class="put"></td>
              <td name='unitcal' hidden class="datas">${ data.unitcal}</td>
              <td><input name='cal' value="${ data.cal}" type="text" class="put" readonly></td>
              <td name='cuser' hidden>${ data.cuser}</td>
              <td name='cusername' class="datas">${ data.cusername}</td>
              <td name='mdate'>${data.mdate}</td>
              <td><i id = 'check' class='far fa-check-circle' style='color: Dodgerblue;'></i><i id = 'cancel' class='fas fa-minus-circle' style='color: gold;'></i><i id = 'delete' class='far fa-trash-alt' style='color: tomato;'></i></td>`
    }
    return template
  }


  // function desc. :修改ajax
  // parameter : id, datas
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function putSR(tr) {
    var obj = $(tr).find('.put')
    var dts = $(tr).find(".datas,:selected")
    var id = $(dts[0]).text()

    var datas = {}

    $(obj).each(function () { datas[$(this).attr('name')] = $(this).val() })

    $.ajax({
      'url': '/api/sportrecord/' + id + '/',
      'type': 'PUT',
      'data': datas
    }).done(function (data) {
      $(dts).each(function () { data[$(this).attr('name')] = $(this).text() })
      $(tr).html(trTemplate('normal', data)).find('select[name="sportid"]').val(data.sportid)
    })
  }


  // function desc. :刪除ajax
  // parameter : id, datas 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function deleteSR(tr) {
    var id = $(tr).find('td[name = "id"]').text()
    $.ajax({
      'url': '/api/sportrecord/' + id + '/',
      'type': 'DELETE'
    }).done(function (data) {
      alert('刪除成功')
      table.row($(tr)).remove().draw();
    })
  }
  

  // //jQuery Ajax
  // name = $(':text:eq(0)').val()
  // age = $(':text:eq(1)').val()
  // $.get("../../api/sportrecord/",function(datas){
  //   $.each(datas, function(idx, data){
  //     inner =  '<tr><td>' + data.sportid.neme 
  //             +'</td><td>'+ data.weight
  //             +'</td><td>'+ data.cal
  //             +'</td><td>'+ data.duration
  //             +'</td><td>'+ data.cdate
  //             +'</td><tr>'

  //     $('#dataTable tbody').html(inner)
  //   })
  // })



})   