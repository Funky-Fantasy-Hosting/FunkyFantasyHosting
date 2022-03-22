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
def default():
	return redirect(url_for("home"))

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/new_league/", methods=["GET", "POST"])
def import_league(errMessage=None):
	if request.method == "GET":
		if (errMessage):
			return render_template("import_league.html", message=errMessage)
		else:
			return render_template("import_league.html")
	else:
		# Grab League information from ESPN
		if (request.form["league_id"] == 1):
			return render_template("import_successful.html", 
									user="username", league_type=request.form["league_type"], league_id=request.form["league_id"])
		else:
			return redirect(url_for("import_league", errMessage="Invalid ESPN League ID"))

@app.route("/account")
def account_screen(username=None):
	# Test account information
	teams = [
		{"name": "Vipers", "league": "Pittsburgh", "wins": 10, "loses": 7},
		{"name": "Panthers", "league": "Pitt", "wins": 2, "loses": 15},
		{"name": "Dogs", "league": "Kennel", "wins": 14, "loses": 3},
	]
	return render_template("account.html", username="cps43", teams=teams)

@app.route("/leagues")
def leagues_screen():
	return render_template("leagues.html")

@app.route("/logout")
def logout():
	return redirect(url_for("home"))
