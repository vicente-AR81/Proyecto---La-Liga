import os
import requests
from flask import Flask, render_template, jsonify
from Banderas import country_to_code

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

    team_url = f"https://api.football-data.org/v4/teams/{team_id}"
    matches_url = f"https://api.football-data.org/v4/teams/{team_id}/matches?limit=5"

    team_response = requests.get(team_url, headers=headers)
    matches_response = requests.get(matches_url, headers=headers)

    team = team_response.json()
    matches = matches_response.json().get("matches", [])

    position_map = {
        "Goalkeeper": "PO",
        "Defence": "DFC",
        "Midfield": "MC",
        "Offence": "DEL",
        None: "-"
    }

    for player in team.get("squad", []):
        original_position = player.get("position")
        player["shortPosition"] = position_map.get(original_position, original_position)
        code = country_to_code(player.get("nationality"))
        if code:
            player["flagUrl"] = f"https://flagcdn.com/w40/{code}.png"
        else:
            player["flagUrl"] = None
        

    return render_template("club.html", team=team, matches=matches)

@app.route("/Clasificaciones")
def Clasificaciones():
    url = "https://api.football-data.org/v4/competitions/PD/standings"
    response = requests.get(url, headers=headers)
    data = response.json()

    table = data["standings"][0]["table"]

    for team in table:
        if team["form"] is None:
            team["form"] = ""

    return render_template("Clasificaciones.html", table=table)


@app.route("/Tabla-Goleadores")
def Goleadores():
    url = "https://api.football-data.org/v4/competitions/PD/scorers"
    response = requests.get(url, headers=headers)
    data = response.json()

    scorers = data["scorers"]

    return render_template("Goleadores.html", scorers=scorers)



@app.route("/Tabla-Asistencias")
def Asistencias():
    url = "https://api.football-data.org/v4/competitions/PD/scorers"
    response = requests.get(url, headers=headers)
    data = response.json()

    players = data["scorers"]

    # Hace que los jugadores con null asistencias se transforme a 0
    for p in players:
        if p["assists"] is None:
            p["assists"] = 0

    # Ordenar por asistencias (de mayor a menor)
    players_sorted = sorted(players, key=lambda x: x.get("assists", 0), reverse=True)

    return render_template("Asistencias.html", assists=players_sorted)


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

