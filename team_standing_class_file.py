class Team_Standing():

    def __init__(
            self,
            key: str,
            season: int,
            teamID: int,
            abv_name: str,
            city: str,
            name: str,
            conference: str,
            division: str,
            total_wins: int,
            total_losses: int,
            home_wins: int,
            home_losses: int,
            away_wins: int,
            away_losses: int,
            percentage: float,
            points_per_game_for: float,
            points_per_game_against: float,
            streak_description: str,
            last_ten_wins: int,
            last_ten_losses: int):

        self._key = key
        self._season = season
        self._teamID = teamID
        self._abv_name = abv_name
        self._city = city
        self._name = name
        self._conference = conference
        self._division = division
        self._total_wins = total_wins
        self._total_losses = total_losses
        self._home_wins = home_wins
        self._home_losses = home_losses
        self._away_wins = away_wins
        self._away_losses = away_losses
        self._pct = percentage
        self._points_per_game_for = points_per_game_for
        self._points_per_game_against = points_per_game_against
        self._streak_description = streak_description
        self._last_ten_wins = last_ten_wins
        self._last_ten_losses = last_ten_losses

    def __repr__(self):
        return f"{self.city} {self.name}"

    @property
    def home_record(self):
        return f"{self._home_wins}-{self._home_losses}"

    @property
    def away_record(self):
        return f"{self._away_wins}-{self._away_losses}"

    @property
    def last_ten_games(self):
        return f"{self._last_ten_wins}-{self._last_ten_losses}"

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
    def pct(self):
        return self._pct

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
