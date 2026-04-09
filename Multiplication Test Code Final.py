import random
import time  


def easy_mode():

    print("\nWelcome to EASY mode : ")

    global correct

    correct = 0
    wrong = 0

    question_number = 1            # this increments by 1 ultil it reaches 10 so that there is only 10 questions per round.

    while question_number != 11:   #stops when 10 questions are asked.

        n1 = random.randint(0,10)           # randomly chooses a number in the given range
        n2 = random.randint(0,10)

        question = int(input(f"\n{question_number} : {n1} x {n2} = "))     # asks the user the question
        answer = n1 * n2                                                   # calculates the answer

        if question != answer:
            print("Incorrect\n") 
            print("The correct answer is", answer)                   # if the answer is wrong, it outputs incorrect and gives the correct answer. adds 1 to the 'wrong' varibale
            wrong += 1
        else:
            print("Correct!\n")                                      # if correct then adds 1 to the 'correct' variable and outputs correct
            correct += 1

        question_number += 1

    print("You got", correct, "out of 10 correct.\n")       #outputs score


def standard_mode():
        
    print("\nWelcome to STANDARD mode : ")

    global correct

    correct = 0
    wrong = 0

    question_number = 1

    while question_number != 11:

        n1 = random.randint(1,12)
        n2 = random.randint(1,12)

        question = int(input(f"\n{question_number} : {n1} x {n2} = "))
        answer = n1 * n2

        if question != answer:
            print("Incorrect\n")
            print("The correct answer is", answer)
            wrong += 1
        else:
            print("Correct!\n")
            correct += 1

        question_number += 1

    print("You got", correct, "out of 10 correct.\n")


def hard_mode():
        
    print("\nWelcome to HARD mode : ")

    global correct
    
    correct = 0
    wrong = 0

    question_number = 1

    while question_number != 11:

        n1 = random.randint(2,15)
        n2 = random.randint(2,15)

        question = int(input(f"\n{question_number} : {n1} x {n2} = "))
        answer = n1 * n2

        if question != answer:
            print("Incorrect\n")
            print("The correct answer is", answer)
            wrong += 1
        else:
            print("Correct!\n")
            correct += 1

        question_number += 1

    print("\nYou got", correct, "out of 10 correct.\n")


#main progarm

play_again = "Y"

while play_again == "Y":

    print("\n~ ~ ~ Welcome to the Multiplication Test ~ ~ ~\n")
    print("Please enter your details below.\n")

    firstname = input("Firstname: ").lower()                          #asks for surname and firstname
    surname = input("Surname: ").upper()

    username = firstname[0] + firstname[1] + firstname[2] + surname[0] + surname[1] + surname[2]       # creating username using first 3 letters of forst name and last name
    print("\nYour username is:", username, "\n")

    start_time = time.time()     #starts timeer

    while True:
        
        diffculty_level = int(input("Which difficulty level would you like to play at? \n 1. EASY \n 2. STANDARD\n 3. HARD\n\n : "))

        if diffculty_level == 1:
            easy_mode()                #calls the function dpending on which mode the user wants to play
            break
        elif diffculty_level == 2:
            standard_mode()
            break
        elif diffculty_level == 3:
            hard_mode()
            break
        else:
            print("\nInvalid input. Try again.\n")

    end_time = time.time()                                    #ends the timer and calculates the time it took by subtracting end time by start time
    time_taken = round(end_time - start_time, 2)

    print("Time taken:", time_taken, "seconds\n")

#file handling

    file = open("results.txt", "a")
    file.write(username + " : " + str(correct) + " : " + str(time_taken) + "\n")
    file.close()


    print("\n~ ~ ~ LEADERBOARD ~ ~ ~\n")

    file = open("results.txt", "r")              #opens the file to read the scores
    lines = file.readlines()
    file.close()

    scores = []

    for line in lines:
        parts = line.strip().split(" : ")

        if len(parts) == 3 and parts[1].strip().isdigit():              #makes sure that the line is valid
            name = parts[0]
            score = int(parts[1].strip())

            try:
                time_value = float(parts[2].strip())
            except:
                time_value = 0.0

            scores.append([name, score, time_value])

    for i in range(len(scores)):                                     # bubble sort to sort the score in descending order
        for j in range(len(scores) - 1):
            if scores[j][1] < scores[j + 1][1]:
                temp = scores[j]
                scores[j] = scores[j + 1]
                scores[j + 1] = temp

    # Display leaderboard
    for item in scores:
        print(item[0], "| Score:", item[1], "| Time:", item[2], "seconds")

    play_again = input("\nDo you want to play again? (Y/N): ").upper()      #checks if you want to play again.

    if play_again != "Y":
        print("\nThanks for playing! Goodbye 👋")                            # if not then goodbye message
