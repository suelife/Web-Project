$(document).ready(function(){
  var table =  $("#dataTable").DataTable();
  
  // function desc. :爬蟲更新政府資料交易平台運動資料
  // parameter : id, datas
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/10/2
  $('#update').click(function(){
    $.get("itemscraping/",function(data){
      if(data == 1)
      {
        querySI()
        alert('更新成功')
      }
      else
        alert('更新失敗')
    })
  })


  // function desc. :新增ajax
  // parameter : datas
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function postSI(datas, tr){
    if(table)
      console.log(table)
    $.ajax({
        'url':'/api/sportitem/',
        'type':'POST',
        'data':datas
      }).done(function(data){
          
    alert("新增成功"+data.id)      
  })}
  

  // function desc. :修改ajax
  // parameter : id, datas
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function putSI(tr){
    var obj = $(tr).find('input.datas, select.datas')
    var id = $(tr).find('input[name = "id"]').val()
    var datas = {}
    $(obj).each(function()
    {
      datas[$(this).attr('name')] = $(this).val()
    })
        
    $.ajax({
      'url':'/api/sportitem/'+id+'/',
      'type':'PUT',
      'data':datas
    }).done(function(data){
        alert("修改成功"+data.id)
    })
  }
  

  // function desc. :刪除ajax
  // parameter : id, datas 
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function deleteSI(tr){
    var id = $(tr).find('input[name = "id"]').val()
    $.ajax({
      'url':'/api/sportitem/'+id+'/',
      'type':'DELETE'
    }).done(function(data){
      alert('刪除成功')
  })}
     
  
  // function desc. :查詢ajax
  // parameter : id, datas
  // create user : Luffy Lin
  // modify user : Luffy Lin
  // modify date : 2018/09/21
  function querySI(){
    $.get("../../api/sportitem/",function(datas){
      var docFlag = $(document.createDocumentFragment())
      
      $.each(datas, function(idx, data){
        mdate = $.format.date(data.mdate, "yyyy-MM-dd HH:mm:ss")
        docFlag.append($('<tr></tr>')
               .append([$('<td></td>').text(data.name),
                        $('<td></td>').text(data.cal),
                        $('<td></td>').text(mdate)]))
      })
          
      $("#dataTable tbody").html(docFlag)
      })
  }


})