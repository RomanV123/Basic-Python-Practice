import random

def play_game():
    number = random.randint(1, 20)
    attempts = 5

    print("\n🎯 Guess the number between 1 and 20")
    print(f"You have {attempts} attempts.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number:
            print("🎉 Correct guess!")
            print(f"You had {attempts} attempts left.")
            return True
        else:
            print("Wrong guess.")
            if guess < number:
                print("Hint: Too low.")
            else:
                print("Hint: Too high.")
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

    print(f"❌ You're out of attempts. The number was {number}.")
    return False


def main():
    wins = 0
    losses = 0

    while True:
        if play_game():
            wins += 1
        else:
            losses += 1

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            break

    print(f"\n🧾 Game Over — Wins: {wins}, Losses: {losses}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()