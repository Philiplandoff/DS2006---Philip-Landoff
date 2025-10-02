import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

player1_rolls = []
player2_rolls = []
# Round 1
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)

# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 2
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 3
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 4
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 5
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 10
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 7
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 8
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)

# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 9
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

#round 10
input("\nPress ENTER to roll the dice..")
player1_roll = random.randint(1, 10)
print("Player 1 rolled: ", player1_roll)
player2_roll = random.randint(1, 10)
print("Player 2 rolled: ", player2_roll)

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!, he is on fire!")
    print("Because ", player1_roll," is greater than ", player2_roll)
    round_result = "Player 1 wins the round!"
    
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
    round_result = "It's a tie!"
    
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)
    round_result = "Player 2 wins the round!"
    
player1_rolls.append(player1_roll)
player2_rolls.append(player2_roll)
# we can print the game score:
print("The game score is Player 1:", player1_wins, "vs. Player 2:", player2_wins)



# Print who won the current round

print("Round result:", round_result)
input("\nPress ENTER to continue...")


# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the king of Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the king of Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

print("\n--- Game Summary ---")
for i in range(len(player1_rolls)):
    print(f"Round {i+1}: Player 1 rolled {player1_rolls[i]}, Player 2 rolled {player2_rolls[i]}")