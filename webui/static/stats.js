
function Get(url){
    var Httpreq = new XMLHttpRequest();
    Httpreq.open('GET',url,false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}

function updateStatistics() {
    var d = new Date();
    var json_obj = JSON.parse(Get('stats.json?at=' + + d.getTime()));
    //{"frames": 2, "name": "siriusguider 9000", "fps": 0.12826401414055663
    document.getElementById('stats').innerHTML = "fps: " + json_obj.fps 
}

window.setInterval(updateStatistics, 1000);
