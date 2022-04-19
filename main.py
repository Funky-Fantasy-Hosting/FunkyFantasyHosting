# Setup of importing/init comes from fl10_model.py
from flask import Flask, request, abort, url_for, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import user as User
from data_access import *
import bcrypt
import league, team, user, player, matchup, playoffs, bigquery_fun

#from FunkyFantasyHosting.ESPN_endpoints.EXAMPLE_league_pull_api import *

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
def default():
	return redirect(url_for("home"))

# Home Screen
@app.route("/home")
def home():
  return render_template("home.html")


# New League Screen
@app.route("/new_league/", methods=["GET", "POST"])
def import_league():
	if request.method == "GET":
		return render_template("import_league.html")
	else:
		# Grab League information from ESPN
		# df_league_table = pull_new_league(request.form["league_id"], 2) 	# example of new league
		return render_template("import_successful.html", league_type=request.form["league_type"], league_id=request.form["league_id"])

# Join League Screen
@app.route("/join_league/", methods=["GET", "POST"])
def join_league():
	if "username" in session:
		if request.method == "GET":
			return render_template("join_league.html")
		else:
			#TODO test/register signed in user to appropriate team using given league id and team name
			#call function to get list/dict of teams from entered league ID ie list/dict = function(request.form["league_id"])
			#if request.form["team_name"] in list/dict
				#update DB, render template for updated account page
			#else 
				#return render_template("invalid_join_league.html")
			return redirect(url_for("account_screen"))
	else: 
		return render_template("account.html")

# Account Screen
@app.route("/account", methods=["GET", "POST"])
def account_screen(userTeams=None):
	if "username" in session:
		#TODO Call method to populate a table representing list of leagues a user belongs to
		#For now displays the hypothetical test league the group members belong to, and a random team from that league
		testLeague = league.League(721301807)
		teams = testLeague.get_teams()
		userTeams = [
			{"league": "721301807", "team": teams[0].get_name(), "record": "0-0"}
		]
		if request.method == "POST":
			#TODO modeify the way changing an active league is done by the user, will require cooresponding changes to account.html
			#For now user is asked to type in the league they wish to make active. Any of the names listed in the hypothetitcal 
			#table of leagues will add a leagueID session variable, thus giving access to the league screen
			leagueID = request.form['leagueID'] 
			if leagueID == "Atlantic" or leagueID == "Metropolitan" or leagueID == "Central" or leagueID == "Pacific":
				session["leagueID"] = request.form['leagueID']
				return render_template("account.html", teams=userTeams)
			else:
				return render_template("account.html", teams=userTeams)
		else:
			return render_template("account.html", teams=userTeams)
	else: 
		return render_template("account.html")

# League Screen
@app.route("/league")
@app.route("/league/<leagueName>")
def leagues_screen(leagueName=None):
	if leagueName is not None:
		session["leagueID"] = leagueName
	if "leagueID" in session:
		# TODO Call function to load in standings cooresponding table data for league, for now loads sample data made by connor
		# TODO: Convert example lists to database calls
		testLeague = league.League(721301807)
		teams = testLeague.get_teams()
		teams[0].get_name()
		standings = [
			{"name": teams[0].get_name(), "wins": "0", "losses": "0"}]
		for t in (range(len(teams) - 1)):
			standings.append({"name": teams[t+1].get_name(), "wins": "0", "losses": "0"}); 
		
		matchups = [
			{"matchId": "1", "home": "Pittsburgh Penguins", "away": "New York Rangers", "home_points": "3", "away_points": "2"},
			{"matchId": "2", "home": "Philadelphia Flyers", "away": "Washington Capitals", "home_points": "0", "away_points": "0"}
		]
		return render_template("league.html", teams=standings, matchups=matchups, week=5)
	else:
		return redirect(url_for("account_screen"))
		
# Free Agent Screen
@app.route("/freeAgents", methods=["GET", "POST"])
def free_Agent_Screen(freeAgents=None):
	if "username" in session:
		if "leagueID" in session:
			#TODO Call method to populate a table representing list of players not belonging a team for a particiular league
			#For now hypothetical list created below
			freeAgents = [
				{"name": "Zach Wilson", "nflTeam": "New York Jets"},
				{"name": "Rashaad Penny", "nflTeam": "Seattle Seahawks"},
				{"name": "Randall Cobb", "nflTeam": "Green Bay Packers"},
				{"name": "Cole Kmet", "nflTeam": "Chicago Bears"},
			]
			if request.method == "POST":
				#TODO have button trigger call to update DB
				return redirect(url_for("league_screen"))
			else:
				return render_template("free_agent.html", freeAgents=freeAgents)
		else:
			return redirect(url_for("account_screen"))
	else: 
		return render_template("free_agent.html")

# Team Screen
@app.route("/team")
@app.route("/team/<leagueName>/<teamName>")
def team(leagueName=None, teamName=None):
	# TODO: Grab team / bench from backend
	# TODO: Determine which team owns the team
	teamList = [
		{"link": "https://www.espn.com/nfl/player/_/id/3039707/mitchell-trubisky", "position": "QB", "name": "Mitchell Trubisky", "opp": "Browns", "points": 10},
		{"link": "https://www.espn.com/nfl/player/_/id/4241457/najee-harris", "position": "RB", "name": "Najee Harris", "opp": "Browns", "points": 20},
		{"link": "https://www.espn.com/nfl/player/_/id/4046692/chase-claypool", "position": "WR", "name": "Chase Claypool", "opp": "Browns", "points": 13},
	]
	benchList = [
		{"link": "https://www.espn.com/nfl/player/_/id/4361411/pat-freiermuth", "position": "TE", "name": "Pat Friermuth", "opp": "Browns", "points": 5},
		{"link": "https://www.espn.com/nfl/player/_/id/3932905/diontae-johnson", "position": "WR", "name": "Diontae Johnson", "opp": "Browns", "points": 12},
	]
	return render_template("team.html", team=teamList, bench=benchList, league=leagueName, teamOwner="test")

@app.route("/matchup/<matchupId>")
def matchup(matchupId=None):
	# TODO: Grab home team and away team's rosters from DB
	homeList = [
		{"link": "https://www.espn.com/nfl/player/_/id/3039707/mitchell-trubisky", "position": "QB", "name": "Mitchell Trubisky", "opp": "Browns", "points": 10},
		{"link": "https://www.espn.com/nfl/player/_/id/4241457/najee-harris", "position": "RB", "name": "Najee Harris", "opp": "Browns", "points": 20},
		{"link": "https://www.espn.com/nfl/player/_/id/4046692/chase-claypool", "position": "WR", "name": "Chase Claypool", "opp": "Browns", "points": 13},
	]
	homeBenchList = [
		{"link": "https://www.espn.com/nfl/player/_/id/4361411/pat-freiermuth", "position": "TE", "name": "Pat Friermuth", "opp": "Browns", "points": 5}
	]
	awayList = [
		{"link": "https://www.espn.com/nfl/player/_/id/4361411/pat-freiermuth", "position": "TE", "name": "Pat Friermuth", "opp": "Browns", "points": 5},
		{"link": "https://www.espn.com/nfl/player/_/id/4046692/chase-claypool", "position": "WR", "name": "Chase Claypool", "opp": "Browns", "points": 13},
		{"link": "https://www.espn.com/nfl/player/_/id/4241457/najee-harris", "position": "RB", "name": "Najee Harris", "opp": "Browns", "points": 20},
	]
	awayBenchList = [
		{"link": "https://www.espn.com/nfl/player/_/id/3039707/mitchell-trubisky", "position": "QB", "name": "Mitchell Trubisky", "opp": "Browns", "points": 10},
	]

	homeTeam = {
		"name": "Pittsburgh Penguins",
		"roster": homeList,
		"bench": awayBenchList,
		"totalPoints": "43",
	}
	awayTeam = {
		"name": "Washington Capitals",
		"roster": awayList,
		"bench": awayBenchList,
		"totalPoints": "28",
	}

	return render_template("matchup.html", awayTeam=awayTeam, homeTeam=homeTeam, week=5)

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
	if "username" in session:
		session.clear()
		return redirect(url_for("home"))
	else:
		return redirect(url_for("home"))

# Login Screen
@app.route('/login', methods=["GET", "POST"])
def login_screen():
		if request.form.get("login") == "True":
			username = request.values.get('username')
			password = request.values.get('password')
			
			hashedPassword = createHashedPassword(password)

			# create user object
			user = User(username, hashedPassword, None, None, None, None)

			# check if user exists
			entity = get_user_entity(user)
			if entity:
				#User exists
				user2 = entity_to_user(entity)
				if checkPassword(password, user2.password):
					session['username'] = username
					return (redirect("/"))
				else:
					# Username and Password do not match
					return render_template("invalid_login.html")
			else:
				# Username or Password does not exist
				return render_template("invalid_login.html")
		return (render_template("login.html"))


# Create Account Screen
@app.route('/create_account', methods=["GET", "POST"])
def create_account():
	if request.method == 'POST':
		if request.form.get("create_account") == "True":
			email = request.values.get('email')
			username = request.values.get('username')
			password = request.values.get('password')
			screenname = request.values.get('screenname')
			hashedPassword = createHashedPassword(password)
			user = User(username, hashedPassword, screenname, None, None, None)

			temp = get_user_entity(user)

			if temp:
				#User already exists error
				entity_to_user(temp)
				return(render_template("login.html"))
			else:
				entity = user_to_entity(user)
				update_entity(entity)
				session['username'] = username
				return (redirect("/"))
	return (render_template("create_account.html"))

# Secrect key for sessions
app.secret_key = "!s3cr3t k3y!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# Create hashed password
def createHashedPassword(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def checkPassword(password, hashedPassword):
    return bcrypt.checkpw(password, hashedPassword)
