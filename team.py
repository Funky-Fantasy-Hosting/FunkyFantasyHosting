import league, matchup, player, playoffs, user

#Defining the type of playerList, which is a list of players
playerListType = 'list[player.Player]'

class Team:
    def __init__(self, name: str, playerList: playerListType, owner: int, FAABBudget: int):
        self.name = name
        self.playerList = playerList
        self.startingLineup = None
        self.owner = owner #The ID if the user that owns this team.
        self.nextMatchup = None
        self.status = None
        self.FAABBudget = FAABBudget
        self.waiverPriority = None
        self.rosterSize = None
        self.record = dict.fromkeys(['Wins', 'Ties', 'Losses'], 0)
        self.rank = None

    def eval_record(self, winWeight, tieWeight, lossWeight):
        return (self.record["Wins"] * winWeight + self.record["Ties"] * tieWeight + self.record["Losses"] * lossWeight)


    def add_player(self, player: player.Player):
        for plyr in self.playerList:
            if(player.get_id() == plyr.get.id()):
                return False
        self.playerList.add(player)
        return None


    def drop_player():
        return None

    
    def trade_player():
        return None

    def set_lineup():
        return None

    def update_owner():
        return None

    def set_vampire():
        return None