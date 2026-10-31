'''Python Basics Assignment '''

print("=" * 60)
print("1. PRINTING AND VARIABLES")
print("=" * 60)

# Print your name using only one print function
print("Sarvesh")

# Define variables with the requested values
mukesh = 7
z = 6
rohan = 5
longitude = 4

# Output should be 5
print(rohan)

# Declare four variables
ur_age = 21
ur_weight = 50.6
ur_first_name = "Mukesh"
ur_last_name = "Manral"

# Print the types of the variables
print(type(ur_age))
print(type(ur_weight))
print(type(ur_first_name))
print(type(ur_last_name))

# Print their values
print(ur_age, ur_weight, ur_first_name, ur_last_name)

# Compare two equal names
ur_first_name = "Mukesh"
ur_last_name = "Mukesh"
TrueOrFalse = ur_last_name == ur_first_name
print(TrueOrFalse)

# Define x and print it
x = 777
print(x)


print("\n" + "=" * 60)
print("2. OPERATORS")
print("=" * 60)

# Initialize variables
x = 7
y = 77
z = 77.7
zz = "Hi"

# Arithmetic operators
print("Addition:", x + z)
print("Subtraction:", z - y)
print("Multiplication:", x * z)
print("Exponentiation:", x ** 2)  # x raised to the power 2
print("Division:", x / z)
print("Floor division:", x // z)
print("Modulo:", x % z)

# Comparison operators
print("x < z:", x < z)
print("Type of x < z:", type(x < z))
print("x <= z:", x <= z)
print("x == z:", x == z)
print("x > z:", x > z)
print("x >= z:", x >= z)
print("x != z:", x != z)

# Logical operators
print((108 == 108) and (21 == 21))
print((108 == 108) and (21 == 11))
print((108 == 108) or (21 == 11))
print((108 == 108) or (21 == 11) or (108 <= 11))


print("\n" + "=" * 60)
print("3. CONDITIONAL STATEMENTS")
print("=" * 60)

money = 100000
print(money > 2000)

money = 10000
if money > 1000:
    print("You can afford the data science course.")

test_score = 80
if test_score > 80:
    print("A grade")
elif test_score > 60 and test_score < 80:
    print("B grade")
else:
    print("Nothing for you")


print("\n" + "=" * 60)
print("4. LOOPS AND JUMP STATEMENTS")
print("=" * 60)

# Print numbers from 0 to 9
for iterating_variable in range(10):
    print(iterating_variable)

# Print a message 10 times
for _ in range(10):
    print("I love sports")

# Print numbers from 0 to 9 using a while loop
number = 0
while number < 10:
    print(number)
    number += 1

# Break when num equals 5
for num in range(10):
    if num == 5:
        break
    print("The number is", num)

# Continue when num equals 5 (skip only 5)
for num in range(10):
    if num == 5:
        continue
    print("The number is", num)


print("\n" + "=" * 60)
print("5. STRING MANIPULATION")
print("=" * 60)

# Define the requested string
string_ = "We are creating next generation data science eco-system at CollegeRanker"

# Length, including spaces
print("Length:", len(string_))

# Positive and negative indexing
print("First character:", string_[0])
print("Last character:", string_[-1])

# Slicing
print("First six characters:", string_[:6])
print("From index 7 to ten characters from the end:", string_[7:-10])

# Count a character and a substring
print("Count of 'e':", string_.count("e"))
print("Count of 'data':", string_.count("data"))

# find() returns -1 if not found; index() raises an error if not found
print("find('data'):", string_.find("data"))
print("index('data'):", string_.index("data"))

# startswith() and endswith()
print("Starts with 'We':", string_.startswith("We"))
print("Ends with 'CollegeRanker':", string_.endswith("CollegeRanker"))

# Convert to uppercase
print("Uppercase:", string_.upper())

# Convert only the first character to uppercase
example_text = "python is useful"
print("First character uppercase:", example_text.capitalize())

# Check lower case and upper case
print("'hello'.islower():", "hello".islower())
print("'HELLO'.isupper():", "HELLO".isupper())

# Check digit, alphabetic, and alphanumeric strings
print("'12345'.isdigit():", "12345".isdigit())
print("'Python'.isalpha():", "Python".isalpha())
print("'Python123'.isalnum():", "Python123".isalnum())

# Replace C++ with Python, then split the string
new_str = "C++ is easy to learn"
print("Original:", new_str)
new_str = new_str.replace("C++", "Python")
print("Replaced:", new_str)
print("Split:", new_str.split())


print("\n" + "=" * 60)
print("6. FUNCTIONS")
print("=" * 60)

# Define a welcome message function
def welcome_message(name):
    print("Welcome to Functions !!!", name)

# Call the function with a name
welcome_message("Sarvesh")

# Add 3 and 4, store the result in total, and print it
def add_numbers(a, b):
    return a + b

total = add_numbers(3, 4)
print("Total:", total)

# Return the difference between large_number and small_number
def substraction_function(small_number, large_number):
    return large_number - small_number

# Pass positional arguments in the correct order
print(substraction_function(3, 7))

# Keyword arguments allow arguments to be passed by name
print(substraction_function(large_number=7, small_number=3))


print("\n" + "=" * 60)
print("7. SCOPE OF VARIABLES")
print("=" * 60)

# Access a global variable inside a function
global_variable = "variable outside of function"

def random_function():
    return global_variable

print(random_function())

# A local variable with the same name does not change the global variable
global_variable = "variable outside of function"

def random_function():
    global_variable = "changing variable outside of function from inside of function"
    return global_variable

print(random_function())
print(global_variable)

print("\nAssignment completed.")
