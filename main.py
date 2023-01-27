import random

def rock_paper_scissors():
    print("Let's play Rock, Paper, Scissors!\n")

    r = "rock"
    p = "paper"
    s = "scissors"
    all_choices = (r, p, s)

    user = input(f"Enter a choice ({r}, {p}, {s}): ")

    if user not in all_choices:
        print("Invalid choice. Try again.")
        return
    
    computer = random.choice(all_choices)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    # r>s, s>p, p>r
    if user == computer:
        print("Tie!\n")
    elif (user == r and computer == s) or (user == s and computer == p) or (user == p and computer == r):
        print("You win!\n")
    else:
        print("You lose!\n")

if __name__ == "__main__":
    rock_paper_scissors()