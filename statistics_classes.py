from datetime import datetime
from relativedate import relativedelta

# Split classes up into one class per file
# Run Flake8
# Do type hints and annotations - methods and function for sure!
# TESTS!!!!!!!!

class Player():
    
    
    def __init__(self, player_id, first_name, last_name, team_ID, team_name, jersey, position, birthday, birth_city, birth_state, college, experience, salary, height, weight):
        
        self._player_id = player_id
        self._first_name = first_name
        self._last_name = last_name
        self._team_ID = team_ID
        self._team_name = team_name
        if jersey != None:
            self._raw_jersey = jersey
            self._jersey = jersey
        else:
            self._raw_jersey = -1
            self._jersey = 'N/A'
        self._position = position
        
        if birthday != None:


            date_of_birth = datetime.fromisoformat(birthday)
            self._birthday = date_of_birth.strftime("%d/%m/%Y")
            date_now = datetime.now()
            difference_in_time = relativedelta(date_now, date_of_birth)
            self._raw_age = difference_in_time.years
            self._age = difference_in_time.years
        else:
            self._birthday = 'N/A'
            self._age = 'N/A'
            self._raw_age = 0
        
        
        if birth_city != None:
            self._birth_city = birth_city
        else:
            self._birth_city = "N/A"
        
        if birth_state != None:
            self._birth_state = birth_state
        else:
            self._birth_state = "N/A"
        
        if college != None:
            self._college = college
        else:
            self._college = "N/A"
        
        self._experience = experience + 2 # not sure why but the API experience value is 2 less than actual experience
        if salary != None:
            self._raw_salary = salary
            self._salary = "$" + "{:,}".format(salary)
        else: 
            self._salary = "N/A"
            self._raw_salary = 0
            
            
            
        self._height = float("{:.1f}".format(height * 2.54)) # convert to cm
        self._weight = float("{:.1f}".format(weight / 2.2 )) # convert to kg
        
    
    def set_team(self, team):
        self._team = team
    
    @property
    def raw_salary(self):
        return self._raw_salary
        
    def get_team_details(self):
        return self._team.details()
        
        
    def __repr__(self):
        return f"""{self.first_name} {self.last_name} of the {self._team} is {self._age} years old. 
His team plays in the {self._team.get_location()}.
He is {self._height}cm tall and weighs {self._weight}kg.
His salary is {self._salary} and he has been playing in the NBA for {self._experience} years.

Further player details:
{'{:<25}'.format("Birthday: " + self._birthday)}  {'{:<25}'.format("Birth City: " + self._birth_city)}  {'{:<25}'.format("Birth State: " + self._birth_state)} 
{'{:<25}'.format("College: " + self._college)}  {'{:<25}'.format("Position: " + self._position)}  {'{:<25}'.format("Jersey Number: " + str(self._jersey))}
"""
        
    @property
    def player_id(self):
        return self._player_id
    
    @property
    def first_name(self):
        return self._first_name
        
    @property
    def last_name(self):
        return self._last_name
        
    @property
    def full_name(self):
        return self._first_name + " " + self._last_name
        

    @property
    def team_ID(self):
        return self._team_ID
        
    @property
    def team_name(self):
        return self._team_name
        
    @property
    def jersey(self):
        return self._jersey
        
    @property
    def position(self):
        return self._position
        
    @property
    def birth_city(self):
        return self._birth_city
        
    @property
    def birth_state(self):
        return self._birth_state
        
    @property
    def college(self):
        return self._college
        
    @property
    def salary(self):
        return self._salary
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def height(self):
        return self._height
        
    @property
    def weight(self):
        return self._weight
        
    @property
    def age(self):
        return self._age
        
    
    @property
    def raw_age(self):
        return self._raw_age
        
    
    @property
    def raw_jersey(self):
        return self._raw_jersey
        
    
        
      
      
class Team():
    
    def __init__(self, teamID, key, city, name, leagueID, stadiumID, conference, division):
        self._key = key
        self._city = city
        self._name = name
        self._leagueID = leagueID
        self._stadiumID = stadiumID
        self._conference = conference
        self._division = division
        self._players = []
    

    def __repr__(self):
        return self._city + " " + self._name
        
        
    
    def reorder(self, column):
        column_name = column.lower()

        if column_name == "last name":
            self._players.sort(key=lambda x: x.last_name)
            self._ordering = 'last name'
            print('{:<25}'.format("Player name"))
            for player in self._players:
                print('{:<25}'.format(player.full_name))
            return True
            
        elif column_name == "jersey":
            self._players.sort(key=lambda x: x.raw_jersey, reverse=True)
            self._ordering = 'jersey'
            print('{:<25}'.format("Player name") + "Jersey")
            for player in self._players:
                print('{:<27}'.format(player.full_name) + str(player.jersey))
            return True
        elif column_name == "position":
            self._players.sort(key=lambda x: x.position, reverse=True)
            self._ordering = 'position'
            print('{:<25}'.format("Player name") + "Position")
            for player in self._players:
                print('{:<29}'.format(player.full_name) + player.position)
            return True
        elif column_name == "salary":
            self._players.sort(key=lambda x: x.raw_salary, reverse=True)
            self._ordering = 'salary'
            print('{:<25}'.format("Player name") + "Salary")
            for player in self._players:
                print('{:<25}'.format(player.full_name) + player.salary)
            return True
        elif column_name == "experience":
            self._players.sort(key=lambda x: x.experience, reverse=True)
            self._ordering = 'experience'
            print('{:<25}'.format("Player name") + "Experience (years)")
            for player in self._players:
                print('{:<32}'.format(player.full_name) + str(player.experience))
            return True
        elif column_name == "age":
            self._players.sort(key=lambda x: x.raw_age, reverse=True)
            self._ordering = 'age'
            print('{:<25}'.format("Player name") + "Age")
            for player in self._players:
                print('{:<25}'.format(player.full_name) + str(player.age))
            return True
        elif column_name == "weight":
            print('{:<25}'.format("Player name") + "Weight (kgs)")
            self._players.sort(key=lambda x: x.weight, reverse=True)
            self._ordering = 'weight'
            for player in self._players:
                print('{:<28}'.format(player.full_name) + str(player.weight))
            return True
        elif column_name == "height":
            print('{:<25}'.format("Player name") + "Height (cm)")
            self._players.sort(key=lambda x: x.height, reverse=True)
            self._ordering = 'height'
            for player in self._players:
                print('{:<28}'.format(player.full_name) + str(player.height))
            return True
        else:
            return False
        

        
            
    
        
    def add_player(self, player):
        if player not in self._players:
            self._players.append(player)
            self._players.sort(key=lambda x: x.last_name)
            self._ordering = 'last name'
            return True
        else:
            return False
    
            
            
    def print_player_names(self):
        print(f"\nThe current players of the {self.get_team_name()} team are:\n")
        # new line every 4 names
        count = 0
        for player in self._players:
            count += 1
            print('{:<25}'.format(player.full_name), end='')
            if count % 4 == 0:
                # new line
                print()
        print()
    
    def get_team_name(self):
        return self._city + " " + self._name
    
    def get_location(self):
        return self._conference + " conference and the " + self._division + " division"
             
    
    def details(self):
        return self._city + " " + self._name + " "
             
             
    @property
    def key(self):
        return self._key
        
        
    @property
    def ordering(self):
        return self._ordering


class Team_Standing():
    
    def __init__(self, key, season, teamID, abv_name, city, name, conference, division, total_wins, total_losses,
    home_wins, home_losses, away_wins, away_losses, percentage, points_per_game_for, points_per_game_against, streak_description,
    last_ten_wins, last_ten_losses):
        
        self._key = key; self._season = season; self._teamID = teamID; self._abv_name = abv_name; self._city = city
        self._name = name; self._conference = conference; self._division = division; self._total_wins = total_wins
        self._total_losses = total_losses; self._home_wins = home_wins; self._home_losses = home_losses
        self._away_wins = away_wins; self._away_losses = away_losses; self._percentage = percentage;
        self._points_per_game_for = points_per_game_for; self._points_per_game_against = points_per_game_against; self._streak_description = streak_description
        self._last_ten_wins = last_ten_wins; self._last_ten_losses = last_ten_losses
        
    def __repr__(self):
        return f"{self.city} {self.name}"

        
    @property
    def season(self):
        return self._season
        
    @property
    def total_wins(self):
        return self._total_wins
        
    @property
    def total_losses(self):
        return self._total_losses
        
    @property
    def home_wins(self):
        return self._home_wins
    
    @property
    def home_losses(self):
        return self._home_losses
        
    @property
    def away_wins(self):
        return self._away_wins
    
    @property
    def away_losses(self):
        return self._away_losses
        
    @property
    def percentage(self):
        return self._percentage

        
    @property
    def name(self):
        return self._name    
        
        
    @property
    def teamID(self):
        return self._teamID
        
    
    @property
    def key(self):
        return self._key
        
    @property
    def city(self):
        return self._city
    
    @property
    def conference(self):
        return self._conference
        
    @property
    def points_per_game_for(self):
        return self._points_per_game_for
    
    @property
    def points_per_game_against(self):
        return self._points_per_game_against
        
    @property
    def streak_description(self):
        return self._streak_description
        
    @property
    def last_ten_wins(self):
        return self._last_ten_wins
        
    @property
    def last_ten_losses(self):
        return self._last_ten_losses
        
        
    
class Season():
    
    @property
    def ordering(self):
        return self._ordering
    
    def reorder(self, column):
        column_name = column.lower()
        if column_name == "team city":
            self.reorder_by_city()
            self._ordering = 'team city'
            return True
        elif column_name == "w":
            self.reorder_by_total_wins()
            self._ordering = 'total wins'
            return True
        elif column_name == "team name":
            self.reorder_by_name()
            self._ordering = 'team name'
            return True
        elif column_name == "l":
            self.reorder_by_total_losses()
            self._ordering = 'total losses'
            return True
        elif column_name == "home":
            self.reorder_by_home_wins()
            self._ordering = 'home wins'
            return True
        elif column_name == "away":
            self.reorder_by_away_wins()
            self._ordering = 'away wins'
            return True
        elif column_name == "ppg":
            self.reorder_by_points_per_game_for()
            self._ordering = 'points per game for'
            return True
        elif column_name == "oop ppg":
            self.reorder_by_points_per_game_against()
            self._ordering = 'points per game against'
            return True
        elif column_name == "strk":
            self.reorder_by_streak_description()
            self._ordering = 'streak'
            return True
        elif column_name == "l10":
            self.reorder_by_last_ten_wins()
            self._ordering = 'last 10 games'
            return True
        else:
            return False
    

        
    
    def __init__(self, year):
        self._year = year
        self._name_season = str(year-1) + "/" + str(year)
    
    def reorder_by_total_wins(self):
        
        self._eastern_conference.sort(key=lambda x: x.total_wins, reverse=True)
        self._western_conference.sort(key=lambda x: x.total_wins, reverse=True)
        
    def reorder_by_total_losses(self):
        
        self._eastern_conference.sort(key=lambda x: x.total_losses, reverse=True)
        self._western_conference.sort(key=lambda x: x.total_losses, reverse=True)
    
    def reorder_by_city(self):
        
        self._eastern_conference.sort(key=lambda x: x.city, reverse=True)
        self._western_conference.sort(key=lambda x: x.city, reverse=True)
    
    def reorder_by_streak_description(self):
        
        self._eastern_conference.sort(key=lambda x: x.streak_description, reverse=True)
        self._western_conference.sort(key=lambda x: x.streak_description, reverse=True)
    
    
    def reorder_by_name(self):
        
        self._eastern_conference.sort(key=lambda x: x.name, reverse=True)
        self._western_conference.sort(key=lambda x: x.name, reverse=True)
        
    def reorder_by_home_wins(self):
        
        self._eastern_conference.sort(key=lambda x: x.home_wins, reverse=True)
        self._western_conference.sort(key=lambda x: x.home_wins, reverse=True)
        
    
    def reorder_by_away_wins(self):
        
        self._eastern_conference.sort(key=lambda x: x.away_wins, reverse=True)
        self._western_conference.sort(key=lambda x: x.away_wins, reverse=True)
        
    def reorder_by_percentage(self):
        
        self._eastern_conference.sort(key=lambda x: x.percentage, reverse=True)
        self._western_conference.sort(key=lambda x: x.percentage, reverse=True)
    
    def reorder_by_points_per_game_for(self):
        
        self._eastern_conference.sort(key=lambda x: x.points_per_game_for, reverse=True)
        self._western_conference.sort(key=lambda x: x.points_per_game_for, reverse=True)
        
    def reorder_by_points_per_game_against(self):
        
        self._eastern_conference.sort(key=lambda x: x.points_per_game_against, reverse=True)
        self._western_conference.sort(key=lambda x: x.points_per_game_against, reverse=True)
        
        
    def reorder_by_last_ten_wins(self):
        
        self._eastern_conference.sort(key=lambda x: x.last_ten_wins, reverse=True)
        self._western_conference.sort(key=lambda x: x.last_ten_wins, reverse=True)
    

    def add_team_standings(self, team_standings):
        self._eastern_conference = []
        self._western_conference = []
        for team_standing in team_standings:
            if team_standing.conference == "Eastern":
                self._eastern_conference.append(team_standing)
            else:
                self._western_conference.append(team_standing)
        
            
        self._eastern_conference.sort(key=lambda x: x.percentage, reverse=True)
        self._western_conference.sort(key=lambda x: x.percentage, reverse=True)
        self._ordering = 'percentage'
        
        
    def get_standings(self):
        print(f"\nFor the {self._name_season} season the standings were as follows\n")
        
        print(" Eastern Conference")
        print("=" * 100)
        print(f" {'{:<15}'.format('Team City')}  {'{:<15}'.format('Team Name')}" + '   W    L   PCT    Home   Away    PPG    OPP PPG    STRK    L10')
        print("=" * 100)
        
        for team_standing in self._eastern_conference:
            print(f" {'{:<15}'.format(team_standing.city)}  {'{:<15}'.format(team_standing.name)}  {team_standing.total_wins}   {team_standing.total_losses}  \
{'{:<5}'.format(team_standing.percentage)}  {'{:>5}'.format(str(team_standing.home_wins) + '-' + str(team_standing.home_losses))}  \
{'{:>5}'.format(str(team_standing.away_wins) + '-' + str(team_standing.away_losses))}  {'{:<7}'.format(team_standing.points_per_game_for)}   \
{'{:<7}'.format(team_standing.points_per_game_against)}    {'{:<2}'.format(team_standing.streak_description)}   {'{:>5}'.format(str(team_standing.last_ten_wins) + '-' + str(team_standing.last_ten_losses))}") 
               
        
        
        print("\n Western Conference")
        print("=" * 100)
        print(f" {'{:<15}'.format('Team City')}  {'{:<15}'.format('Team Name')}" + '   W    L   PCT    Home   Away    PPG    OPP PPG    STRK    L10')
        print("=" * 100)
        
        for team_standing in self._western_conference:
            print(f" {'{:<15}'.format(team_standing.city)}  {'{:<15}'.format(team_standing.name)}  {team_standing.total_wins}   {team_standing.total_losses}  \
{'{:<5}'.format(team_standing.percentage)}  {'{:>5}'.format(str(team_standing.home_wins) + '-' + str(team_standing.home_losses))}  \
{'{:>5}'.format(str(team_standing.away_wins) + '-' + str(team_standing.away_losses))}  {'{:<7}'.format(team_standing.points_per_game_for)}   \
{'{:<7}'.format(team_standing.points_per_game_against)}    {'{:<2}'.format(team_standing.streak_description)}   {'{:>5}'.format(str(team_standing.last_ten_wins) + '-' + str(team_standing.last_ten_losses))}")
            
        
    def __repr__(self):
        return "Season" + self._year
    
    
    @property
    def year(self):
        return self._year
        
        
    
    