import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN") #<-- Token guardado en la consola de windows (No poner)-->

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/api/teams')
def get_teams():

    url = "https://api.football-data.org/v4/matches"

    headers = {
        "X-Auth-Token": API_TOKEN 
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

