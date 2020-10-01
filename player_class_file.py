from datetime import datetime
from relativedate import relativedelta


class Player():

    def __init__(
            self,
            player_id: int,
            first_name: str,
            last_name: str,
            team_ID: int,
            team_name: str,
            jersey,
            position: str,
            birthday: str,
            birth_city: str,
            birth_state: str,
            college: str,
            experience: int,
            salary: int,
            height: int,
            weight: int):

        self._player_id = player_id
        self._first_name = first_name
        self._last_name = last_name
        self._team_ID = team_ID
        self._team_name = team_name
        if jersey is not None:
            self._raw_jersey = jersey
            self._jersey = jersey
        else:
            self._raw_jersey = -1
            self._jersey = 'N/A'
        self._position = position

        if birthday is not None:

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

        if birth_city is not None:
            self._birth_city = birth_city
        else:
            self._birth_city = "N/A"

        if birth_state is not None:
            self._birth_state = birth_state
        else:
            self._birth_state = "N/A"

        if college is not None:
            self._college = college
        else:
            self._college = "N/A"

        # not sure why but the API experience value is 2 less than actual
        # experience
        self._experience = experience + 2
        if salary is not None:
            self._raw_salary = salary
            self._salary = "$" + "{:,}".format(salary)
        else:
            self._salary = "N/A"
            self._raw_salary = 0

        self._height = float("{:.1f}".format(height * 2.54))  # convert to cm
        self._weight = float("{:.1f}".format(weight / 2.2))  # convert to kg

    def set_team(self, team):
        self._team = team

    @property
    def raw_salary(self):
        return self._raw_salary

    def get_team_details(self):
        return self._team.details()

    def __repr__(self):
        return (f"{self.first_name} {self.last_name} of the {self._team}"
f" is {self._age} years old.\nHis team plays in both the {self._team.get_location()}."
f"\nHe is {self._height}cm tall and weighs {self._weight}kg."
f"\nHis salary is {self._salary} and he has been playing in"
f" the NBA for {self._experience} years.\n"

"\nFurther player details:\n"
'{:<40}'.format("\nBirthday: " + self._birthday)
+ '{:<40}'.format("Birth City: " + self._birth_city)
+ '{:<40}'.format("\nBirth State: " + self._birth_state)
+ '{:<40}'.format("College: " + self._college)
+ '{:<40}'.format("\nPosition: " + self._position)
+ '{:<40}'.format("Jersey Number: " + str(self._jersey)))

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
