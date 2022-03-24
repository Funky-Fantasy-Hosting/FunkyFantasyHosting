# Football Import
from espn_api.football import League
# Basketball Import
#from espn_api.basketball import League

# EXAMPLE of using the python version of ESPN v3 for importing a league

s2 = "AECAlZGGZ%2BKVVazn84JPRPKlzGn8c0h0mgcW%2BmMD7rZbRi7Eo%2FD0AftzOhmp%2Bp2OXGN4jU37nau7amjPktismejCclO5Nw2itHBLxlMp5ho0TL9dQYfP8ElaaVYyi8r1rL5VfDEz9ZvVDKtNE2kqhfi5yeNP5G4H75oQV7I6j4oIqUTPdvXSW6KExsDka6tNgzr5Nlrbo1VLR2v7wqsUwnPHjL2y930EX9xhSzVCvN7Nhq47eb%2B%2FTed93BQHkkt1zSj0pk6BF0cQZVSWymyq5%2BSV"
sw_id = "{D3FB8C91-2170-4F49-9BF1-CFF8AABC99A1}"

# public league
#league = League(league_id=1245, year=2018)
# private league with username and password
#league = League(league_id=1245, year=2018, username='userName', password='pass')
# debug mode
#league = League(league_id=1245, year=2018, debug=True)


# private league with cookies
league = League(league_id=1151092, year=2019, espn_s2=s2, swid=sw_id, debug=True)
print(league)

lamar_jackson = league.player_info(playerId=3916387)

print(lamar_jackson)
print(lamar_jackson.stats)

#league.free_agents(week=3)