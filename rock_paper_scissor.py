import random

def main():
    list = ["rock","paper", "scissors"]
    n = int(input("Total points to win: "))
    ur_score = 0
    cpu_score = 0
    while (ur_score < n) and (cpu_score < n):
        try:
            inp = input("Your move(rock, paper or scissors): ").strip().lower()
            if inp not in list:
                print("Invalid input")
                continue
            ran = random.choice(list)
            if (inp == ran):
                print("It is a TIE in this round!")
            elif (inp == 'rock' and ran == 'scissors') or (inp == 'scissors' and ran == 'paper') or (inp == 'paper' and ran == 'rock'):
                print("You WIN the round!!🏆")
                ur_score += 1
            else:
                print("You LOSE in this round!!")
                cpu_score += 1
            print(f"Your Score: {ur_score} | CPU Score: {cpu_score}")
        except Exception as e:
            print(f"An error occurred: {e}")

    if ur_score > cpu_score:
        print("\nFinally You are the VICTOR!!🎉")
    elif ur_score < cpu_score:
        print("\nFinally CPU is the VICTOR!")
    else:
        print(("\nFinally It is a TIE"))



if __name__=="__main__":
    main()