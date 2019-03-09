#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

from Question3db import get_posts

app = Flask(__name__)

HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Error</title>
    <style>
    	body
    	{
    		background-color:white;
    		color:black;
    	}
      	h1 
      	{ 
      		text-align: center; 
      	}
    </style>
  </head>
  <body>
  <h1>Question 3</h1>
  <table border="1px" align="center">
    <tr>
    <td width="250px" height="auto">Date</td>
    <td width="250px" height="auto">Error in percentage</td>
  </tr>
  </table>
%s
  </body>
</html>
'''
POST = '''\
  	<table border="1px" align="center">
  	<tr>
  	<td width="250px" height="auto">%s</td>
  	<td width="250px" height="auto">%s</td>
  	</tr>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "".join(POST % (date,num) for date,num in get_posts())
  html = HTML_WRAP % posts
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)