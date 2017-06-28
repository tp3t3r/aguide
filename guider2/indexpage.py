
class IndexPage():
    def __init__(self, status, imagefile, button, output='index.html'):
        self.template="""
            <html>
                <title>sg9k</title>
                <head>
                    <link rel='stylesheet' href='style.css'>
                    <script type='text/javascript'>
                        function reloadImage() {
                            reloadImage.counter = 0;
                            var d = new Date();
                            document.getElementById('evf').src = '%s?at=' + d.getTime();
                        }
                        window.setInterval(reloadImage, 900);
                    </script>
                    <meta http-equiv="cache-control" content="max-age=0" />
                    <meta http-equiv="cache-control" content="no-cache" />
                    <meta http-equiv="expires" content="0" />
                    <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
                    <meta http-equiv="pragma" content="no-cache" />
                </head>
                <body>
                    <!--div class='title'>guide camera:</div-->
                    <img width='640' height='480' id='evf' src='%s'></img>
                    <div>%s</div>
                    <div class='button-container'>
                        <form action='index.html#' method='get'>
                            <input type='submit' value='%s' name'%s'>
                        </form>
                    </div>
                </body>
            </html>
        """ % (imagefile,imagefile,status,button,button)

        with open(output, 'w') as fd:
            fd.write(self.template)
 
