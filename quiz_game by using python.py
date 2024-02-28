import random
user_name=input("enter your name :")
questions=[{"question":"what is the captial of Telangana?","answer":"Hyderabad"},
           {"question":"who is the prime minister of India?","answer":"narendra modi"},
           {"question":"In which year ISRO Launch chandrayaan-3?","answer":"2023"},
           {"question":"How many times India got ICC ODI World Cup","answer":"2"},
           {"question":"what is the formation date of Telangana","answer":"02-06-2014"}]
random.shuffle(questions)  #shuffle the questions
score=0  #Initialize score
for i,q in enumerate(questions,1):
    print(f"question{i}:{q['question']}")
    user_answer=input("your answer:").strip().lower()
    if user_answer==q['answer'].lower():
        print("correct answer!!")
        score+=1
    else:
        print("Incorrect!")

print(f"your scored {score} out of {len(questions)}")
print("congrats",user_name,"you try your level best")
