function makeNames() {
    $("#names").empty();
    $("#names2").empty();
    var name = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    $.each(name,function(index,value){
        var id = "#"+value;
        var new_row = "<img id='"+value+"' src='/static/letters/"+value+".jpg' width='70' height='70'>";
        if ( index < 13 ){
            $("#names").append(new_row);
        }
        else{
            $("#names2").append(new_row);
        }
        $(id).draggable({
            zIndex: 2500,
            cursor:"move",
            revert: function(){
                $(this).removeClass('border_light');
                return true;
            },
            drag: function(e, i) {
                if (!$(this).hasClass('border_light')) {
                    $(this).addClass('border_light');
                }
            }
        });
        $(id).hover(
            function() {
                $(this).addClass('border_light');
                $(this).css('cursor', 'move' );
            }, 
            function() {
                $(this).removeClass('border_light');
            }
        );
    });
}

$(document).ready(function() {
    makeNames();
    var rnd_gif = Math.floor(Math.random() * 3) + 1;
    var filename_gif;
    if (level=="1"){
        filename_gif = "one"+rnd_gif;
    }
    else if( level=="2" ){
        filename_gif = "two" + rnd_gif;
    }
    else{
        filename_gif = "three" + rnd_gif;
    }
    answer = answer[filename_gif];
    var user_answer=[];
    $(".answer").droppable({

        drop:function (event,ui) {
            //get dropped name
            var drop_name = $(ui.draggable).attr('id');
            user_answer.push(drop_name);
            $("#"+drop_name).remove();
            var new_row2 = "<span class='answer_letter'>"+drop_name+"</span>";
            $(".answer").append(new_row2);
        }
    });

    
    $("#gif").css('cursor', 'pointer' );
    $("#gif").one("click",function () {
        $("#gif").attr("src","/static/gifs/"+filename_gif+".gif");
        $("#gif").css('cursor', 'default' );
        $("#instruction").text("want some hints?");
        $("#instruction").css('cursor','pointer');
        $("#instruction").one("click",function () {
            $("#instruction").css('cursor','default');
            $("#instruction").css('font-weight','light');
            $("#instruction").css('color','gray');
            $("#instruction").css('font-size','22px');
            $("#instruction").css('padding-top','17px');
            $("#instruction").css('padding-bottom','20px');
            var hint_txt = "The first letter is:"+answer[0]+"||The last letter is:"+answer[answer.length - 1];
            $("#instruction").text(hint_txt);
        });
    });

    $("#btn_clear").click(function () {
        makeNames();
        $(".answer").empty();
        user_answer=[];
    });
    $("#btn_submit").click(function () {
        var score = 0;
        var max_i = Math.min(user_answer.length,answer.length);
        for(var i = 0; i < max_i; ++i){
            if ( user_answer[i] == answer[i] ){
                score += 1;
            }
        }
        
    });
});