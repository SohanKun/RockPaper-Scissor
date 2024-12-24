print("     WELCOM TO ROCK-PAPER-SCISSORS GAME ")
import random
def gamewin(comp,user):
    if comp == user:
        return None
    elif comp == 'r':   
        if user == 's':
            return False
        elif user == 'p':
            return True
    elif comp == 'p':
        if user == 'r':
            return False
        elif user == 's':
            return True
    elif comp == 's':
        if user == 'p':
            return False
        if user == 'r':
            return True
while True:
    print("computer has taken an option")
    randNo = random.randint(1,3)
    if randNo == 1:
        comp = 'r'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 's'
    user = input("What is your option rock(r), paper(P) (or) scissor(s)? : ")
    a = gamewin(comp,user)
    print(f"comp chose :{comp}")
    print(f"you chose : {user}")

    if a == None:
        print("the game has been tie!")
    elif a:
        print("you win the game!")
    else:
        print("you lose the game!")
    play_again=input("Do you want to play again? (y/n) : ").strip().lower()
    if play_again!="y":
        break
print("Thanks for playing")
