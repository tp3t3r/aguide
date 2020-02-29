client_side_script="""
function getData() {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET",'status',false);
    Httpreq.send(null);
    if (Httpreq.status == 200) {
        var response = Httpreq.responseText;
        document.getElementById('status').innerHTML = response + "\\n";
    }
}
window.setInterval(getData, 2000);
"""

skeleton="""
<html>
<head><script>%s</script></head>
<p>contents comes here</p>
<div id='status'></div>
</html>
""" % client_side_script
