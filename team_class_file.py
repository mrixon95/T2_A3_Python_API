from typing import List
from player_class_file import Player


class Team():

    def __init__(self, teamID: int, key: int, city: str, name: str,
                 leagueID: int, stadiumID: int, conference: str, division: str
                 ):
        self._key = key
        self._city = city
        self._name = name
        self._leagueID = leagueID
        self._stadiumID = stadiumID
        self._conference = conference
        self._division = division
        self._players: List[Player] = []

    def __repr__(self):
        return self._city + " " + self._name

    def reorder(self, column: str):
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
                print('{:<32}'.format(player.full_name) +
                      str(player.experience))
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
        print(
            f"\nThe current players of the {self.get_team_name()} team are:\n")
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
        return f"{self._conference} conference and the \
{self._division} division"

    def details(self):
        return self._city + " " + self._name + " "

    @property
    def key(self):
        return self._key

    @property
    def ordering(self):
        return self._ordering
