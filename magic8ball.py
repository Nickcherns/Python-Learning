import random


name = "Keith"

question = "Is earth flat?"

answerPrompt = "Magic 8-Ball's answer: "

random_number = random.randint(1, 9)

print(name + " asks: " + question)

if random_number == 1:
    print(answerPrompt + "Yes - definitely")
elif random_number == 2:
    print(answerPrompt + "It is decidedly so")
elif random_number == 3:
    print(answerPrompt + "Without a doubt")
elif random_number == 4:
    print(answerPrompt + "Reply hazy, try again")
elif random_number == 5:
    print(answerPrompt + "Ask again later")
elif random_number == 6:
    print(answerPrompt + "Better not tell you now")
elif random_number == 7:
    print(answerPrompt + "My sources say no")
elif random_number == 8:
    print(answerPrompt + "Outlook not so good")
elif random_number == 9:
    print(answerPrompt + "Very doubtful")
else: 
    print("Error")