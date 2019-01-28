$(document).ready(function () {
    //確認email是否正確參數
    chkEmail = 0;
    //確認密碼是否正確參數
    chkPassword = 0;
    //初始化密碼比較值
    psw=""
    cpw=""
    //如為編輯頁面，則password會有初始值
    editpw = $('input[name="password"]').val
    if(editpw){
        psw=editpw
        cpw=editpw
        chkPassword = 1;
    }


    // function desc. :確認email是否重複
    // parameter : datas
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/07
    $('#email').change(function () {
        var email = $(this).val()
        if(email){
            $.get("../check/" + email, function (data) {
                if (data==1)
                {
                    chkEmail = 0
                    $('#emailmsg').html('此email已被註冊，請重新輸入')
                }
                else
                {
                    chkEmail = 1
                    $('#emailmsg').html('')
                }
                    
            })
        }
        else
        {
            chkEmail = 0
            $('#emailmsg').html('請輸入email')
        }
    })
    

    // function desc. :確認密碼是否一致
    // parameter : datas
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/07   
    $('input[type="password"]').change(function () {
        var pw=$(this).val()

        if($(this).attr("name") == "password" )
            psw = pw
        else
            cpw = pw
        
        console.log(psw+","+cpw)
        
        if(psw && cpw && psw != cpw)
        {
            console.log("A")
            $('#pswmsg').html('密碼不一致，請重新輸入')
            chkPassword = 0;
        }
        else if(psw && cpw && psw == cpw)
        {
            $('#pswmsg').html('')
            chkPassword = 1;
        }
        else
        {
            $('#pswmsg').html('請輸入密碼與再次確認密碼')
        }
        
    })


    // function desc. :送出前確認相關資訊是否輸入完全
    // parameter : datas
    // create user : Luffy Lin
    // modify user : Luffy Lin
    // modify date : 2018/10/07   
    $("#submit").submit(function(){
        var name = $('input[name="name"]').val();
        var birthday = $('input[name="birthday"]').val();
        var gender = $('input:radio[name="gender"]:checked').val();
        
        if(chkEmail){
            alert('請輸入email')
            return false;
        }else if(name){
            alert('請輸入姓名')
            return false;
        }else if(birthday){
            alert('請輸入生日')
            return false;
        }else if(gender){
            alert('請選擇性別')
            return false;
        }else if(chkPassword){
            alert('請輸入密碼')
            return false;
        }
        else{
            return true;
        }
    })
    
    
})