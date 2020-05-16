// client side

var response = 0;
var previous = 0;

function renderState(response) {
    console.log("response: " + response)
}
function refreshEvf() {
    d = new Date();
    now_ts = "?" + d.getTime();
    console.log("now_ts: " + now_ts)
    document.getElementById("evf").src = "evf.png"+now_ts
}
function pollServer() {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET","/status",false);
    Httpreq.send(null);
    if (Httpreq.status == 200) {
        response = Httpreq.responseText;
        //document.getElementById('debug').innerHTML = response;
        console.log("response: " + response)
        if(response > previous) {
            renderState(response);
        }
        refreshEvf()
        previous = response
    }
}

window.setInterval(pollServer, 1000);
