# Setup of importing/init comes from fl10_model.py
from flask import Flask, request, abort, url_for, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

# init #
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FFH.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# View #

# Initialize Database
@app.cli.command('initdb')
def initdb_command():
	"""Reinitializes the database each time"""
	db.drop_all()
	db.create_all()

# Redirect to home by default
@app.route("/")
def default(user=None):
	return redirect(url_for("home", user=user))

# Home Screen
@app.route("/home")
def home(user=None):
	return render_template("home.html", username="TestUser")

# New League Screen
@app.route("/new_league/", methods=["GET", "POST"])
def import_league(user=None):
	if request.method == "GET":
		return render_template("import_league.html", username="TestUser")
	else:
		# Grab League information from ESPN
		if (request.form["league_id"] == "1"):
			return render_template("import_successful.html", username="TestUser", league_type=request.form["league_type"], league_id=request.form["league_id"])
		else:
			return render_template("import_league.html", username="TestUser", message="Invalid EPSN League ID")

# Account Screen
@app.route("/account")
@app.route("/account/<user>")
def account_screen(user=None, userTeams=None):
	# TODO: Test account information
	# TODO: Grab league list from player object
	# TODO: Grab which team user controls within the league (record too)
	userTeams = [
		{"league": "Atlantic", "team": "Buffalo Sabres", "record": "23-33"},
		{"league": "Metropolitan", "team": "Pittsburgh Penguins", "record": "40-17"},
		{"league": "Central", "team": "Chicago Blackhawks", "record": "24-32"},
		{"league": "Pacific", "team": "Vegas Golden Knights", "record": "36-28"},
	]
	return render_template("account.html", username="TestUser", teams=userTeams)

# League Screen
@app.route("/leagues")
@app.route("/leagues/<leagueName>")
def leagues_screen(leagueName=None):
	# TODO: Convert example lists to database calls
	standings = [
		{"name": "Pittsburgh Penguins", "wins": "40", "loses": "17"},
		{"name": "Washington Capitals", "wins": "36", "loses": "28"},
		{"name": "Philadelphia Flyers", "wins": "24", "loses": "32"},
		{"name": "New York Rangers", "wins": "23", "loses": "33"},
	]
	matchups = [
		{"home": "Pittsburgh Penguins", "away": "New York Rangers", "home_points": "3", "away_points": "2"},
		{"home": "Philadelphia Flyers", "away": "Washington Capitals", "home_points": "0", "away_points": "0"}
	]
	return render_template("leagues.html", username="TestUser", leagueName=leagueName, teams=standings, matchups=matchups, week=5)

# Team Screen
@app.route("/team")
@app.route("/team/<leagueName>/<teamName>")
def team(leagueName=None, teamName=None):
	# TODO: Grab team / bench from backend
	teamList = [
		{"link": "https://www.espn.com/nfl/player/_/id/3039707/mitchell-trubisky", "position": "QB", "name": "Mitchell Trubisky", "opp": "Browns", "points": 10},
		{"link": "https://www.espn.com/nfl/player/_/id/4241457/najee-harris", "position": "RB", "name": "Najee Harris", "opp": "Browns", "points": 20},
		{"link": "https://www.espn.com/nfl/player/_/id/4046692/chase-claypool", "position": "WR", "name": "Chase Claypool", "opp": "Browns", "points": 13},
	]
	benchList = [
		{"link": "https://www.espn.com/nfl/player/_/id/4361411/pat-freiermuth", "position": "TE", "name": "Pat Friermuth", "opp": "Browns", "points": 5}
	]
	return render_template("team.html", username="TestUser", team=teamList, bench=benchList)

@app.route("/player/<playerId>")
def player(playerId=None):
	# TODO: Grab player from ESPN using playerId
	player = {"name": "Bob Smith",
			  "fumbles": "0",
			  "receiving_targets": "2",
			  "receiving_yards": "30",
			  "receiving_touchdowns": "1",
			  "receptions": "2",
			  "rushing_attempts": "0",
			  "rushing_yards": "0",
			  "rushing_touchdowns": "0",
			}
	return render_template("player.html", player=player)

# Logout Screen
@app.route("/logout")
def logout():
	# TODO: Log user out and return to /home
	return redirect(url_for("home"))

# Login Screen
@app.route('/login')
def login():
    return render_template("login.html")

# Create Account Screen
@app.route('/create_account')
def create_account():
    return render_template("create_account.html")
