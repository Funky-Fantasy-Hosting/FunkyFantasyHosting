from FunkyFantasyHosting import league, matchup, player, playoffs, user

#Defining the type of playerList, which is a list of players
playerListType = 'list[player.Player]'


class Team:
    def __init__(self, team_df):
        self.id = team_df.loc['team_id']
        self.name = team_df.loc['team_name']
        self.playerList = team_df.loc['lineup']
        self.startingLineup = None
        self.owner = team_df.loc['user_id'] #The ID of the user that owns this team.
        self.nextMatchup = None
        self.status = None
        self.FAABBudget = None
        self.waiverPriority = None
        self.rosterSize = len(self.playerList)
        self.record = team_df.loc['record']
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