# Create a function to help Mr. James plan for a donut celebration
## Input: Exam Scores for all students
## Output: How many donuts

# Conditions
## If the class average is an A, every student gets a donut
## If the class average is a B, every student gets a half donut. Make sure not to round half donuts up. Return the float.
## If the class average is a C, every student gets 1/3 of a donut. Make sure not to round up, but to return the float
## If the class average is a D, every student will give Mr. James a half donut.


# Step One
## Create a flow chart for your algorithm

# Step Two
## Create your function. Fully comment out you code.
arr = ['A,B,C,D']
A = range(90,100)
B = range(80-89)
C = range(60-79)
D = range(40-59)
def sum_arr(arr):
    ans = 0
    for num in arr:
        ans = ans + num
    return(ans)
my_sum = sum_arr(arr)
print(my_sum)

# Step Three
## Beta test your function with another group. How can you make you function better?
