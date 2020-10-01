from typing import Dict
import requests
import json
from team_class_file import Team
from player_class_file import Player
from season_class_file import Season
from team_standing_class_file import Team_Standing


class Data_Handler():

    season_dict: Dict[int, Season] = {}
    players_dict: Dict[str, Player] = {}
    teams_dict: Dict[str, Player] = {}

    @classmethod
    def get_team(cls, team_key: str):
        team = cls.teams_dict.get(team_key)

        if team is not None:
            return team
        else:
            print(f"There is no team with {team_key} as their key")

    @classmethod
    def players_from_state(cls):

        while True:

            print("Which state do you want players from: ")
            state = input()
            state_lower = state.lower()
            count = 0
            for player in cls.players_dict.values():
                if player.birth_state.lower() == state_lower:
                    print()
                    print(player)
                    count += 1

            print(
                f"\nThere are {count} active NBA players "
                + "from the state of {state}\n")
            break

    @classmethod
    def teams_info(cls):

        while True:

            print("Which team would you like to choose: ", end='')
            team_search = input()
            team_search_lower = team_search.lower()
            matches = 0
            print("\nSearching NBA team list for matching names.\n")

            matched_team = None
            for team_object in cls.teams_dict.values():
                team_name = team_object.get_team_name()
                team_name_lower = team_name.lower()
                if team_search_lower in team_name_lower:
                    matched_team = team_object
                    matches += 1
                    print("Matched team name: \t" + team_name)

            if matches == 1:
                print()
                return matched_team
            elif matches > 1:
                print(
                    f"\nThere are {matches} team names in total that match "
                    "your search. Please type in their full name so we "
                    "can find the exact team you are looking for.")
            else:
                print(
                    "We could not find any team names which matched "
                    + f"{team_search}. Please try again.")

    @classmethod
    def import_player_data(cls):

        url = "https://api.sportsdata.io/v3/nba/scores/json/Players"

        headers = {
            "Ocp-Apim-Subscription-Key": "a97b696fd5bd43798916b4a0dbb0f64f"}

        response = requests.get(url, headers=headers)
        players_data = json.loads(response.text)
        total_players = len(players_data)

        for player in players_data:

            key = str(player['PlayerID']) + '_' + player['FirstName'] + \
                '_' + player['LastName'] + '_' + str(player['TeamID'])
            player_object = Player(
                player['PlayerID'],
                player['FirstName'],
                player['LastName'],
                player['TeamID'],
                player['Team'],
                player['Jersey'],
                player['Position'],
                player['BirthDate'],
                player['BirthCity'],
                player['BirthState'],
                player['College'],
                player['Experience'],
                player['Salary'],
                player['Height'],
                player['Weight'])

            team_object = cls.teams_dict.get(player['Team'])

            player_object.set_team(team_object)
            if not team_object.add_player(player_object):
                raise ValueError

            cls.players_dict[key] = player_object

        print(f"All {total_players} active NBA players have been loaded")

    @staticmethod
    def get_current_season_number():

        headers = {
            "Ocp-Apim-Subscription-Key": "a97b696fd5bd43798916b4a0dbb0f64f"}
        url_current_season = "https://api.sportsdata.io/v3/nba/scores/"
        url_current_season += "json/CurrentSeason"
        current_season_response = requests.get(
            url_current_season, headers=headers)
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

        current_season_team_standings = cls.get_team_standings_data(
            current_season_number)
        past_season_team_standings = cls.get_team_standings_data(
            past_season_number)

        current_season_object.add_team_standings(current_season_team_standings)
        past_season_object.add_team_standings(past_season_team_standings)

    @classmethod
    def import_team_data(cls):

        headers = {
            "Ocp-Apim-Subscription-Key": "a97b696fd5bd43798916b4a0dbb0f64f"}
        teams_url = "https://api.sportsdata.io/v3/nba/scores/json/teams"

        response = requests.get(teams_url, headers=headers)
        teams_data = json.loads(response.text)

        for teams in teams_data:
            team_key = teams['Key']
            team_object = Team(
                teams['TeamID'],
                team_key,
                teams['City'],
                teams['Name'],
                teams['LeagueID'],
                teams['StadiumID'],
                teams['Conference'],
                teams['Division'])
            cls.teams_dict[team_key] = team_object

    @classmethod
    def get_team_standings_data(cls, year: int):

        headers = {
            "Ocp-Apim-Subscription-Key": "a97b696fd5bd43798916b4a0dbb0f64f"}
        standings_url = "https://api.sportsdata.io/v3/nba/scores/json/"
        standings_url += f"Standings/{year}"

        response = requests.get(standings_url, headers=headers)
        standings_data = json.loads(response.text)
        num_teams = len(standings_data)
        teams = []

        for team in standings_data:

            key = str(team['TeamID']) + '_' + team['City'] + '_' + team['Name']
            team_object = Team_Standing(
                key,
                team['Season'],
                team['TeamID'],
                team['Key'],
                team['City'],
                team['Name'],
                team['Conference'],
                team['Division'],
                team['Wins'],
                team['Losses'],
                team['HomeWins'],
                team['HomeLosses'],
                team['AwayWins'],
                team['AwayLosses'],
                team['Percentage'],
                team['PointsPerGameFor'],
                team['PointsPerGameAgainst'],
                team['StreakDescription'],
                team['LastTenWins'],
                team['LastTenLosses'])

            teams.append(team_object)

        print(
            f"All {num_teams} active NBA team standings from "
            f"{year} have being loaded into the program.")

        return teams

    @classmethod
    def search_team_standings(cls, year: int):

        # player dict has key: player name
        if year in cls.season_dict.keys():
            return cls.season_dict.get(year)
        else:
            print(f"The year {year} standings data is unavailable")
            return None

    @classmethod
    def search_player_data(cls):

        # player dict has key: player name

        while True:

            print("Which player would you like to search for: ", end='')
            player_search = input()
            player_search_lower = player_search.lower()
            matches = 0
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
                print(
                    f"\nThere are {matches} names in total that match "
                    "your search. Please type in their full name so \
                    we can find the exact player you are looking for.")
            else:
                print(
                    "We could not find any names which matched"
                    f"{player_search}"
                    "Please try again.")
