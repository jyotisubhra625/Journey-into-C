'''questions = [
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

money = 0

for i in range(len(questions)):
    print("Question", i+1, questions[i])  # Accessing list elements using square brackets
    
    if i == 0:
        answers = ("Earth", "Mars", "Jupiter", "Saturn")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "2":
            print("Correct answer")
            money += 5
        else:
            print("Incorrect answer")
    
    elif i == 1:
        answers = ("R.K. Narayan", "Harper Lee", "Arundhati Roy", "Vikram Seth")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "2":
            print("Correct answer")
            money += 5
        else:
            print("Incorrect answer")
    
    elif i == 2:
        answers = ("Uttarakhand", "Kerala", "Tamil Nadu", "Himachal Pradesh")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "1":
            print("Correct answer")
            money += 5
        else:
            print("Incorrect answer")
    
    elif i == 3:
        answers = ("C.V. Raman", "Homi J. Bhabha", "Vikram Sarabhai", "Satyendra Nath Bose")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "1":
            print("Correct answer")
            money += 10
        else:
            print("Incorrect answer")
    
    elif i == 4:
        answers = ("Brahma", "Vishnu", "Shiva", "Ganesha")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "4":
            print("Correct answer")
            money += 10
        else:
            print("Incorrect answer")
    
    elif i == 5:
        answers = ("Udaipur", "Jaipur", "Jodhpur", "Bikaner")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "1":
            print("Correct answer")
            money += 10
        else:
            print("Incorrect answer")
    
    elif i == 6:
        answers = ("Ashoka", "Akbar", "Narasimhadeva I", "Krishnadeva Raya")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "3":
            print("Correct answer")
            money += 25
        else:
            print("Incorrect answer")
    
    elif i == 7:
        answers = ("Aryabhatiya", "Brahmasphuta Siddhanta", "Mahabharata", "Ramayana")
        print("Options are:", answers)
        ans = input("Enter your answer (1/2/3/4): ")
        if ans == "1":
            print("Correct answer")
            money += 25
        else:
            print("Incorrect answer")
    
    elif(i==8):
        answers=("Aryabhatiya", "Brahmasphuta Siddhanta", "Mahabharata", "Ramayana" )
        print("Options are:",answers)
        ans=input("Enter your answer (1/2/3/4): ")
        if(ans==1):
            print("Correct answer")
            money=money+25
        else:
            print("Incorrect answers")
    elif(i==9):
        answers=("Indira Gandhi", "Mother Teresa", "Sarojini Naidu", "Rani Lakshmibai" )
        print("Options are:",answers)
        ans=input("Enter your answer (1/2/3/4): ")
        if(ans==2):
            print("Correct answer")
            money=money+25
        else:
            print("Incorrect answers")
    i=i+1

if(money<100):
    print("Money Won : ",money,"lakh")
elif(money>100):
    print("Money won :",(money//100),"crore",(money%100),"lakh") 
    '''

# Define the questions, options, and correct answers in a dictionary
questions = {
    "Which of the following planets in our solar system is known as the 'Red Planet'?": {
        "options": ("Earth", "Mars", "Jupiter", "Saturn"),
        "correct_answer": 2,
        "money": 5
    },
    "Who is the author of the famous Novel 'To Kill a Mockingbird'?": {
        "options": ("R.K. Narayan", "Harper Lee", "Arundhati Roy", "Vikram Seth"),
        "correct_answer": 2,
        "money": 5
    },
    "Which Indian state is known as the 'Land of Gods'?": {
        "options": ("Uttarakhand", "Kerala", "Tamil Nadu", "Himachal Pradesh"),
        "correct_answer": 1,
        "money": 10
    },
    "Who was the first Indian to win the Nobel Prize in Physics?": {
        "options": ("C.V. Raman", "Homi J. Bhabha", "Vikram Sarabhai", "Satyendra Nath Bose"),
        "correct_answer": 1,
        "money": 10
    },
    "In Hindu mythology, what is the name of the god of wisdom and remover of obstacles?": {
        "options": ("Brahma", "Vishnu", "Shiva", "Ganesha"),
        "correct_answer": 4,
        "money": 25
    }
}

# Initialize the total money won
total_money = 0

# Iterate over the questions
for question, details in questions.items():
    print(question)
    print("Options are:", details["options"])
    ans = input("Enter your answer (1/2/3/4): ")
    
    # Check if the answer is correct
    if ans == str(details["correct_answer"]):
        print("Correct answer")
        total_money += details["money"]
    else:
        print("Incorrect answer")

# Print the total money won
if total_money < 100:
    print("Money Won:", total_money, "lakh")
elif total_money > 100:
    print("Money won:", (total_money // 100), "crore", (total_money % 100), "lakh")