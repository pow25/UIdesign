$(document).ready(function() {
    $("#user_name").text(user_id);
    $("#pb-shape").text(shape_process+"%");
    $("#pb-shape").attr("style","width:"+shape_process+"%");
    $("#pb-letter").text(letter_process+"%");
    $("#pb-letter").attr("style","width:"+letter_process+"%");
    $("#btn_shape").click(function() {
       window.location.href = "/before_shape"; 
    });
});