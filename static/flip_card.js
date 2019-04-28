function progress(timeleft, timetotal, $element) {
    var progressBarWidth = timeleft * $element.width() / timetotal;
    $element.find('div').animate({ width: progressBarWidth }, 500).html(Math.floor(timeleft/60) + ":"+ timeleft%60);
    if(timeleft > 0) {
        setTimeout(function() {
            progress(timeleft - 1, timetotal, $element);
        }, 1000);
    }
    else{
        window.location.href="/after_shape/"+ parseInt(16-item_count, 10);
    }
};
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
  
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
  
      // And swap it with the current element.
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
  
    return array;
};

function random_select_img(file_list) {
    var arr = Array(16).fill().map((x,i)=>i+1);
    arr = shuffle(arr);
    for(var i = 0; i < 8; ++i){
        var cur_file = file_list[Math.floor(Math.random() * 10)];
        cur_file = "/static/shape/" + cur_file;
        $("#img"+arr[i].toString()).find(".back img").attr("src",cur_file);
        $("#img"+arr[i+8].toString()).find(".back img").attr("src",cur_file);
    }
}
var file_list = ["3d.png","asterisk.png","black-cloud.png",
                 "check-box-empty.png","letter-x.png",
                 "moon-phase-outline.png","plus-symbol.png",
                "star.png","tick.png","remove.png","heart.png"];

var previous_click_id = "";
var item_count = 16;

$(document).ready(function() {
    progress(time_game, time_game, $('#progressBar'));
    random_select_img(file_list);

    $(function(){
        $(".flip").flip({
            trigger: 'manual'
        });
    });

    $(".flip" ).click(function() {
        $(this).flip(true);
        var cur_click_id = $(this).attr('id');
        if (previous_click_id) {
            var prev_addr = $("#"+previous_click_id).find(".back img").attr('src');
            var cur_addr = $("#"+cur_click_id).find(".back img").attr('src');
            if (cur_addr == prev_addr && cur_click_id!=previous_click_id){
                setTimeout(function(){
                    $("#"+previous_click_id).remove();
                    $("#"+cur_click_id).remove();                
                    previous_click_id = "";
                    item_count -= 2;
                    if (item_count == 0){
                        window.location.href="/after_shape/16";
                    }
                }, 300);
            
            }
            else{
                setTimeout(function(){
                    $("#"+previous_click_id).effect( "shake" );
                    $("#"+cur_click_id).effect("shake");
                    $("#"+previous_click_id).flip(false);
                    $("#"+cur_click_id).flip(false);
                    previous_click_id = "";
                }, 300);

            }
        }
        else{
            previous_click_id = cur_click_id;
        }
    });
});