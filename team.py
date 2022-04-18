import FunkyFantasyHosting.league, FunkyFantasyHosting.matchup, FunkyFantasyHosting.player, FunkyFantasyHosting.playoffs, FunkyFantasyHosting.user

#Defining the type of playerList, which is a list of players
playerListType = 'list[player.Player]'


class Team:
    def __init__(self, team_df):
        self.id = 'team_id'
        self.name = 'team_name'
        self.playerList = [{"link": "https://www.espn.com/nfl/player/_/id/3039707/mitchell-trubisky", "position": "QB", "name": "Mitchell Trubisky", "opp": "Browns", "points": 10},
        {"link": "https://www.espn.com/nfl/player/_/id/4241457/najee-harris", "position": "RB", "name": "Najee Harris", "opp": "Browns", "points": 20},
        {"link": "https://www.espn.com/nfl/player/_/id/4046692/chase-claypool", "position": "WR", "name": "Chase Claypool", "opp": "Browns", "points": 13},]
        self.startingLineup = None
        self.owner = 'test' #The ID of the user that owns this team.
        self.nextMatchup = None
        self.status = None
        self.FAABBudget = None
        self.waiverPriority = None
        self.rosterSize = len(self.playerList)
        self.record = "0-0"
        self.rank = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


    #Returns an integer representing the record of the team so it can be ordered with other teams
    def eval_record(self, winWeight, tieWeight, lossWeight):
        return (self.record["Wins"] * winWeight + self.record["Ties"] * tieWeight + self.record["Losses"] * lossWeight)

    def add_player(self, player):
        for plyr in self.playerList:
            if(player.get_id() == plyr.get.id()):
                return False
        self.playerList.add(player)
        player.set_league_team(self)
        return True


    def drop_player(self, player):
        index = 0
        for plyr in self.playerList:
            if(player.get_id() == plyr.get.id()):
                self.playerList.pop(index)
                return True
            index += 1
        return False

    

    #This method needs to drop both players and then add them to the other teams, but we also have to make sure each step can happen.

    #METHOD MOVED TO LEAGUE CLASS
    
    # @staticmethod
    # def trade_player(player1: player.Player, player2: player.Player):
    #     team1 = player1.get_league_team()
    #     team2 = player2.get_league_team()

    #     team1.drop_player(player1)
    #     team2.drop_player(player2)

    #     return None

    def set_lineup():
        return None

    def update_owner():
        return None

    def set_vampire():
        return None