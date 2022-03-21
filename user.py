import league, matchup, player, playoffs, team

#Define the type of leagueList, which is a list of leagues
leagueListType = 'list[league.League]'


class User:
    def __init__(self, username: str, password: str, screenname: str, leagueList: leagueListType, commishList, avatar:str):
        self.username = username
        self.password = password #Obviously username and password are going to be more secure than this
        self.screenname = screenname
        self.leagueList = leagueList
        self.commishList = commishList
        self.avatar = avatar #Avatar is a string that represents the image, like the name of the file or the path or something.

    def login():
        return None

    def logout():
        return None

    def add_league(self, league: league.League):
        self.leagueList.add(league)
        return True

    def remove_league(self, league: league.League):
        targetId = league.get_id
        index = 0
        for lge in self.leagueList:
            id = lge.get_id()
            if(id == targetId):
                self.leagueList.pop(index)
                return True
            index += 1

        return False
    
    def update_avatar(self, avatar: str):
        self.avatar = avatar
        return True

    def update_password():
        return None