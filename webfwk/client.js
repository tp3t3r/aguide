// client side

var response = 0;
var previous = 0;


function renderState(response) {
    document.getElementById('debug').innerHtml + response;
    // TODO switch-case
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
        previous = response
    }
}
window.setInterval(pollServer, 1000);
