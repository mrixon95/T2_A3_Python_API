
import requests
import json
from statistics_classes import Player, Team_Standing, Season, Team

class Data_Handler():
    
    season_dict = {}
    players_dict = {}
    teams_dict = {}
    
    
    @classmethod
    def get_team(cls, team_key):
        team = cls.teams_dict.get(team_key)
        
        if team != None:
            return team
        else:
            print(f"There is no team with {team_key} as their key")
    
    
    @classmethod
    def import_player_data(cls):

        url = "https://api.sportsdata.io/v3/nba/scores/json/Players"
        
        headers = {"Ocp-Apim-Subscription-Key" : "a97b696fd5bd43798916b4a0dbb0f64f"}
        
        response = requests.get(url,headers=headers)
        players_data = json.loads(response.text)
        total_players = len(players_data)
        
        
        for player in players_data:
            
            key = str(player['PlayerID']) + '_' + player['FirstName'] + '_' + player['LastName'] + '_' + str(player['TeamID'])
            player_object = Player(player['PlayerID'], player['FirstName'], player['LastName'], player['TeamID'], player['Team'], player['Jersey'], 
            player['Position'], player['BirthDate'], player['BirthCity'], player['BirthState'], player['College'], player['Experience'], player['Salary'], player['Height'], player['Weight'])
            
            team_object = cls.teams_dict.get(player['Team'])
            
            player_object.set_team(team_object)
            
            cls.players_dict[key] = player_object
            
        
        print(f"All {total_players} active NBA players have been loaded")
        
    
    
    @staticmethod
    def get_current_season_number():
    
        headers = {"Ocp-Apim-Subscription-Key" : "a97b696fd5bd43798916b4a0dbb0f64f"}
        url_current_season = 'https://api.sportsdata.io/v3/nba/scores/json/CurrentSeason'
        current_season_response = requests.get(url_current_season, headers=headers)
        current_season_data = json.loads(current_season_response.text)

        # set up variables for the current season
        return current_season_data['Season']
        
        

    
    
        
    @classmethod
    def import_past_two_seasons_data(cls):
        
        current_season_number = cls.get_current_season_number()
        past_season_number = current_season_number - 1
        
        current_season_object = Season(current_season_number)
        past_season_object = Season(past_season_number)
        

        cls.season_dict[current_season_number] = current_season_object
        cls.season_dict[past_season_number] = past_season_object
        
        
        current_season_team_standings = cls.get_team_standings_data(current_season_number)
        past_season_team_standings = cls.get_team_standings_data(past_season_number)
        
        current_season_object.add_team_standings(current_season_team_standings)
        past_season_object.add_team_standings(past_season_team_standings)
        
        
        
        
    @classmethod
    def import_team_data(cls):
        
        headers = {"Ocp-Apim-Subscription-Key" : "a97b696fd5bd43798916b4a0dbb0f64f"}
        teams_url = f"https://api.sportsdata.io/v3/nba/scores/json/teams"
        
        response = requests.get(teams_url,headers=headers)
        teams_data = json.loads(response.text)
        num_teams = len(teams_data)
        
        for teams in teams_data:
            team_key = teams['Key']
            team_object = Team(teams['TeamID'], team_key, teams['City'], teams['Name'], teams['LeagueID'], teams['StadiumID'], teams['Conference'], teams['Division'])
            cls.teams_dict[team_key] = team_object
        
        
    
    @classmethod
    def get_team_standings_data(cls, year):
        
        
        headers = {"Ocp-Apim-Subscription-Key" : "a97b696fd5bd43798916b4a0dbb0f64f"}
        standings_url = f"https://api.sportsdata.io/v3/nba/scores/json/Standings/{year}"
        
        response = requests.get(standings_url,headers=headers)
        standings_data = json.loads(response.text)
        num_teams = len(standings_data)
        teams = []
        
        
        for team in standings_data:
            
            key = str(team['TeamID']) + '_' + team['City'] + '_' + team['Name']
            team_object = Team_Standing(key, team['Season'], team['TeamID'], team['Key'], team['City'], team['Name'], team['Conference'], team['Division'],
            team['Wins'], team['Losses'], team['HomeWins'], team['HomeLosses'], team['AwayWins'], team['AwayLosses'], team['Percentage'], team['PointsPerGameFor'], team['PointsPerGameAgainst'], team['StreakDescription'])
            
            teams.append(team_object)
            
        
        print(f"All {num_teams} active NBA team standings from {year} have being loaded into the program.")
        
        return teams
    
            
        
    @classmethod
    def search_player_data(cls): 
        
        # player dict has key: player name
        

        while True:
            
            print("Which player would you like to search for: ", end='')
            player_search = input()
            player_search_lower = player_search.lower()
            matches = 0
            match_name = ''
            print("\nSearching NBA player list for matching names.\n")
            
            
            matched_player = None
            for player_object in cls.players_dict.values():
                full_name = player_object.full_name
                full_name_lower = player_object.full_name.lower()
                if player_search_lower in full_name_lower:
                    matched_player = player_object
                    matches += 1
                    print("Matched player name: \t" + full_name)
                    
                    
            if matches == 1:
                print()
                return matched_player
            elif matches > 1:
                print(f"\nThere are {matches} names in total that match your search. Please type in their full name so we can find the exact player you are looking for.")
            else:
                print(f"\nWe could not find any names which matched {player_search}. Please try again.")
                
                
                
        
        
        

        
        
        
            
            
        
    
    @staticmethod
    def get_date():
        
        pass
        # while True:
        #     try:
        #         print("For the statistics, let's enter the date.")
                
        #         day = int(input('Enter the day: '))
        #         month = int(input('Enter the month: '))
        #         year = int(input('Enter the year: '))
               
        #         birthday = datetime.datetime(year, month, day)
        #         valid_date = True # we only get here if month and day are integers
        #         return birthday.strftime("%Y-%b-%d").upper()
                
        #     except ValueError as e:
        #         print("Error: " + str(e) + "\nPlease try again!")
                
            
        
        