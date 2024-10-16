#list=array
#dictionary=object

questions=[
    "Which of the following planets in our solar system is known as the 'Red Planet'?",
    "Who is the author of the famous Novel 'To Kill a Mockingbird'?",
    "Which Indian state is known as the 'Land of Gods'?",
    "Who was the first Indian to win the Nobel Prize in Physics?",
    "In Hindu mythology, what is the name of the god of wisdom and remover of obstacles?",
    "Which Indian city is known as the 'City of Lakes'?",
    "Who was the Indian king who built the famous temple of Konark?",
    "What is the name of the famous Indian mathematical text that dates back to the 5th century CE?",
    "Who was the first Indian woman to win the Nobel Peace Prize?" 
    ]
money=0
print(' "GET READY TO BE A CROREPATI!" ')
for i in range(len(questions)):
    print("Question",i+1,">",questions[i])
    
    if(i==0):
        answers=("Earth", "Mars", "Jupiter", "Saturn")
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="2"):
            print("Correct answer")
            money=money+5
        else:
            print("Incorrect answers")
    elif(i==1):
        answers=("R.K. Narayan", "Harper Lee", "Arundhati Roy", "Vikram Seth")
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="2"):
            print("Correct answer")
            money=money+5
        else:
            print("Incorrect answers")
    elif(i==2):
        answers=("Uttarakhand", "Kerala", "Tamil Nadu", "Himachal Pradesh" )
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="1"):
            print("Correct answer")
            money=money+5
        else:
            print("Incorrect answers")
    elif(i==3):
        answers=("C.V. Raman", "Homi J. Bhabha", "Vikram Sarabhai", "Satyendra Nath Bose")
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="1"):
            print("Correct answer")
            money=money+10
        else:
            print("Incorrect answers")
    elif(i==4):
        answers=("Brahma", "Vishnu", "Shiva", "Ganesha" )
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="4"):
            print("Correct answer")
            money=money+10
        else:
            print("Incorrect answers")
    elif(i==5):
        answers=("Udaipur", "Jaipur", "Jodhpur", "Bikaner" )
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="1"):
            print("Correct answer")
            money=money+10
        else:
            print("Incorrect answers")
    elif(i==6):
        answers=("Ashoka", "Akbar", "Narasimhadeva I", "Krishnadeva Raya")
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="3"):
            print("Correct answer")
            money=money+25
        else:
            print("Incorrect answers")
    elif(i==7):
        answers=("Aryabhatiya", "Brahmasphuta Siddhanta", "Mahabharata", "Ramayana" )
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="1"):
            print("Correct answer")
            money=money+25
        else:
            print("Incorrect answers")
    elif(i==8):
        answers=("Indira Gandhi", "Mother Teresa", "Sarojini Naidu", "Rani Lakshmibai" )
        print("Options are:",answers)
        ans=input("Enter your answer:")
        if(ans=="2"):
            print("Correct answer")
            money=money+25
        else:
            print("Incorrect answers")
    i=i+1

if(money<100):
    print("Money Won : ",money,"lakh")
elif(money>100):
    print("Money won :",(money//100),"crore",(money%100),"lakh")   
    
    

    