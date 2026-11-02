import random

while True:
    number = random.randint(1, 100)
    attempts = 5
    won = False

    print("\nNumber Guessing Game")
    print("I have chosen a number between 1 and 100.")
    print("You have 5 chances to guess it!")

    for i in range(1, attempts + 1):

        while True:
            print("\nAttempt", i, "of", attempts)
            print("Lives remaining:", attempts - i + 1)

            guess = input("Enter your guess: ").strip()

            if guess.isdigit():
                guess = int(guess)
            else:
                print("Error! Please enter a valid integer.")
                continue

            if guess < 1:
                print("The number must be between 1 and 100!")
                continue

            elif guess > 100:
                print("The number must be between 1 and 100!")
                continue

            break

        if guess == number:
            print("\nCongratulations! You guessed the number!")

            if i == 1:
                print("Rank: Excellent!")
            elif i == 2:
                print("Rank: Very Good!")
            elif i == 3:
                print("Rank: Good!")
            elif i == 4:
                print("Rank: Pass!")
            else:
                print("Rank: Lucky Win!")

            won = True
            break

        difference = abs(guess - number)

        if guess < number:
            print("Go higher!")
        else:
            print("Go lower!")

        if difference <= 5:
            print("Very close!")
        elif difference <= 15:
            print("Close, but you are still some distance away!")
        else:
            print("You are far away!")

    if won == False:
        print("\nYou have run out of chances!")
        print("The hidden number was", number)
        print("Unfortunately, you lost!")

    while True:
        again = input(
            "\nDo you want to play again? (yes/no): "
        ).strip().lower()

        if again in ["yes", "y"]:
            break
        elif again in ["no", "n"]:
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            print("Please enter yes or no.")
