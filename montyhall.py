import random
#helps with stats shout out chatgpt
class MontyHallGame:
    def __init__(self):
        # Initialize game statistics
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.switch_wins = 0
        self.switch_losses = 0
        self.keep_wins = 0
        self.keep_losses = 0

    def start_game(self):
        # Start a new game
        self.games_played += 1
        doors = ['A', 'B', 'C']
        car_door = random.choice(doors)  # Randomly select the door with the car
        player_choice = self.get_player_choice(doors)  # Get the player's choice
        revealed_door = self.reveal_door(doors, car_door, player_choice)  # Reveal a door with a goat
        final_choice = self.get_final_choice(player_choice, revealed_door)  # Get the final choice after switching

        # Determine win/loss and update statistics
        if final_choice == car_door:
            print("Congratulations! You won the car!woooo!")
            self.games_won += 1
            if final_choice != player_choice:
                self.switch_wins += 1
            else:
                self.keep_wins += 1
        else:
            print("Sorry, you got a goat.")
            self.games_lost += 1
            if final_choice != player_choice:
                self.switch_losses += 1
            else:
                self.keep_losses += 1

    def get_player_choice(self, doors):
        # Get a valid door choice from the player
        while True:
            choice = input(f"Choose a door ({', '.join(doors)}): ").upper()
            if choice in doors:
                return choice
            print("Invalid choice. Please choose a valid door.")

    def reveal_door(self, doors, car_door, player_choice):
        # Reveal a door that has a goat behind it
        remaining_doors = [door for door in doors if door != player_choice and door != car_door]
        revealed_door = random.choice(remaining_doors)
        print(f"The host reveals a goat behind door {revealed_door}.")
        return revealed_door

    def get_final_choice(self, player_choice, revealed_door):
        # Determine whether to switch or stay
        while True:
            switch = input("Do you want to switch your choice? (yes/no): ").lower()
            if switch in ['yes', 'no']:
                if switch == 'yes':
                    return next(door for door in ['A', 'B', 'C'] if door != player_choice and door != revealed_door)
                return player_choice
            print("Invalid input. Please enter 'yes' or 'no'.")

    def view_statistics(self):
        # Display game statistics
        print("\n--- Game Statistics ---")
        print(f"Games Played: {self.games_played}")
        print(f"Games Won: {self.games_won}")
        print(f"Games Lost: {self.games_lost}")
        print(f"Games Played Switching: {self.switch_wins + self.switch_losses}")
        print(f"Games Won Switching: {self.switch_wins}")
        print(f"Games Lost Switching: {self.switch_losses}")
        print(f"Games Won Keeping: {self.keep_wins}")
        print(f"Games Lost Keeping: {self.keep_losses}")

        if (self.switch_wins + self.switch_losses) > 0:
           switch_win_percentage = (self.switch_wins / (self.switch_wins + self.switch_losses)) * 100
           print(f"Percentage of Wins Switching: {switch_win_percentage:.2f}%")
        else:
            print("Percentage of Wins Switching: No data available (no switching games played)")

        if (self.keep_wins + self.keep_losses) > 0:
            keep_win_percentage = (self.keep_wins / (self.keep_wins + self.keep_losses)) * 100
            print(f"Percentage of Wins Keeping: {keep_win_percentage:.2f}%")
        else:
            print("Percentage of Wins Keeping: No data available (no keeping games played)")

        print("-----------------------\n")

       
    def run(self):
        # Main game loop
        while True:
            print("Welcome to the Monty Hall Game!")
            print("[1] Start Game")
            print("[2] View Statistics")
            print("[3] Quit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.view_statistics()
            elif choice == '3':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    game = MontyHallGame()
    game.run()
