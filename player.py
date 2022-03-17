class Player:
    def __init__(self, name, nflTeam, leagueTeam, injuryStatus, playerRankings, news, playerBio):
        self.name = name
        self.nflTeam = nflTeam
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