// client side

var response = "";
var previous = "";

var evf_pic = "evf.png"

function changeState(response) {
    console.log("response: " + response)
}
function refreshEvf() {
    d = new Date();
    now_ts = "?" + d.getTime();
    console.log("now_ts: " + now_ts)
    document.getElementById("evf").src = evf_pic + now_ts
}
function pollServer() {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET","/state",false);
    Httpreq.send(null);
    if (Httpreq.status == 200) {
        response = Httpreq.responseText;
        //document.getElementById('debug').innerHTML = response;
        if(response != previous) {
            changeState(response);
        }
        refreshEvf()
        previous = response
    }
}

window.setInterval(pollServer, 3000);
