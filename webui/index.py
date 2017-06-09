#main page

import cgi
buttons = cgi.FieldStorage()

configValues = {
    "thold" : 100
}

print """
<html>
    <title>Autoguider</title>
    <head>
        <script type='text/javascript'>
            function reloadImage() {
                reloadImage.counter = 0;
                var d = new Date();
                document.getElementById('evf').src = 'evf.jpg?at=' + d.getTime();
            }
            window.setInterval(reloadImage, 1500);
        </script>
    </head>
    <body>
        <h1>image:</h1>
        <img width='640' height='480' id='evf' src='evf.jpg'></img>
        <form action='index.py' method="post">"""

def handle_plus_minus(buttonname):
    if buttons[buttonname]:
        configValues['thold'] = buttons[buttonname]
handle_plus_minus('THP')
print "<button name='THP' value='%d'>inc. threshold</button>" % (thold + 2)
handle_plus_minus('THM')
print "<button name='THM' value='%d'>dec. threshold</button>" % (thold - 2)
print """
        </form>
    </body>
</html>
"""

print form.keys()
