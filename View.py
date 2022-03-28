# Setup of importing/init comes from fl10_model.py
from flask import Flask, request, abort, url_for, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

# init #
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

# Redirect to login by default (idea from fl06_session.oy)
@app.route("/")
def default(user=None):
	return redirect(url_for("home", user=user))

@app.route("/home")
def home(user=None):
	return render_template("home.html", username=user)

@app.route("/new_league/", methods=["GET", "POST"])
def import_league(user=None, errMessage=None):
	if request.method == "GET":
		if (errMessage):
			return render_template("import_league.html", message=errMessage, username=user)
		else:
			return render_template("import_league.html", username=user)
	else:
		# Grab League information from ESPN
		if (request.form["league_id"] == 1):
			return render_template("import_successful.html", 
									username=user, league_type=request.form["league_type"], league_id=request.form["league_id"])
		else:
			return redirect(url_for("import_league", user=user, errMessage="Invalid ESPN League ID"))

@app.route("/account")
def account_screen(user=None, userTeam=None):
	# Test account information
	return render_template("account.html", username=user, team=userTeam)

@app.route("/leagues")
def leagues_screen(user=None):
	return render_template("leagues.html", username=user)

@app.route("/team")
def team(user=None, team=None):
	teamList = [
		{"link": "https://www.espn.com/nfl/player/_/id/3039707/mitchell-trubisky", "position": "QB", "name": "Mitchell Trubisky", "opp": "Browns", "points": 10},
		{"link": "https://www.espn.com/nfl/player/_/id/4241457/najee-harris", "position": "RB", "name": "Najee Harris", "opp": "Browns", "points": 20},
		{"link": "https://www.espn.com/nfl/player/_/id/4046692/chase-claypool", "position": "WR", "name": "Chase Claypool", "opp": "Browns", "points": 13},
	]
	benchList = [
		{"link": "https://www.espn.com/nfl/player/_/id/4361411/pat-freiermuth", "position": "TE", "name": "Pat Friermuth", "opp": "Browns", "points": 5}
	]
	return render_template("team.html", username="TestUser", team=teamList, bench=benchList)

@app.route("/logout")
def logout():
	return redirect(url_for("home"))

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/create_account')
def create_account():
    return render_template("create_account.html")
