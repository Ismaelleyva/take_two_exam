# Teach the Padawans (middle schoolers) the ways of the force.

## Your goal is to create a lesson to teach absolute beginners how to program! There are two sections you may pick from. Your students must walk away with a working program and a class average of a B on your self made assessment.

## Section 1
### Criteria to Cover in your lesson
#- variables
#- arrays
#- if/else
#- for loops

print('What is programing???:):)')
print('first, you need to know what variables do in programing.')
print('variables can be numbers or words but in programing regular numbers and words do not work like you think.')

print('for example')
print('to have your computer to just print out the number 100 you will need to use A variable like "num" to be "=" to 100')
print('now witch one is correct')
ans = input("num = 100 or 100 = num")
if ans == "num = 100":
    print('great job')
else:
    print('that is not correct')

print('now try setting up a variable but this time for a word using str')
ans1 = input("str = world or world = str")
if ans1 == "str = world":
    print('great job')
else:
    print('that is not correct')
print('okay now we can move on to arrays')
print('arrays are a list of variables')
print('sinse arrays are lists you need to use [] around the list. Also, you can use "arr" for the variable')
print('which one is correct')
ans2 = input("[1,2,3,4,5] = arr or arr = ['boy','toy','cab']")
if ans2 == "arr = ['boy','toy','cab']":
    print('great job')
else:
    print('that is not correct')
print('remember that arr = [1,2,3,4,5] would be correct if it was written this way')
print('now that you know what variables and arrays are you are ready to move on to if/else statements. An if/else statement in programing is litterly telling the computer If your variable is =,>,<, than you tell the computer to say a statement or answer a question')
print('to write an if/else statement you will write if variable == variable:')
print('I can create a question by using input() where in the parenthesis you can write a regular question then use an if/else statement saying if you pick this answere then true but if you pick the other answere then its false')

print('Now, to write an if/else statement that answeres a question in atom using python3 is: print(are you a) que = input(boy or girl) then you can write an if/else statement by writing if variable = boy print(okay great)')
print('then write elif variable == girl print(great) then write else:  print(that is not right)')
print('for example, I can ask the question are you a boy or girl?')
que = input("boy or girl")
if que == "boy":
    print('okay thx')
elif que == "girl":
    print('okay thx')
else:
    print('that is not right')

print("now this is an if/else statement that has nesting involved which only means an if/else statement in an if/else statement")
print("So in the print() part of your if statement add another question with an or statement so you can write an if/else statement. so your program will do this:")
que4 = input("boy or girl")
if que4 == "boy":
    print('are you sure you are a boy?')
    que5 = input("yes or no")
    if que5 == "yes":
        print('okay thx')
    elif que5 == "no":
        print('okay thx')
    else:
        print('that is not an answere')
elif que4 == "girl":
    print('are you sure you are a girl?')
    que5 = input("yes or no")
    if que5 == "yes":
        print('okay thx')
    elif que5 == "no":
        print('okay thx')
    else:
        print('that is not an answere')
else:
    print('that is not an answere')
