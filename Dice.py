'''Create a simple Python program that simulates rolling dice. Users can specify the
number of sides on the dice and the number of rolls.
● The program generates random numbers for each roll and displays the results.
● It's a quick and fun way to emulate the experience of rolling dice, commonly used
in board games or tabletop role-playing games.
● The simulator allows users to explore the outcomes of dice rolls without the
physical dice.'''

import random

def roll_dice(num_sides, num_rolls):
    results = []
    for _ in range(num_rolls):
        roll_result = random.randint(1, num_sides)
        results.append(roll_result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            num_rolls = int(input("Enter the number of rolls: "))
            
            if num_sides <= 0 or num_rolls <= 0:
                print("Please enter positive numbers for sides and rolls.")
                continue
            
            # Roll the dice
            dice_rolls = roll_dice(num_sides, num_rolls)
            
            # Display results
            print(f"\nResults of rolling a {num_sides}-sided dice {num_rolls} times:")
            for i, result in enumerate(dice_rolls, start=1):
                print(f"Roll {i}: {result}")
            
            play_again = input("\nDo you want to roll again? (yes/no): ").lower()
            if play_again != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Thank you for using the Dice Rolling Simulator!")

if __name__ == "__main__":
    main()