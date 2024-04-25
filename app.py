from flask import Flask, request, jsonify,render_template,json
import pandas as pd
import requests

app = Flask(__name__)

def get_data():
    URL = "https://api.quotable.io/random"
    response = requests.get(URL)
    response_json = response.json()
    return response_json

@app.route('/getdata', methods = ['GET','POST','DELETE'])
def data():
    if request.method == 'GET':
        return (get_data())
    else:
        return 'API WORKING'

@app.route('/postdata', methods = ['GET','POST','DELETE'])
def post_data():
    if request.method == 'GET':
        res = get_data()
        print(res)
        return render_template('author.html', jsonfile = res)
    else:
        return 'API WORKING'


if __name__=='__main__':
    app.run(debug = True)
get_data()
