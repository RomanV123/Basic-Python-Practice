
print("Welcome to rock, paper, scissors!")

input1 = input("Player 1, please enter your choice (rock, paper, or scissors): ").lower().strip()
input2 = input("Player 2, please enter your choice (rock, paper, or scissors): ").lower().strip()

if input1 == input2:
    print("It's a tie!")
elif input1 == "rock" and input2 == "scissors":
    print("Player 1 wins!")
elif input1 == "paper" and input2 == "rock":
    print("Player 1 wins!")
elif input1 == "scissors" and input2 == "paper":
    print("Player 1 wins!")
elif input2 == "rock" and input1 == "scissors":
    print("Player 2 wins!")
elif input2 == "paper" and input1 == "rock":
    print("Player 2 wins!")
elif input2 == "scissors" and input1 == "paper":
    print("Player 2 wins!")
    
