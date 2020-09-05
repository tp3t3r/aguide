// client side

var response = "";
var previous = "";

var evf_pic = "evf.png"

function changeState(response) {
    if ( response == "WAIT-FOR-CAM" ) {
        document.getElementById('button_text').value = '(setting up)'
        document.getElementById('button_text').disabled = true;
        return
    }
    if ( response == "FREE-RUN" ) {
        document.getElementById('button_text').value = 'Lock'
        document.getElementById('button_text').disabled = false
        return;
    }
    if ( response == "LOCKED" ) {
        document.getElementById('button_text').value = 'Start tracking'
        document.getElementById('button_text').disabled = false;
        return
    }
    if ( response == "TRACKING" ) {
        document.getElementById('button_text').value = 'Stop'
        document.getElementById('button_text').disabled = false;
        return
    }
    console.log("response: " + response)
}
function refreshEvf() {
    d = new Date();
    now_ts = "?" + d.getTime();
    //console.log("now_ts: " + now_ts)
    document.getElementById("evf").src = evf_pic + now_ts
}
function pollServer() {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET","/state",false);
    Httpreq.send(null);
    if (Httpreq.status == 200) {
        response = Httpreq.responseText;
        console.log("response: " + response)
        //document.getElementById('debug').innerHTML = response;
        if(response != previous) {
            changeState(response);
        }
        refreshEvf()
        previous = response
    }
}

window.setInterval(pollServer, 3000);
