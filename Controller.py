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
	return redirect(url_for("import_league"))

@app.route("/new_league/", methods=["GET", "POST"])
def import_league():
	if request.method == "GET":
		return render_template("import_league.html")
	else:
		# Grab League information from ESPN
		# if (Check to make sure ID was legit):
			return render_template("import_successful.html", 
									user="username", league_type=request.form["league_type"], league_id=request.form["league_id"])
		# else
		#	return render_template("import_failed")
