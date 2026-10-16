'''
Addition quiz

Step 1 : Generate two single-digit integers for number1 (e.g.,4) and number 2 (e.g.,5)
Step 2 :Prompt the student to answer ,"What is 4 + 5?" (user input)
Step 3:Check whether tthe student's answer is correct .
'''

import random

while True :
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Try again!")
num1 = 4
num2 = 5

answer = int(input(f"What is {num1} + {num2}? "))

if answer == num1 + num2:
    print("Correct!")
else:
    print("Try again!")    
    
        