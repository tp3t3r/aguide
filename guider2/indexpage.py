class ConfigPage():
    def __init__(self, thold, sspeed, output='config.html'):
        self.template="""
        <html>
            <head>
                    <meta http-equiv="cache-control" content="max-age=0" />
                    <meta http-equiv="cache-control" content="no-cache" />
                    <meta http-equiv="expires" content="0" />
                    <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
                    <meta http-equiv="pragma" content="no-cache" />
            </head>
            <form action='index.html' method='get'>
                threshold: <input type='text' name='threshold' value='%d'><input type='submit' value='set'>
            </form>
            <form action='index.html' method='get'>
                shutter speed: <input type='text' name='shutterspeed' value='%d'><input type='submit' value='set'>
            </form>
        </html>
        """ % (thold, sspeed)
        with open(output, 'w') as fd:
            fd.write(self.template)
 
class IndexPage():
    def __init__(self, status, imagefile, button, refresh=1200, output='index.html'):
        self.template="""
            <html>
                <title>bg9k</title>
                <head>
                    <link rel='stylesheet' href='style.css'>
                    <script type='text/javascript'>
                        function reloadImage() {
                            reloadImage.counter = 0;
                            var d = new Date();
                            document.getElementById('evf').src = '%s?at=' + d.getTime();
                        }
                        window.setInterval(reloadImage, %d);
                        function getData() {
                            var Httpreq = new XMLHttpRequest();
                            Httpreq.open("GET",'infolog.dat',false);
                            Httpreq.send(null);
                            if (Httpreq.status == 200) {
                                var response = Httpreq.responseText;
                                document.getElementById('infolog').innerHTML = response + "\\n";
                            }
                        }
                        window.setInterval(getData, %d);
                    </script>
                    <meta http-equiv="cache-control" content="max-age=0" />
                    <meta http-equiv="cache-control" content="no-cache" />
                    <meta http-equiv="expires" content="0" />
                    <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
                    <meta http-equiv="pragma" content="no-cache" />
                </head>
                <body>
                    <!--div class='title'>guide camera:</div-->
                    <div class='top_container'>
                        <img src='bguider9k.png'</img><br>
                        <a href='index.html#'><img width='720' height='540' id='evf' src='%s'></img></a><br>
                        <textarea id='infolog' class='infolog' disabled></textarea>
                        <div class='button-container'>
                            <form action='index.html#' method='get'>
                                <input type='hidden' name='current_state' value='%s'>
                                <input class='button' type='submit' value='%s'>
                            </form>
                        </div>
                    </div>
                    <hr>
                    <div class='config'><a href='config.html'>settings</div>
                </body>
            </html>
        """ % (imagefile,refresh,refresh,imagefile,status,button)

        with open(output, 'w') as fd:
            fd.write(self.template)
 
