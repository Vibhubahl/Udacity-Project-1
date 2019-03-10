#!/usr/bin/env python+
from flask import Flask, request, redirect, url_for

from Question2db import get_posts

app = Flask(__name__)

HTML_WRAP = '''\
<!DOCTYPE html>
<html>
    <head>
        <title>POPULAR AUTHORS</title>
    </head>
    <body>
    MOST POPULAR AUTHORS <br>
%s
    </body>
</html>
'''
POST = '''\
        %s &nbsp; -&nbsp; %s&nbsp; views<br>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    posts = "".join(POST % (name, num) for name, num in get_posts())
    html = HTML_WRAP % posts
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
