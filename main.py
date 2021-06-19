import random as r

#Making class for game
class RockPaperScissors:
    #CONSTANT
    CHOICES = ['rock', 'paper', 'scissors']

    #game method
    def game(self):
        while True:
            print("\nPlease choose from the following options:\n")
            print("r = Rock\np = Paper\ns = Scissors\n")
            user_input = input()
            computer_input = r.choice(self.CHOICES)
            if user_input.lower() == 'r' and computer_input == 'rock':
                print('Your opponent chose Rock!\nYou tied!!\n')
                break
            elif user_input.lower() == 'p' and computer_input == 'paper':
                print('Your opponent chose Paper!\nYou tied!!\n')
                break
            elif user_input.lower() == 's' and computer_input == 'scissors':
                print('Your opponent chose Scissors!\nYou tied!!\n')
                break
            elif user_input.lower() == 'r' and computer_input == 'paper':
                print('Your opponent chose Paper!\nYou lost!!\n')
                break
            elif user_input.lower() == 'r' and computer_input == 'scissors':
                print("Your opponent chose Scissors!\nYou won!!\n")
                break
            elif user_input.lower() == 'p' and computer_input == 'rock':
                print("Your opponent chose Rock!\nYou won!!\n")
                break
            elif user_input.lower() == 'p' and computer_input == 'scissors':
                print("Your opponent chose Scissors!\nYou lost!!\n")
                break
            elif user_input.lower() == 's' and computer_input == 'rock':
                print("Your opponent chose Rock!\nYou lost!!\n")
                break
            elif user_input.lower() == 's' and computer_input == 'paper':
                print("Your opponent chose Paper!\nYou won!!\n")
                break
            else:
                print("\nOopps! That's not valid input!\n")

#Initiate class
playing = RockPaperScissors()

#Run method for starting class
def run():
    while True:
        ask = input("Would you like to play Rock, Paper, Scissors?\nType 'y' for yes and 'n' to quit: ")
        if ask.lower() == 'y':
            playing.game()
        elif ask.lower() == 'n':
            break
        else:
            print("\nOpps, please try again!!\n")


#Calling run method
run()

#This was fun:)