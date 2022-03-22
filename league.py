import team, user, player, matchup, playoffs

class League:

    #Global Constants related to the League class

    #The different types of leagues that can be created, assigned to arbitrary integers to prevent misspelling and unneccesary string comparisons
    DEFAULT, GUILLOTINE, VAMPIRE, PIRATE = 0, 1, 2, 3

    #The differnt types of waivers, which is either waiver or faab
    WAIVER, FAAB = 0, 1





    def __init__(self, name: str, type: int, teamList: 'list[team.Team]', rosterMax: int, commish: user.User, playerList: 'list[player.Player]', matchupList: 'list[matchup.Matchup]', size: int, waiverType: int, FAABBudget: int, waiverDropPeriod: int,):
        self.name = name
        self.type = type
        self.teamList = teamList
        self.rosterMax = rosterMax
        self.commish = commish
        self.playerList = playerList
        self.rosterSettings = None
        self.scoringSettings = None
        self.memberSettings = None
        self.matchupList = matchupList
        self.size = size
        self.waiverType = waiverType
        self.FAABBudget = FAABBudget
        self.waiverDropPeriod = None
        self.tradeTimeline = None
        self.tradeDeadline = None
        self.playoffStartTime = None
        self.playoffTeamNumber = None
        self.injuredReserveSlots = None
        self.irSettingRules = None
        #self.teamStandings = None #Don't need because teamList is sorted from last to first
        self.week = None
        self.winWeight = 2 #How much a win counts for in terms of standings
        self.tieWeight = 1 #How much a tie counts for in terms of standings
        self.lossWeight = 0 #How much a loss counts for in terms of standings

    def __repr__(self):
        return None
    
    def sort_team_list(self):
        self.teamList.sort(key = lambda x: x.eval_record(self.winWeight, self.tieWeight, self.lossWeight))
        return True

    def add_team(self, team: team.Team):
        for tm in self.teamList:
            if tm.get_id() == team.get_id(): #Teams cannot have the same ID
                return(False)
            if tm.get_name() == team.get_name(): #Teams in the same league cannot have the same name
                return(False)
        self.teamList.add(team)
        return True
    
    def remove_team(self, team: team.Team):
        index = 0
        for tm in self.teamList:
            if tm.get_id() == team.get_id():
                self.teamList.pop(index)
                return True
            index += 1
        return False

    def guillotine_team(self):
        self.sort_team_list()
        return self.remove_team(self.teamList(0))

    def set_scoring():
        return None

    def set_matchup():
        return None

    def set_FAAB():
        return None

    def lock_waivers():
        return None

    def process_trade():
        return None

    def set_pirate():
        return None

    def set_vampire():
        return None

    def set_pirate_settings():
        return None

    def set_vampire_settings():
        return None



