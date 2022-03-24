"""This file contains operations for accessing datastore"""
from google.cloud import datastore
from user import User
from player import Player
from matchup import Matchup
from playoffs import Playoffs
from league import League
from team import Team

"""Basic CRUD operations"""
def retrieve_entity(id, kind='user'):
    client = get_client()
    # Make sure this is an int; string will yield a different result.
    # It's OK to use strings instead, but make sure you're consistent.
    key = client.key(kind, int(id))
    return client.get(key)

"""Adds an entity to the datastore"""
def update_entity(entity):
    client = get_client()
    client.put(entity)

"""Deletes a specific entity from the datastore"""
def delete_entity(id, kind='user'):
    client = get_client()
    key = client.key(kind, int(id))
    client.delete(key)

"""Returns a list of entities"""
def get_entities(kind):
    result = []
    client = get_client()
    query = client.query(kind)
    for entity in query.fetch():
        result.append(entity)
    return result


"""Converts a User object into an entity"""
def user_to_entity(user):
    client = get_client()
    key = client.key('user')
    entity = datastore.Entity(key)
    entity['username'] = user.username
    entity['password'] = user.password
    entity['screenname'] = user.screenname
    entity['leagueList'] = user.leagueList
    entity['commishList'] = user.commishList
    entity['avatar'] = user.avatar
    return entity

"""Converts an entity into a User object"""
def entity_to_user(entity):
    username = entity['username']
    password = entity['password']
    screenname = entity['screenname']
    leagueList = entity['leagueList']
    commishList = entity['commishList']
    avatar = entity['avatar']
    user = User(username, password, screenname, leagueList, commishList, avatar)
    return user

"""Takes user object and returns user entity"""
def get_user_entity(user):
    client = get_client()
    query = client.query(kind="user")
    query = query.add_filter("username", "=", user.username)
    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i


"""Converts a Player object into an entity"""
def player_to_entity(player):
    client = get_client()
    key = client.key('player')
    entity = datastore.Entity(key)
    entity['id'] = player.id
    entity['name'] = player.name
    entity['nflTeam'] = player.nflTeam
    entity['leagueTeam'] = player.leagueTeam
    entity['leagueStatus'] = player.leagueStatus
    entity['fantasyMetrics'] = player.fantasyMetrics
    entity['injuryStatus'] = player.injuryStatus
    entity['playerRankings'] = player.playerRankings
    entity['leagueTransactionHistory'] = player.leagueTransactionHistory
    entity['fantasyPoints'] = player.fantasyPoints
    entity['news'] = player.news
    entity['playerBio'] = player.playerBio
    entity['vunerableFlag'] = player.vunerableFlag
    return entity

"""Converts an entity into a Player object"""
def entity_to_player(entity):
    id = entity['id']
    name = entity['name']
    nflTeam = entity['nflTeam']
    leagueTeam = entity['leagueTeam']
    leagueStatus = entity['leagueStatus']
    fantasyMetrics = entity['fantasyMetrics']
    injuryStatus = entity['injusyStatus']
    playerRankings = entity['playerRankings']
    leagueTransactionHistory = entity['leagueTransactionHistory']
    fantasyPoints = entity['fantasyPoints']
    news = entity['news']
    playerBio = entity['playerBio']
    vunerableFlag = entity['vunerableFlag']
    player = Player(id, name, nflTeam, leagueTeam, leagueStatus, fantasyMetrics, injuryStatus, playerRankings, leagueTransactionHistory, fantasyPoints, news, playerBio, vunerableFlag)
    return player

"""Takes Player object and returns Player entity"""
def get_player_entity(player):
    client = get_client()
    query = client.query(kind="player")
    query = query.add_filter("id", "=", player.id)
    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i


"""Converts a League object into an entity"""
def league_to_entity(league):
    client = get_client()
    key = client.key('league')
    entity = datastore.Entity(key)
    entity['id'] = league.id
    entity['name'] = league.name
    entity['type'] = league.type
    entity['teamList'] = league.teamList
    entity['rosterMax'] = league.rosterMax
    entity['commish'] = league.commish
    entity['playerList'] = league.playerList
    entity['rosterSettings'] = league.rosterSettings
    entity['scoringSettings'] = league.scoreSettings
    entity['memberSettings'] = league.memberSettings
    entity['matchupList'] = league.matchupList
    entity['size'] = league.size
    entity['waiverType'] = league.waiverType
    entity['FAABBudget'] = league.FAABBudget
    entity['waiverDropPeriod'] = league.waiverDropPeriod
    entity['tradeTimeline'] = league.tradeTimeline
    entity['tradeDeadline'] = league.tradeDeadline
    entity['playoffStartTime'] = league.playoffStartTime
    entity['playoffTeamNumber'] = league.playoffTeamNumber
    entity['injuredReserveSlots'] = league.injuredReserveSlots
    entity['irSettingRules'] = league.irSettingRules
    entity['week'] = league.week
    entity['winWeight'] = league.winWeight
    entity['tieWeight'] = league.tieWeight
    entity['lossWeight'] = league.lossWeight
    return entity

"""Converts an entity into a League object"""
def entity_to_league(entity):
    id = entity['id']
    name = entity['name']
    type = entity['type']
    teamList = entity['teamList']
    rosterMax = entity['rosterMax']
    commish = entity['commish']
    playerList = entity['playerList']
    rosterSettings = entity['rosterSettings']
    scoringSettings = entity['scoringSettings']
    memberSettings = entity['memberSettings']
    matchupList = entity['matchupList']
    size = entity['size']
    waiverType = entity['waiverType']
    FAABBudget = entity['FAABBudget']
    waiverDropPeriod = entity['waiverDropPeriod']
    tradeTimeline = entity['tradeTimeline']
    tradeDeadline = entity['tradeDeadline']
    playoffStartTime = entity['playoffStartTime']
    playoffTeamNumber = entity['playoffTeamNumber']
    injuredReserveSlots = entity['injuredReserveSlots']
    irSettingRules = entity['irSettingsRules']
    week = entity['week']
    winWeight = entity['winWeight']
    tieWeight = entity['tieWeight']
    lossWeight = entity['lossWeight']

    """League is going to need to be adjusted to have constructor that takes input for anything we are storing to recreate the object"""
    league = League(id, name, type, teamList, rosterMax, commish, playerList, matchupList, size, waiverType, FAABBudget, waiverDropPeriod)
    return league

"""Takes League object and returns League entity"""
def get_league_entity(league):
    client = get_client()
    query = client.query(kind="league")
    query = query.add_filter("id", "=", league.id)
    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i


"""Converts a Team object into an entity"""
def team_to_entity(team):
    client = get_client()
    key = client.key('team')
    entity = datastore.Entity(key)
    entity['id'] = team.id
    entity['name'] = team.name
    entity['playerList'] = team.playerList
    entity['startingLineup'] = team.startingLineup
    entity['owner'] = team.owner
    entity['nextMatchup'] = team.nextMatchup
    entity['status'] = team.status
    entity['FAABBudget'] = team.FAABBudget
    entity['waiverPriority'] = team.waiverPriority
    entity['rosterSize'] = team.rosterSize
    entity['record'] = team.record
    entity['rank'] = team.rank
    return entity

"""Converts an entity into a Team object"""
def entity_to_team(entity):
    id = entity['id']
    name = entity['name']
    playerList = entity['playerList']
    startingLineup = entity['startingLineup']
    owner = entity['owner']
    nextMatchup = entity['nextMatchup']
    status = entity['status']
    FAABBudget = entity['FAABBudget']
    waiverPriority = entity['waiverPriority']
    rosterSize = entity['rosterSize']
    record = entity['record']
    rank = entity['rank']
   
    """Team is going to need to be adjusted to have constructor that takes input for anything we are storing to recreate the object"""
    team = Team(id, name, playerList, owner, FAABBudget)
    return team

"""Takes Team object and returns Team entity"""
def get_team_entity(team):
    client = get_client()
    query = client.query(kind="team")
    query = query.add_filter("id", "=", team.id)
    query = query.add_filter("owner", "=", team.owner)
    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i


"""Converts a Matchup object into an entity"""
def matchup_to_entity(matchup):
    client = get_client()
    key = client.key('matchup')
    entity = datastore.Entity(key)
    entity['homeTeam'] = matchup.homeTeam
    entity['awayTeam'] = matchup.awayTeam
    entity['homeScore'] = matchup.homeScore
    entity['awayScore'] = matchup.awayScore
    entity['week'] = matchup.week
    entity['league'] = matchup.league
    entity['playoffFlag'] = matchup.playoffFlag
    return entity

"""Converts an entity into a Matchup object"""
def entity_to_matchup(entity):
    homeTeam = entity['homeTeam']
    awayTeam = entity['awayTeam']
    homeScore = entity['homeScore']
    awayScore = entity['awayScore']
    week = entity['week']
    league = entity['league']
    playoffFlag = entity['playoffFlag']

    """Matchup is going to need to be adjusted to have constructor that takes input for anything we are storing to recreate the object"""
    matchup = Matchup(homeTeam, awayTeam, league, week)
    return matchup

"""Takes Matchup object and returns Matchup entity"""
def get_matchup_entity(matchup):
    client = get_client()
    query = client.query(kind="matchup")
    query = query.add_filter("league", "=", matchup.league)

    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i


"""Converts a Playoffs object into an entity"""
def playoff_to_entity(playoff):
    client = get_client()
    key = client.key('team')
    entity = datastore.Entity(key)
    entity['league'] = playoff.league
    entity['teamList'] = playoff.teamList
    entity['matchupList'] = playoff.matchupList
    entity['byeList'] = playoff.byeList
    return entity

"""Converts an entity into a Playoff object"""
def entity_to_playoff(entity):
    league = entity['league']
    teamList = entity['teamList']
    matchupList = entity['matchupList']
    byeList = entity['byeList']
    
    playoff = Playoffs(teamList, league)
    return playoff

"""Takes Playoff object and returns Playoff entity"""
def get_playoff_entity(playoff):
    client = get_client()
    query = client.query(kind="playoff")
    query = query.add_filter("league", "=", playoff.league)

    # query fetch returns an iterator
    for i in query.fetch():
        # return first (and only) one
        return i


"""Returns the current datastore client"""
def get_client():
    return datastore.Client()