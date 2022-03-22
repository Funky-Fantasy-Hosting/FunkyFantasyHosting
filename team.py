import league, matchup, player, playoffs, user

#Defining the type of playerList, which is a list of players
playerListType = 'list[player.Player]'

class Team:
    def __init__(self, id: int, name: str, playerList: playerListType, owner: int, FAABBudget: int):
        self.id = id
        self.name = name
        self.playerList = playerList
        self.startingLineup = None
        self.owner = owner #The ID of the user that owns this team.
        self.nextMatchup = None
        self.status = None
        self.FAABBudget = FAABBudget
        self.waiverPriority = None
        self.rosterSize = None
        self.record = None
        self.rank = None

    def get_id(self):
        return self.id

    def eval_record(self, winWeight, tieWeight, lossWeight):
        return (self.record["Wins"] * winWeight + self.record["Ties"] * tieWeight + self.record["Losses"] * lossWeight)

    def add_player(self, player: player.Player):
        for plyr in self.playerList:
            if(player.get_id() == plyr.get.id()):
                return False
        self.playerList.add(player)
        player.set_league_team(self)
        return True


    def drop_player(self, player:player.Player):
        index = 0
        for plyr in self.playerList:
            if(player.get_id() == plyr.get.id()):
                self.playerList.pop(index)
                return True
            index += 1
        return False

    
    @staticmethod
    def trade_player(player1: player.Player, player2: player.Player):
        team1 = player1.get_league_team()
        team2 = player2.get_league_team()

        team1.drop_player(player1)
        team2.drop_player(player2)

        return None

    def set_lineup():
        return None

    def update_owner():
        return None

    def set_vampire():
        return None