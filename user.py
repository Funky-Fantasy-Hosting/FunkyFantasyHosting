from . import league, matchup, player, playoffs, team

#Define the type of leagueList, which is a list of leagues
leagueListType = 'list[league.League]'


class User:
    def __init__(self, username, password, screenname, leagueList, commishList, avatar):
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

    def get_username(self):
        return self.username

    def get_leagueList(self):
        return self.leagueList

    def add_league(self, lid):
        self.leagueList.add(lid)
        return True

    # def remove_league(self, league):
    #     targetId = league.get_id
    #     index = 0
    #     for lge in self.leagueList:
    #         id = lge.get_id()
    #         if(id == targetId):
    #             self.leagueList.pop(index)
    #             return True
    #         index += 1

    #     return False
    
    def update_avatar(self, avatar):
        self.avatar = avatar
        return True

    def update_password():
        return None

    def get_id(self):
        id = 0
        for x in range(0, len(self.username)):
            id += ord(self.username[x])
        return id
        
