function pollServer() {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET",'status',false);
    Httpreq.send(null);
    if (Httpreq.status == 200) {
        var response = Httpreq.responseText;
        // document.getElementById('status').innerHTML = response + "\\n";
    }
}
window.setInterval(pollServer, 2000);
