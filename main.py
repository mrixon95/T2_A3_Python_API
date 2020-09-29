from data_handler import Data_Handler as dh
from statistics_classes import Player, Team, Season

dh.import_team_data()
dh.import_player_data()
dh.import_past_two_seasons_data()


player = dh.search_player_data()
print(player)
