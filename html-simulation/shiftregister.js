var $ = document.getElementById.bind(document);
var data = 0

function data_clicked() {
    if($("data").style.backgroundColor == "rgb(255, 0, 0)") {
        $("data").style.backgroundColor = "#FFFFFF";
        data = 0
    } else {
        $("data").style.backgroundColor = "#FF0000";
        data = 1
    }
}

function clock_clicked() {
    var i;
    for(i=7; i>0; i--) {
        $("bit"+i+"_s").style.backgroundColor = $("bit"+(i-1)+"_s").style.backgroundColor;
        $("bit"+i+"_s").innerHTML = $("bit"+(i-1)+"_s").innerHTML
    }
    $("bit0_s").style.backgroundColor = $("data").style.backgroundColor;
    $("bit0_s").innerHTML = data
    $("s_sum").innerHTML = "Value: " + sum("s")
}

function latch_clicked() {
    var i;
    for(i=0; i<8; i++) {
        $("bit"+i+"_p").style.backgroundColor = $("bit"+i+"_s").style.backgroundColor;
        $("bit"+i+"_p").innerHTML = $("bit"+i+"_s").innerHTML
    }
    $("p_sum").innerHTML = "Value: " + sum("p")
}

function sum(t) {
    var sum = 0
    for(i=7; i>=0; i--) {
        sum += parseInt($("bit"+i+"_"+t).innerHTML) * Math.pow(2, 7-i)
    }
    return sum
}