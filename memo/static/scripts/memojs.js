$(document).ready(function(){
    var blockCon = $('.blockCon')

    // 點擊card標題
    blockCon.on('mousedown','i.fas',function(e){
        $(this).parents('.card').children('.cardCon').slideToggle(500)
        e.stopPropagation();
    })
    
    // 新增按鈕
    $('#createCard').click(function(){
        $('#iF').css('display','block')
        $('#iF').find(':text').focus();

    })

    // 新增取消
    $('#iF').find('#iFcancel').click(function(){
        $('#iF').css('display','none')
    })

    // 修改按鈕
    blockCon.on('mousedown','input[name="update"]',function(e){
        $(this).parents('.cardblock').children('.card').css('display','none')
        $(this).parents('.cardblock').children('.manage').css('display','block')
        e.stopImmediatePropagation();
    })

    // 封存按鈕
    blockCon.on('mousedown','input[name="archive"]',function(e){
        var cb = $(this).parents('.cardblock')
        console.log(cb)
        $.ajax({
            type:'put',
            url:'/api/memorf/'+$(this).attr('id').substring(7,)+'/',
            data:{"memoState":"a"}
        }).done(function(datas){
            cb.remove()                
        });
        e.stopImmediatePropagation();
    })

    // 刪除按鈕
    blockCon.on('mousedown','input[name="delete"]',function(e){
        var con = confirm('是否確認刪除?')
        if (con){
            var cb = $(this).parents('.cardblock')
            $.ajax({
                type:'delete',
                url:'/api/memorf/'+$(this).attr('id').substring(6,)+'/'
            }).done(function(datas){
                cb.remove()                
            });
            e.stopImmediatePropagation();
        }else{e.stopImmediatePropagation();}
    })

    
    // 更新取消按鈕
    blockCon.on('click','input[name="cancel"]',function(e){
        $(this).parents('.cardblock').children('.card').css('display','block')
        $(this).parents('.cardblock').children('.manage').css('display','none')
        e.stopImmediatePropagation();
    })



    // 搜尋
    $('#searchbtn').on('click',function(){
        keyword = $('.searchtext').val()
        if (keyword){
            var search = false
            $('.cardCon').css('display','none')
            $.each($(".card"),function(key,value){
                if($(value).find('.cardTitle').html().search(keyword)>-1||
                    $(value).find('div[name="content"]').html().search(keyword)>-1){
                    $(value).children('.cardCon').css('display','block')
                    search = true
                }
            })
            if (!search){
                alert('搜尋沒有結果')
            }
        }else{
            alert('請輸入關鍵字')
        }    
    })         
})
