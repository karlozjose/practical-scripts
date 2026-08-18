import random, time, re

numberOfQuestions = 5
correctAnswers = 0
time_limit = 8
attempts = 3
for questionNumber in range(1, 1+numberOfQuestions):
    start_time = time.time() # start time for the time limit on each question

    # Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    allowReGex = re.compile(r'^\d+$') # allow digits begging and end

    attempt = 1 # attempt number 1
    while attempt <= attempts:

        while True:
            user_input = input(prompt)
            mo = allowReGex.search(user_input)
            if mo != None:
                break
            if attempt == attempts:
                print("Input is not an interger.")
                break
            print("Input is not an interger. Try again.")
            attempt += 1
        
        question_time = time.time()
        ans = num1 * num2
        time_taken = round((question_time - start_time),2)

        if time_taken >= time_limit:
            print("Time out")
            print("You took "+ str(time_taken) + " seconds to answer.")
            break
        elif user_input == str(ans) and time_taken < time_limit:
            print('Correct!')
            print('You answer in '+ str(time_taken) + ' seconds.')
            start_time = question_time
            correctAnswers += 1
            break
        elif user_input != str(ans) and attempt < attempts :
            print("incorrect answer, try again")
            attempt += 1
        elif user_input != str(ans) and attempt == attempts :
            print("incorrect answer")
            attempt += 1 

    time.sleep(1) # Brief pause to let user see the results.

print()
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
print("Thanks for playing!")
print()
time.sleep(1)
