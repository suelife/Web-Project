$(document).ready(function () {
    
    // function desc. :編輯狀態時，將所有readonly與disable取消
    // parameter : datas
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/07
    $("#edit").click(function(){
       $("input,#submit").removeAttr("readonly").removeAttr("disabled").removeAttr("hidden")
       $(this).attr("hidden","true")
   })
    
});