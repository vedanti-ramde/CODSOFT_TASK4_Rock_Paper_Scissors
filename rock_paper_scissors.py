import random
user_score = 0
computer_score = 0
draw_score = 0
while True:
    print("\n===== ROCK PAPER SCISSORS GAME =====")
    print("1. Play Game")
    print("2. View Score")
    print("3. Reset Score")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":

        print("\nChoose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = input("Enter your choice (1-3): ")

        if user_choice == "1":
            user = "Rock"
        elif user_choice == "2":
            user = "Paper"
        elif user_choice == "3":
            user = "Scissors"
        else:
            print("Invalid Choice!")
            continue

        computer = random.choice(["Rock", "Paper", "Scissors"])

        print("\nYour Choice     :", user)
        print("Computer Choice :", computer)

        if user == computer:
            print("\nIt's a Tie!")
            draw_score += 1

        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):

            print("\nCongratulations! You Win!")
            user_score += 1

        else:
            print("\nComputer Wins!")
            computer_score += 1

        while True:
            play_again = input("\nDo you want to play again? (Y/N): ")

            if play_again.upper() == "Y":
                break

            elif play_again.upper() == "N":
                break

            else:
                print("Invalid Choice!")

        if play_again.upper() == "N":
            continue

    elif choice == "2":

        print("\n===== SCORE BOARD =====")
        print("User Score     :", user_score)
        print("Computer Score :", computer_score)
        print("Draws          :", draw_score)

    elif choice == "3":

        user_score = 0
        computer_score = 0
        draw_score = 0

        print("\nScores Reset Successfully!")

    elif choice == "4":

        print("\nThank you for playing!")
        break

    else:
        print("Invalid Choice! Please enter 1-4.")