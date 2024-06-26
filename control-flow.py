
# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 

letter = input(" Please enter a letter from the alphabet ")
print(f"you entered {letter}")


# 2. Write the code that determines whether the letter entered is a vowel

vowels = {'a','e','i','o','u'}
if letter in vowels:
        print(f"the letter {letter} is a vowel.")
           



# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':





# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while True:
    length = input("enter a word or phrase ")
    print(f"What you entered is {len(length)} characters long")
    if length == 'quit':
        break




# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

age = int(input("Input a dog's age: "))
if age <= 2:
    years = age * 10
else:
    years = 20 +(age -2)*7
print(f"The dog's age is {years}")


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# make variable for each input
print("enter the lengths of three side of a triangle: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a ==b == c:
    triangle = "equilateral"
elif a != b and b!= c and a != c:
    triangle = "scalene"
else:
    triangle = "isosceles"
print(f"A triangle with sides {a}, {b},{c} is a {triangle} triangle")

# anothe way to solve this using len ()
# I google searched " Python check if all elements in a list are different"
# https://www.geeksforgeeks.org/python-check-if-list-contains-all-unique-elements/




# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):
###############----reference-----############ https://stackoverflow.com/questions/58565291/find-store-the-first-50-terms-of-the-fibonacci-sequence-via-looping
def print_fibonacci(x):
    a, b = 0, 1  # Initialize the first two terms
    for term in range(x):  # Loop through the first x terms
        if term <= 1:
            # For the first two terms, print the term number itself
            print(f"term: {term} / number: {term}")
        else:
            # For subsequent terms, calculate the next Fibonacci number and print it
            print(f"term: {term} / number: {a}")
            a, b = b, a + b  # Update the numbers for the next term

# Call the function to print the first 50 terms
print_fibonacci(50)




# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.



month = input(" Enter the month of the year (Jan - Dec):")
day = int(input("enter the day of the month"))

if month == 'Dec' or month == 'Jan' or month == 'Feb' or month == 'Mar':
    season = 'Winter'
elif month == 'Apr' or month == 'May':
    season = 'Spring'
elif month == 'Jun':
    if day < 21:
        season = 'Spring'
    else:
        season = 'Summer'
elif month == 'Jul' or month == 'Aug':
    season = 'Summer'
elif month == 'Sep':
    if day < 22:
        season = 'Summer'
    else:
        season = 'Fall'
elif month == 'Oct' or month == 'Nov':
    season = 'Fall'
elif month == 'Dec':
    if day < 21:
        season = 'Fall'
    else:
        season = 'Winter'


print(f"{month} {day} is in {season}")