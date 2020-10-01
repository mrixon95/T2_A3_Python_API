import unittest
from unittest.mock import patch
from data_handler import Data_Handler as dh


class TestOrderStandings(unittest.TestCase):
    
    
	def setUp(self):
		dh.import_team_data()
		dh.import_player_data()
		dh.import_past_two_seasons_data()
		
	
	def test_ordering_players_based_on_stats(self):
	    
	    team = dh.get_team('HOU')
	    team.reorder("Salary")
	    top_paid_player = team._players[0]
	    top_paid_player_name = top_paid_player.full_name
	    self.assertEqual(top_paid_player_name, 'Russell Westbrook')
	    
	    team.reorder("Height")
	    tallest_player = team._players[0]
	    tallest_player_name = tallest_player.full_name
	    self.assertEqual(tallest_player_name, 'Tyson Chandler')
	    
	    team = dh.get_team('LAL')
	    team.reorder("Weight")
	    heaviest_player = team._players[0]
	    heaviest_player_name = heaviest_player.full_name
	    self.assertEqual(heaviest_player_name, 'JaVale McGee')
	    
	    team.reorder("Age")
	    oldest_player = team._players[0]
	    oldest_player_name = oldest_player.full_name
	    self.assertEqual(oldest_player_name, 'LeBron James')
	    
	
	def test_print_out_player(self):
	    
	    team = dh.get_team('HOU')
	    team.reorder("Salary")
	    top_paid_player = team._players[0]
	    self.assertEqual(str(top_paid_player), 
	    
	    f"Russell Westbrook of the Houston Rockets"
        f" is 31 years old."
        f"\nHis team plays in both the Western conference and the Southwest division."
        f"\nHe is 190.5cm tall and weighs 90.9kg."
        f"\nHis salary is $38,506,482 and he has been playing in"
        f" the NBA for 12 years.\n"

        "\nFurther player details:\n"
        '{:<40}'.format("\nBirthday: 12/11/1988")
        + '{:<40}'.format("Birth City: Long Beach")
        + '{:<40}'.format("\nBirth State: California")
        + '{:<40}'.format("College: UCLA")
        + '{:<40}'.format("\nPosition: PG")
        + '{:<40}'.format("Jersey Number: 0")
	    )
	    
 
	def test_reorder_standings(self):
	    
	    team_standings = dh.search_team_standings(2020)  
	    team_standings.reorder('team name')
	    self.assertEqual(team_standings.ordering, 'team name')
	    city_team_last_alphabet = team_standings._eastern_conference[0].city
	    self.assertEqual(city_team_last_alphabet, 'Washington')
	    
	    team_standings.reorder('percentage')
	    city_team_last_alphabet = team_standings._western_conference[0].city
	    self.assertEqual(city_team_last_alphabet, 'Golden State')
	    
	    
