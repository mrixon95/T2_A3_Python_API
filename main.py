from data_handler import Data_Handler as dh

dh.import_team_data()
dh.import_player_data()
dh.import_past_two_seasons_data()


def menu():
    print("\nMain menu: \n\
1 - Search for the statistics of an active player in the NBA\n\
2 - View the team standings for the 2018/2019 season \n\
3 - View the team standings for the 2019/2020 season \n\
4 - View the current players of a particular team\n\
5 - View the current players from a particular state\n\
6 - Exit program\n"
          )


def get_team_members():

    team = dh.teams_info()
    team.print_player_names()

    while True:
        print(
            f"\nThe players are ordered by {team.ordering}. Would you like to\
            reorder the players by one of their other statistics? (Y/N): ")
        entry = input().lower()
        if entry == 'y':
            while True:
                print("Players can be reordered by:   \
Last name, Jersey, Position, Salary, Experience, Age, Weight, Height")

                print("Type in the name of the stat\
you would like to reorder by: ")
                stat = input().lower()
                if team.reorder(stat):
                    # reordered and printed successfully
                    break
                else:
                    print("Input is invalid. Try again.")

        elif entry == 'n':
            break
        else:
            print("Invalid input. Please try again.")


def get_players_from_particular_state():
    dh.players_from_state()


def order_standings(season_year):

    team_standings = dh.search_team_standings(season_year)
    team_standings.get_standings()
    while True:
        print(
            f"\nThe standings are ordered by {team_standings.ordering}.\
Would you like to reorder the standings by one of the\
other columns? (Y/N): ")
        entry = input().lower()
        if entry == 'y':
            while True:
                print("Type in the name of the column\
you would like to reorder by: ")
                column = input().lower()
                if team_standings.reorder(column):
                    team_standings.get_standings()
                    break
                else:
                    print("Input is invalid. Try again.")

        elif entry == 'n':
            break
        else:
            print("Invalid input. Please try again.")


quit = False
while not quit:

    menu()
    entry = None
    try:
        entry = int(input("Your input: "))
        if not 1 <= entry <= 6:
            print("Invalid input. Please enter an integer between 1 and 6")
            continue
        elif entry == 1:
            player = dh.search_player_data()
            print(player)

        elif entry == 2:
            order_standings(2019)

        elif entry == 3:
            order_standings(2020)

        elif entry == 4:
            get_team_members()

        elif entry == 5:
            get_players_from_particular_state()

        elif entry == 6:
            quit = True
            print("Exiting the program")

        else:
            print("Invalid input")

    except ValueError:
        print("Sorry your input was invalid. \
Please enter an integer between 1 and 6")
