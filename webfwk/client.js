function renderState(state) {
    // TODO switch-case
}
function pollServer() {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET","/status",false);
    Httpreq.send(null);
    if (Httpreq.status == 200) {
        var response = Httpreq.responseText;
        //document.getElementById('debug').innerHTML = response;
        if response
    }
}
window.setInterval(pollServer, 1000);
