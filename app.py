# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login' , method = 'POST')
def verify_otp():
    username = request.form["username"]
    password = request.form["password"]
    mobile_number = request.form["number"]

    if(username == 'verify' password == '12345'):
        ACCOUNT_SID = "AC581715db7ddccb97bb594b93d90677e8"
        AUTH_TOKEN = "543ff7222942ec033191cbf8669610cd"
        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return(text = "Entered User ID or Password is wrong")

def Client():
    client = AccessToken(ACCOUNT_SID , AUTH_TOKEN)


        verification = client.verify \
            .services('VAcbf3c71ae6f0a2cb433b0cfcf1c5b763') \
            .verifications \
            .create(to=mobile_number, channel='sms')










if __name__ == "__main__":
    app.run()

