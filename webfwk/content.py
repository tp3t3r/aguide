skeleton="""
<html>
<head><script src="client.js"></script></head>
<div id='content'>{content}</div>
<div id='status'></div>
<form action="/fsm" method="POST">
    <input type="text" id="hiddentext" name="hiddenkey">
    <input type="submit" value="{buttontext}">
</form>
</html>
"""
