# Setup of importing/init comes from fl10_model.py
from flask import Flask, request, abort, url_for, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy


# init # Thank you IDE power
from FunkyFantasyHosting.ESPN_endpoints.EXAMPLE_league_pull_api import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FFH.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models #
members = db.Table('members',
		db.Column('league_id', db.Integer, db.ForeignKey('league.ID'), primary_key=True),
		db.Column('user_id', db.Integer, db.ForeignKey('user.ID'), primary_key=True)
	)

class League(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	game_type = db.Column(db.String(20))
	member_list = db.relationship('User', secondary=members, lazy='subquery', backref=db.backref('leagues', lazy=True))
	commissioner = db.Column(db.String(20))
	records = db.Column(db.String(80))

class User(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20))
	avatar = db.Column(db.Text) # store Avatar as a link to their picture
	password = db.Column(db.String(20))

# Controllers #

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
	return render_template("home.html", username=user)

# New League Screen
@app.route("/new_league/", methods=["GET", "POST"])
def import_league(user="Scrappy", errMessage=None):
	if request.method == "GET":
		if (errMessage):
			return render_template("import_league.html", message=errMessage, username=user)
		else:
			return render_template("import_league.html", username=user)
	else:
		df_league_table = pull_new_league(request.form["league_id"], 2) 	# example of new league
		return render_template("import_successful.html",
								username=user, league_type=request.form["league_type"], league_id=request.form["league_id"])

		# # Grab League information from ESPN
		# if (request.form["league_id"] == 1):
		# 	say_hi()
		# 	pull_new_league(request.form["league_id"])
		# 	return render_template("import_successful.html",
		# 							username=user, league_type=request.form["league_type"], league_id=request.form["league_id"])
		#
		# else:
		# 	return redirect(url_for("import_league", user=user, errMessage="Invalid ESPN League ID"))

# Account Screen
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
@app.route("/leagues/<leagueName>")
def leagues_screen(leagueName=None):
	return render_template("leagues.html", username="TestUser")

# Team Screen
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
