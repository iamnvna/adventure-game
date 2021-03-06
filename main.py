print("Welcome to the Adventure Game!")

name = input("What is your name?: ")
age = input("What is your age?: ")

def game():
    health = 10
    
    def game_over():
        if health > 20:
            print("You won!"
                  f"\nYou have amassed {health} health.")
            quit()
        elif health > 0:
            print(f"You have {health} health left.")
        else:
            print("You lost all your health."
                  "\nGame over!")
            quit()
    
    print(f"You are starting with {health} health.")
    print("Let's begin!")
    left_or_right = input("First choice, left or right? (left/right): ")
    if left_or_right == "left":
        ans = input("Nice! You followed the path and reached a lake. Do you swim across "
                    "or go around? (across/around): ")
        if ans == "around":
            print("You went around and reached the other side of the lake.")
            print("You won!")
            quit()
        elif ans == "across":
            print("You managed to get across but were bit by a snake and lost 5 health.")
            health -= 5
            game_over()
            ans = input("You noticed a house and a farm, which do you go to? (house/farm): ")
            if ans == "house":
                print("You got shot for trespassing and lost 5 health")
                health -= 5
                print(f"You have {health} health left.")
                game_over()
            else:
                ans = input("You got through the farm and saw a mango and apple tree."
                            "\nWhich fruit are you plucking to gain health? (mango/apple): ")
                if ans == "mango":
                    print("You got 10 health!")
                    health += 10
                    game_over()
                    ans = input("You come across a wild animal finding your way out of the farm. "
                                "(fight/flight): ")
                    if ans == "fight":
                        print("You got bullied by the wild animal. You lost 10 health.")
                        health -= 10
                        game_over()
                        ans = input("You managed to escape. You are out of the farm. You see your "
                                    "crush. Are you approaching them? (yes/no): ")
                        if ans == "yes":
                            print("You limped helplessly to your crush, as you begin telling your story,"
                                  "you lose breath (5 health).")
                            health -= 5
                            game_over()
                        elif ans == "no":
                            print("Your heart is broken walking away and you lose 10 health")
                            health -= 10
                            game_over()
                        else:
                            print("You entered an invalid input."
                                  "\nBye!")
                    elif ans == "flight":
                        print("You run into a stomp and lost all your health.")
                        health -= health
                        game_over()
                    else:
                        print("You entered an invalid input."
                              "\nBye!")
                elif ans == "apple":
                    print("The apple is poisoned by a snake bite, you lost 5 health")
                    health -= 5
                    game_over()
                else:
                    print("You entered an invalid input."
                          "\nBye!")
                    quit()
        else:
            print("You lost!"
                  "\nBye!")
    elif left_or_right == "right":
        print("You fell down and lost 10 health")
        health -= 10
        game_over()
    else:
        print("You entered an invalid input"
              "\nBye!")


if int(age) >= 18:
    print("You are old enough to play.")
    play = input("Do you want to play? (yes/no): ").lower()
    if play == "yes":
        game()
    else:
        quit()
elif int(age) >= 14:
    print("You can play with supervision.")
    game()
else:
    print("Sorry, you have to be 18+ to play."
          "\nBye!")
    quit()


# Commentary
'''
Line 1:
    Line 1 is a print statement that welcomes users to the game.

Line 3-4:
    Line 3 and 4 collects the name and age of the user respectively and assigns them
    to variables. The age variable is evaluated using if else statements to allow the
    user play if they above 18 years old.

Line 6-92:
    Line 9-19:
        This block of code is a function that evaluates if a user has exhausted their
        total health in which case they have lost the game, or they still have health
        value greater than 0. This function is called several times in the main game
        code to evaluate how much health the user has after every action or if they've
        lost all their health. The code quits the program if the user has health less
        than or equal to 0.
        
    This block of code is a function that holds the code to the actual game. The code
    is a series of if else statements that evaluate based of the user input. Due to the
    volume of if else statements in this block, I will pass on explaining what each line
    does. But reading through carefully gives you a fair idea of the game structure.
    
Line 95-108:
    This block of code although is after the main game() function evaluates before the
    code runs. The code evaluates the user age collected from line 4 above and if they are
    above 18 years, the code calls the game function and the user is allowed to play the
    game. They can play with supervision if they are above 14 years or they can't play at
    all.
'''