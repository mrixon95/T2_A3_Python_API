class Season():

    @property
    def ordering(self):
        return self._ordering

    def reorder(self, column: str):
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
        elif column_name == "pct":
            self.reorder_by_percentage()
            self._ordering = 'percentage'
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
        self._name_season = str(year - 1) + "/" + str(year)
        
        

    def reorder_by_total_wins(self):

        self._eastern_conference.sort(key=lambda x: x.total_wins, reverse=True)
        self._western_conference.sort(key=lambda x: x.total_wins, reverse=True)

    def reorder_by_total_losses(self):

        self._eastern_conference.sort(
            key=lambda x: x.total_losses, reverse=True)
        self._western_conference.sort(
            key=lambda x: x.total_losses, reverse=True)

    def reorder_by_city(self):

        self._eastern_conference.sort(key=lambda x: x.city, reverse=True)
        self._western_conference.sort(key=lambda x: x.city, reverse=True)

    def reorder_by_streak_description(self):

        self._eastern_conference.sort(
            key=lambda x: x.streak_description, reverse=True)
        self._western_conference.sort(
            key=lambda x: x.streak_description, reverse=True)

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

        self._eastern_conference.sort(key=lambda x: x.pct, reverse=True)
        self._western_conference.sort(key=lambda x: x.pct, reverse=True)

    def reorder_by_points_per_game_for(self):

        self._eastern_conference.sort(
            key=lambda x: x.points_per_game_for, reverse=True)
        self._western_conference.sort(
            key=lambda x: x.points_per_game_for, reverse=True)

    def reorder_by_points_per_game_against(self):

        self._eastern_conference.sort(
            key=lambda x: x.points_per_game_against, reverse=True)
        self._western_conference.sort(
            key=lambda x: x.points_per_game_against, reverse=True)

    def reorder_by_last_ten_wins(self):

        self._eastern_conference.sort(
            key=lambda x: x.last_ten_wins, reverse=True)
        self._western_conference.sort(
            key=lambda x: x.last_ten_wins, reverse=True)

    def add_team_standings(self, team_standings: list):
        self._eastern_conference = []
        self._western_conference = []
        for team_standing in team_standings:
            if team_standing.conference == "Eastern":
                self._eastern_conference.append(team_standing)
            else:
                self._western_conference.append(team_standing)

        self._eastern_conference.sort(key=lambda x: x.pct, reverse=True)
        self._western_conference.sort(key=lambda x: x.pct, reverse=True)
        self._ordering = 'percentage'

    def get_standings(self):
        print(
            f"\nFor the {self._name_season} season the standings were as"
            + " follows\n")

        print(" Eastern Conference")
        print("=" * 100)
        print(
            f" {'{:<15}'.format('Team City')}  {'{:<15}'.format('Team Name')}"
            + '   W    L    PCT     Home    Away   PPG    OPP PPG    STRK    L10'
        )
        print("=" * 100)

        for team in self._eastern_conference:

            print(  f" {'{:<17}'.format(team.city)}"
                    f"{'{:<17}'.format(team.name)}"
                    f"{team.total_wins}   "
                    f"{team.total_losses}   {'{:<9}'.format(team.pct)}"
                    f"{'{:<7}'.format(team.home_record)}"
                    f"{'{:<7}'.format(team.away_record)}"
                    f"{'{:<9}'.format(team.points_per_game_for)}"
                    f"{'{:<11}'.format(team.points_per_game_against)}"
                    f"{'{:<7}'.format(team.streak_description)}"
                    f"{'{:<7}'.format(team.last_ten_games)}"
            )

        print("\n Western Conference")
        print("=" * 100)
        print(
            f" {'{:<15}'.format('Team City')}  {'{:<15}'.format('Team Name')}"
            + '   W    L    PCT     Home    Away   PPG    OPP PPG    STRK    L10'
        )
        print("=" * 100)

        for team in self._western_conference:

            print(  f" {'{:<17}'.format(team.city)}"
                    f"{'{:<17}'.format(team.name)}"
                    f"{team.total_wins}   "
                    f"{team.total_losses}   {'{:<9}'.format(team.pct)}"
                    f"{'{:<7}'.format(team.home_record)}"
                    f"{'{:<7}'.format(team.away_record)}"
                    f"{'{:<9}'.format(team.points_per_game_for)}"
                    f"{'{:<11}'.format(team.points_per_game_against)}"
                    f"{'{:<7}'.format(team.streak_description)}"
                    f"{'{:<7}'.format(team.last_ten_games)}"
            )

    def __repr__(self):
        return "Season" + self._year

    @property
    def year(self):
        return self._year
