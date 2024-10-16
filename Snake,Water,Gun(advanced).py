import random
import win32com.client as win
import time

speaker=win.Dispatch("SAPI.SpVoice")

def game():
    p1 = 0
    p2 = 0
    while True:
        print("Enter '1' for SNAKE\nEnter '2' for WATER\nEnter '3' for GUN\nEnter '4' to QUIT\nEnter '5' to SEE SCORE\n")

        user = input("Enter your choice: ")
        speaker.speak("Snake!")
        # time.sleep(1)
        speaker.speak("Water!")
        # time.sleep(1)
        speaker.speak("Gun!")
        # time.sleep(0)


        if user not in ['1', '2', '3', '4', '5']:
            print("Invalid Choice! Try Again")
            continue
        
        elif user in ['1', '2', '3']:
            pc = random.choice(['1', '2', '3'])

            choices = ["Snake", "Water", "Gun"]
            if user == pc:
                print(f"Both chose {choices[int(user)-1]}. So Draw!")
                p1 += 1
                p2 += 1

            elif user == '1':
                print(f"You chose : {choices[int(user)-1]}")
                print(f"Computer chose : {choices[int(pc)-1]}")
                if pc == '2':
                    print("Snake drinks water. You Win!")
                    speaker.speak("Snake drinks water. You Win!")
                    p1 += 2
                else:
                    print("Gun shoots snake. You Lose!")
                    speaker.speak("Gun shoots snake. You Lose!")
                    p2 +=2

            elif user == '2':
                print(f"You chose : {choices[int(user)-1]}")
                print(f"Computer chose : {choices[int(pc)-1]}")
                if pc == '1':
                    print("Snake drinks water. You Lose!")
                    speaker.speak("Snake drinks water. You Lose!")
                    p2 +=2
                else:
                    print("Water damages Gun. You Win!")
                    speaker.speak("Water damages Gun. You Win!")
                    p1 += 2

            else:
                print(f"You chose : {choices[int(user)-1]}")
                print(f"Computer chose : {choices[int(pc)-1]}")
                if pc == '1':
                    print("Gun shoots snake. You Win!")
                    speaker.speak("Gun shoots snake. You Win!")
                    p1 += 2
                else:
                    print("Water damages Gun. You Lose!")
                    speaker.speak("Water damages Gun. You Lose!")
                    p2 +=2

        elif user == '5':
            print("Your Score:", p1)
            print("Computer Score:", p2)

        else:
            if p1>p2 :
                print("You Win the Game!")
                speaker.speak("You Win the Game!")
            elif p2>p1 :
                print("Computer Wins the Game!")
                speaker.speak("You Lose the Game!")
            print("Your Score : ",p1)
            print("PC score : ",p2)
            print("Thanks for playing.")
            speaker.speak("Your Score ")
            speaker.speak("PC score ")
            speaker.speak("Thanks for playing.")
            break

game()