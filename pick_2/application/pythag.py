# You need to design & create a function to make a client's life better.

## Step Zero:
### Find your Client and their needs
#  my client needs a program to check the pythagoream theorm so he can spend more time studding than checking answeres. This program can do just that for him.

## Step One: Gantt Chart and Concurrent Programming
### In the form of a Gantt chart, fully plan out the tasks and time needed to complete this task.

## Step Two: Creation
### Create the function!
def check(a,b,c):
    if a*a + b*b == c*c:
        print(c*c, 'right triangle')
    elif a*a + b*b > c*c:
        print('acute triangle')
    elif a*a + b*b < c*c:
        print('obtuse triangle')

check(3,4,5)
## Step Three: Beta Testing
### What can you change and how?
#I can change the fact that this program is not able to use the square root of numbers.
## Step Four: User Documentation
### Create user documentation for your client. What should it contain?
#This program can only be used to check if you have the answeres for a,b, and c. this program is just used to make your homework a little easier.
