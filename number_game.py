import random

def main():
    n = int(input("Give the upper value: "))
    rando_number = random.randint(1,n)

    while True:
        try:
            inp = int(input("Put your guess: "))
            if inp == rando_number:
                print("Congrats 🎉! You guessed it right")
                break
            elif inp < rando_number:
                print("Oh You are close! A hint, Try a BIGGER number!")
            else:
                print("Oh You are close! A hint,Try a SMALLER number!")
        except ValueError:
            print("Invalid input! Enter an integer")


if __name__=="__main__":
    main()