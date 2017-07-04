from flask import Flask, render_template, redirect
from flask import request as r
from flask import Response
import requests

CLIENT_ID = 'GbRmKgbSMmlE2NlugMeFfQIba8hoVyBFsWS8Igsq'
CLIENT_SECRET = 'BfP7jsN8dSsXjGLfTTPiEvarMJOpkZQ2Y7IVVee8X929LfolMV'

app = Flask(__name__)

@app.route('/')
def sign():
    return "<form action='/signin' method='get'><button type='submit'>Sign in</button></form>"

@app.route('/signin', methods=['GET'])
def signin():
    url = "http://127.0.0.1:5000/oauth2-server/authorize?client_id=%s" % CLIENT_ID
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

if __name__ == "__main__":
    app.run(port=8000)
