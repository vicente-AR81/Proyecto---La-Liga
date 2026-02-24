def format_match(match):
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]

    score = match["score"]["fullTime"]
    home_goals = score["home"]
    away_goals = score["away"]

    if home_goals is None:
        result = "vs"
    else:
        result = f"{home_goals} - {away_goals}"

    return {
        "home": home,
        "away": away,
        "result": result,
        "date": match["utcDate"][:10]
    }