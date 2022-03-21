class Player:
    def __init__(self, name: str, nflTeam: str, leagueTeam: str, injuryStatus: str, playerRankings: int, news: str, playerBio: str):
        self.name = name
        self.nflTeam = nflTeam
        self.leagueTeam = leagueTeam
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