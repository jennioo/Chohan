import random 

def load_balance():
    try:
        with open("chohad_balance.txt", "r") as file:
            balance = int(file.read())
            return balance

    except FileNotFoundError:
        print("Staring a new game with the balance of 10000")
        return 10000

    except ValueError:
        print("Error reading your balance file. Staring with the balance of 10000 ")
        return 10000



def save_balance(balance):
    with open("chohad_balance.txt", "w") as file:
        file.write(str(balance))
    print(f"Balance saved:{balance}")    
       


def main():
    balance = load_balance()
    while True:
        dice = random.randint(1,6)

        print("Welcome to the CHOHAD game ")
        print(f"Your current balance is {balance}")

        stake = int(input("How much do you want to stake:"))
        if stake > balance:
            print(f"You do not have enough money to stake\nYour current balance is {balance}\nGo and borrow haha")
            return

        user_choice =input("Which option will you choose?\n (C)ho or (H)ad:").lower()
        if user_choice =="c":
            print("You have chosen even (cho)")
            print("rolling the dice...")
            print (f"Your dice number is {dice}")

            if dice % 2 == 0:
                print("Yay you have won your stake")
                balance = stake + balance 
                print(f"You now have {balance}")


            else:
                print("Opps you have lost this round")
                balance = balance - 2000
                print(f"You now have {balance}")


        elif user_choice =="h":
            print("You have chosen odd (had)")
            print("rolling the dice...")
            print (f"Your dice number is {dice}")

            if not dice % 2 == 0:
                print("Yay you have won your stake")
                balance = stake + balance
                print(f"You now have {balance}")


            else:
                print("Opps you have lost this round")
                balance= balance - 2000
                print(f"You now have {balance}")      

        else:
            print("You have inputed wrongly. Input 'c' or 'h'")
            continue

 
        while True:
            save_balance(balance)
            user_play = input("Do you want to (P)lay again or (E)xit: ").lower()
            if user_play == "p":
                main()
            elif user_play =="e":
                print ("Goodbye!")
                break
            else:
                print("Invalid choice, please enter P or E")


main()
