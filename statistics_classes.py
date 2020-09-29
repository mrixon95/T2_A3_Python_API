from datetime import datetime
from relativedate import relativedelta


class Player():
    
    
    def __init__(self, player_id, first_name, last_name, team_ID, team_name, jersey, position, birthday, birth_city, birth_state, college, experience, salary, height, weight):
        
        self._player_id = player_id
        self._first_name = first_name
        self._last_name = last_name
        self._team_ID = team_ID
        self._team_name = team_name
        self._jersey = jersey
        self._position = position
        
        if birthday != None:


            self._birthday = birthday
            date_of_birth = datetime.fromisoformat(birthday)
            date_now = datetime.now()
            difference_in_time = relativedelta(date_now, date_of_birth)
            self._age = difference_in_time.years
        else:
            self._birthday = 'N/A'
            self._age = 'N/A'
        
        
        self._birth_city = birth_city
        self._birth_state = birth_state
        self._college = college
        self._experience = experience + 2 # not sure why but the API experience value is 2 less than actual experience
        if salary != None:
            self._salary = "$" + "{:,}".format(salary)
        else: 
            self._salary = "N/A"
            
            
            
        self._height = float("{:.1f}".format(height * 2.54)) # convert to cm
        self._weight = float("{:.1f}".format(weight / 2.2 )) # convert to kg
        
    
    def set_team(self, team):
        self._team = team
        
    def get_team_details(self):
        return self._team.details()
        
        
    def __repr__(self):
        return f"""{self.first_name} {self.last_name} of the {self._team} is {self._age} years old and plays in the {self._team.get_location()}.
He is {self._height}cm tall and weighs {self._weight}kg.
He salary is {self._salary} and he has been playing in the NBA for {self._experience} years.

Further player details:
Birt
        
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
        
    
        
      
      
class Team():
    
    def __init__(self, teamID, key, city, name, leagueID, stadiumID, conference, division):
        self._key = key
        self._city = city
        self._name = name
        self._leagueID = leagueID
        self._stadiumID = stadiumID
        self._conference = conference
        self._division = division
    

    def __repr__(self):
        return self._city + " " + self._name
    
    
    def get_location(self):
        return self._conference + " conference and the " + self._division + " division"
             
    
    def details(self):
        return self._city + " " + self._name + " "
             
             
    @property
    def key(self):
        return self._key
        
    


class Team_Standing():
    
    def __init__(self, key, season, teamID, abv_name, city, name, conference, division, total_wins, total_losses,
    home_wins, home_losses, away_wins, away_losses, percentage, points_per_game_for, points_per_game_against, streak_description):
        
        self._key = key; self._season = season; self._teamID = teamID; self._abv_name = abv_name; self._city = city
        self._name = name; self._conference = conference; self._division = division; self._total_wins = total_wins
        self._total_losses = total_losses; self._home_wins = home_wins; self._home_losses = home_losses
        self._away_wins = away_wins; self._away_losses = away_losses; self._percentage = percentage;
        self._points_per_game_for = points_per_game_for; self._points_per_game_against = points_per_game_against; self._streak_description = streak_description
        
        
    def __repr__(self):
        return "f{self.city} {self.name}"

        
    @property
    def season(self):
        return self._season
        
        
    @property
    def teamID(self):
        return self._teamID
        
    
    @property
    def key(self):
        return self._key
        
    @property
    def city(self):
        return self._city
        
        
    
class Season():
    
    
    def __init__(self, year):
        self._year = year

    
    def add_team_standings(self, team_standings):
        self._team_standings = team_standings
        
    def __repr__(self):
        return "Season" + self._year
    
    
    @property
    def year(self):
        return self._year
        
        
    
    