import pathlib

import requests
import cachecontrol
import google.auth.transport
from flask import Flask, render_template, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib import flow
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask("Code Ai app")
app.secret_key = "codewithai"
GOOGLE_CLIENT_ID = "907506792605-4vt61ek8bhgb8fbd13p5pn45o3gqs890.apps.googleusercontent.com"
client_secret_file = os.path.join(pathlib.Path(__file__).parent,"client_secret.json")
client = ""

flow = flow.Flow.from_client_secrets_file(client_secrets_file=client_secret_file
,scopes=["https://www.googleapis.com/auth/userinfo.profile","https://www.googleapis.com/auth/userinfo.email","openid"],
redirect_uri="http://127.0.0.1:5000/callback")

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else:
            return function()
    return wrapper


@app.route('/', endpoint='index_endpoint')
def index():
    return render_template('index.html')


@app.route('/login', endpoint='login_endpoint')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route('/callback', endpoint='callback_endpoint')
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500) #state does not match

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    # return id_info # it has all try this and see
    client = id_info
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    session["first_name"] = id_info.get("given_name")
    session["userphoto"] = id_info.get("picture")
    return redirect("/codecraftpage")


@app.route('/logout', endpoint='logout_endpoint')
def logout():
    session.clear()
    return redirect('/')

@app.route('/loginpage', endpoint='loginpage_endpoint')
def loginpage():
    return render_template('login.html')


@app.route('/codecraftpage', endpoint='codecraftpage_endpoint')
@login_is_required
def codecraftpage():
    name = session.get("name", "")
    photoUrl = session.get("userphoto", "")
    email = session.get("email","")
    firstname = session.get("first_name","")

    return render_template('codecraft.html',name=name, photoUrl = photoUrl,email=email,firstname = firstname)

@app.route('/commentpage', endpoint='commentpage_endpoint')
@login_is_required
def comment_page():
    name = session.get("name", "")
    photoUrl = session.get("userphoto", "")
    email = session.get("email", "")
    firstname = session.get("first_name", "")
    return render_template('commentai.html',name=name, photoUrl = photoUrl,email=email,firstname = firstname)

@app.route('/summarizepage', endpoint='summarizepage_endpoint')
@login_is_required
def summarizepage():
    name = session.get("name", "")
    photoUrl = session.get("userphoto", "")
    email = session.get("email", "")
    firstname = session.get("first_name", "")
    return render_template('summarizecode.html',name=name, photoUrl = photoUrl,email=email,firstname = firstname)

@app.route('/transpage', endpoint='transpage_endpoint')
@login_is_required
def transpage():
    name = session.get("name", "")
    photoUrl = session.get("userphoto", "")
    email = session.get("email", "")
    firstname = session.get("first_name", "")
    return render_template('transcode.html',name=name, photoUrl = photoUrl,email=email,firstname = firstname)

if __name__ == '__main__':
    app.run()
