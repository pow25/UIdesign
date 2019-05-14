$(document).ready(function() {
    $("#user_name").text(user_id);
    $("#pb-shape").text(shape_process+"%");
    $("#pb-shape").attr("style","width:"+shape_process+"%");
    $("#pb-letter").text(letter_process+"%");
    $("#pb-letter").attr("style","width:"+letter_process+"%");

    $("#btn_shape").click(function() {
       window.location.href = "/before_shape"; 
    });
    $("#btn_letter").click(function() {
        window.location.href = "/before_letter"; 
    });
    $(function(){
        $(".flip").flip({
            axis: 'y',
            reverse: true,
            trigger: 'manual'
        });
    });
    $( "#btn_shape" ).mouseover(function() {
        $(this).css('cursor', 'pointer');
        // $(".flip").flip(true);
    });
    $( "#btn_shape" ).mouseleave(function(){
        // $(".flip").flip(false);
    });
    $( "#btn_letter" ).mouseover(function() {
        $(this).css('cursor', 'pointer');
        // $.when($("#img_letter").fadeOut(600)).then(function( ) {
        //     $("#img_letter").attr("src", "/static/letters/B.jpg");
        //     $("#img_letter").fadeIn(600);
        // }); 
    });
    $( "#btn_letter" ).mouseleave(function(){
        // $.when($("#img_letter").fadeOut(600)).then(function( ) {
        //     $("#img_letter").attr("src", "/static/letters/A.jpg");
        //     $("#img_letter").fadeIn(600);
        // }); 
    });
});