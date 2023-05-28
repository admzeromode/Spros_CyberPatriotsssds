$(document).ready(function(){
    $('#block2').hide(0);
    $('#block3').hide(0);
    $("#hide_canvas2").hide(0);
    $('#graf2').hide(0);
                 


    $('#btn_nav1').click(function(){
        $("#block2").hide(0);  
        $("#block3").hide(0);          
        $('#block1').fadeIn(0);
        $("#graf1").fadeIn(0);  
        $("#hide_canvas2").hide(0);
        $('#graf2').hide(0);
                 
               

    })
    $('#btn_nav2').click(function(){
        $("#block1").hide(0);  
        $("#block3").hide(0);   
        $("#graf1").hide(0);                                 
        $('#block2').fadeIn(0);
        $('#btn_search2').fadeIn(0);
        $('#hide_canvas2').fadeIn(0);
        $('#graf2').fadeIn(0);


    })
    $('#btn_nav3').click(function(){
        $("#block2").hide(0);  
        $("#block1").hide(0);  
        $("#canvas1").hide(0);                 
        $("#btn_search3").hide(0);                 
        $('#block3').fadeIn(0);
    })
})
