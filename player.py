import team

class Player:
    def __init__(self, id: int, name: str, nflTeam: str, leagueTeam: int, injuryStatus: str, playerRankings: int, news: str, playerBio: str):
        self.id = id
        self.name = name
        self.nflTeam = nflTeam
        self.leagueTeam = leagueTeam #The ID of the league team
        self.leagueStatus = None
        self.fantasyMetrics = None
        self.injuryStatus = injuryStatus
        self.playerRankings = playerRankings
        self.leagueTransactionHistory = None
        self.fantasyPoints = None
        self.news = news
        self.playerBio = playerBio
        self.vunerableFlag = None

    def __repr__(self):
        return None

    def get_id(self):
        return self.id

    def get_league_team(self):
        return self.leagueTeam

    def set_league_team(self, team:team.Team):
        self.leagueTeam = team.get_id()
        return True