#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

from Question3db import get_posts

app = Flask(__name__)

HTML_WRAP = '''\
<!DOCTYPE html>
<html>
    <head>
        <title>Errors</title>
    </head>
    <body>
    ERRORS GREATER THAN 1 &#137 ON A PARTICULAR DATE<br>
%s
    </body>
</html>
'''
POST = '''\
        %s &nbsp; -&nbsp; %s&nbsp; &#137 &nbsp; error<br>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    posts = "".join(POST % (date, num) for date, num in get_posts())
    html = HTML_WRAP % posts
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
