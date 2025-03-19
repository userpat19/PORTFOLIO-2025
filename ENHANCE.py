import random


class NumberGuessingGame:
    def __init__(self, lower=1, upper=100, attempt = 12): #ADDED NEW ATTRIBUTE(attempt limit)
        self.lower = lower
        self.upper = upper
        self.number = random.randint(self.lower, self.upper)
        self.guesses = 0
        self.attempt = attempt

    def guess(self, user_guess):

        if user_guess < self.lower or user_guess > self.upper: # feedback for the user if the input is not within the range(Attempt wont be counted)
            return "Guess out of range, attempt not counted" # return immediately to avoid incrementing guesses by 1
        
        
        self.guesses += 1

        if user_guess < self.number:
                return "Too low! 🔽"
        if user_guess > self.number:
                return "Too high! 🔼"
        
        return "Correct!"

def play_game(): #MAIN FUNCTION

    while True:
        #Added a difficulty settings in a form of dictionary, each key-value pair is a unique instance to be used depending on the user's choice of difficulty
        difficulties = {"1": NumberGuessingGame(upper=20), 
                        "2": NumberGuessingGame(upper=50, attempt=8),
                        "3": NumberGuessingGame(attempt=5)}
        print("***************************")
        print("*  SELECT GAME DIFFICULTY *")
        print("***************************")
        print("1.Easy")
        print("2.Medium")
        print("3.Hard")
        difficulty = input("Enter Difficulty:")
        game = difficulties.get(difficulty) #Making the object -> "game"
        if game:
            break #exit the loop if the value of game is not "None", otherwise it would keep on prompting the user to enter a valid choice
        print("Again invalid choice, valid choices: 1 | 2 | 3")
        print("\n")

    print("******************************************")
    print(f"  --Guess the number between {game.lower} and {game.upper}--")
    print(f"   --NOTE: You have only {game.attempt} attempts--")
    print("*******************************************")
    while True:
        try:
            user_input = int(input("Enter your guess: "))
            result = game.guess(user_input)
            if result == "Correct!":
                print(f"CORRECT ✅, you guessed it in {game.guesses} attempt/s.")
                # Added a feedback feature intended for the user if he/she won the game
                if game.guesses <= 3:
                    print("WOW VERY GOOD!!!")
                elif game.guesses <= 7:
                    print("COULD'VE GUESS FASTER")
                else:
                    print("TRY HARDER NEXT TIME")

                play_again() #invoked the play_again function after the user won the game



            else:
                if game.guesses < game.attempt:
                    print(result)
                    #Added a attempt tracker
                    print("******************************************")
                    print(f"      --You have {game.attempt - game.guesses} attempt/s left--")
                    print("******************************************")
                else:
                    print("No more Attempts left, You lose!")
                    print(f"--The correct number was {game.number}--") #shows the correct random number if no more attempts left
                    play_again() #invoked the play_again function after the user lost the game
                    break
        except ValueError:
            print("Please enter a valid integer.")



def play_again():
    
   if input("Play Again(Y/N):").strip().upper() == "Y":
      play_game()

   print("************************")
   print(" THANK YOU FOR PLAYING")
   print("************************")


        
play_game()
