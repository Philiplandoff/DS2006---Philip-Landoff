import random
print("🎲 Welcome to Battle of Dices! 🎲")

class Dice:
    def rollD6(self):
        return random.randint(1, 6)
    def rollD10(self):
        return random.randint(1, 10)
    
dice = Dice()
rounds = 0
# numbers of wins needed to win the game
winning_score = 3

# array for storing the names of the players
player_names = []

# array for storing the numbers of wins for each player
player_wins = []

#obtain the number of players:
number_of_players = int(input("how many players?"))

# for loop to obtain the player names: 
for i in range(number_of_players):
    name = input(f"what is the name of player {i + 1}?")
    player_names.append(name)

# initialize scores and rolls
for i in range(number_of_players):
    player_wins.append(0)

# initialize player rolls as empty lists for each player
player_rolls_history = [] # This will be a nested list
for i in range(number_of_players):
    # Add an empty list for each player
    player_rolls_history.append([])

# Repeats until the game is over. as many rounds as needed

gameover = False
while gameover is False:
    print(f"Round {rounds+1}:")

    # Dice roll for each player in the current round:
    current_rolls = []

    # We need to roll the dice for each player:
    for i in range(number_of_players):
        roll1 = dice.rollD6()
        roll2 = dice.rollD10()
        total_rolls = roll1 + roll2
        current_rolls.append(total_rolls)
        player_rolls_history[i].append(total_rolls)  # Store the roll in the player's history
        print(f"{player_names[i]} rolled a {roll1} and {roll2}, the total is {total_rolls}")


    # Obtain the highest roll this round:
    max_roll = max(current_rolls)

    # Winners will store information about who won this round
    winners = []

    # Search for all players who rolled the highest number
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    
    # Print the results of this round:
    print(f"Winners of this round are: {winners} with a roll of {max_roll}")
    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print("\nGame Over!")
            print(f"{player_names[z]} is the new Battle of Dices Champion!")
            gameover = True
    if gameover is False:
        print("Current scores:")
        for k in range(number_of_players):
            print(f"{player_names[k]}: {player_wins[k]} wins")
        rounds += 1
        input("\nPress ENTER to continue to the next round...")

# After the game is over, print the rolls history for each player
print("\nGame Over! Here are the rolls history for each player:")
for i in range(number_of_players):
    print(f"{player_names[i]}'s rolls: {player_rolls_history[i]}")

# Ask if the user wants to save the game history to a file
save_history = input("Do you want to save the game history to a file? (yes/no): ")
if save_history == "yes":
    filename = input("Enter the filename to save the history: ")
    with open(filename, "w") as file:
        for round_number in range(rounds):
            file.write (f"Round {round_number + 1}:\n")
            rolls_str = ""
            for i in range(number_of_players):
                rolls_str += (f"{player_names[i]} rolled {player_rolls_history[i][round_number]}")
                if i < number_of_players - 1:
                    rolls_str += ", "
            print(f"{rolls_str}")
            file.write(rolls_str + "\n")
            print(f"Game history saved to {filename}")