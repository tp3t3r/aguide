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
                    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
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
    def __init__(self, status, stream, button, refresh=1200, output='index.html'):
        self.template="""
            <html>
                <title>bg9k</title>
                <head>
                    <link rel='stylesheet' href='style.css'>
                    <script type='text/javascript'>
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
                    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"> 
                    <meta http-equiv="cache-control" content="max-age=0" />
                    <meta http-equiv="cache-control" content="no-cache" />
                    <meta http-equiv="expires" content="0" />
                    <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
                    <meta http-equiv="pragma" content="no-cache" />
                </head>
                <body>
                    <div class='title'>buksiguider9000</div>
                    <div class='top_container'>
                        <a href='index.html#'><img style='width:100%%' id='evf' src='%s'></img></a><br>
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
        """ % (refresh,stream,status,button)

        with open(output, 'w') as fd:
            fd.write(self.template)
 
