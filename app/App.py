import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN") #<-- Token guardado en la consola de windows (No poner)-->

URL = "https://api.football-data.org/v4/competitions/PD/teams"

headers = {"X-Auth-Token": API_TOKEN}

@app.route("/")
def index():
    response = requests.get(URL, headers=headers)
    data = response.json()

    teams = data["teams"]

    # solo los 20 equipos (seguridad)
    teams = teams[:20]

    return render_template("index.html", teams=teams)

@app.route("/club/<int:team_id>")
def club(team_id):
    url = f"https://api.football-data.org/v4/teams/{team_id}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Error API: {response.status_code}"

    team_data = response.json()

    return render_template("club.html", team=team_data)


@app.route('/api/teams')
def get_teams():

    url = "https://api.football-data.org/v4/competitions/PD/teams"

    headers = {
        "X-Auth-Token": API_TOKEN 
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

