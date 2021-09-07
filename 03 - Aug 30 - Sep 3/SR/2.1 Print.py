# Python Module 2 Demos
# 1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window.

# 2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. 
# Python 3.7.1 comes with 69 built-in functions. You can find their full list provided in alphabetical order in 
# the Python Standard Library.

# 3. To call a function (function invocation), you need to use the function name followed by parentheses. 
# You can pass arguments into a function by placing them inside the parentheses. You must separate arguments 
# with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

print("Hello,", "world!")
print()

# 4. Python strings are delimited with quotes, e.g., "I am a string", or 'I am a string, too'.

print("I am a string.")
print('I am a string.')
print("This is the teacher's example")


# 5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when 
# executed, e.g., to print a certain message to the screen.

# 6. In Python strings the backslash (\) is a special character which announces that the next character has a different 
# meaning, e.g., \n (the newline character) starts a new output line.

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

print('\')


# 7. 'Positional arguments' are the ones whose meaning is dictated by their position, e.g., the second argument is 
# outputted after the first, the third is outputted after the second, etc.

print("My name is", "Python.")
print("Monty Python.")


# 8. 'Keyword arguments' are the ones whose meaning is not dictated by their location, but by a special word (keyword) 
# used to identify them.

print("My name is", "Python.", end = " ")
print("Monty Python.")

print("My name is", "Python.", end = "")
print("Monty Python.")

# 9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies 
# the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter 
# specifies what to print at the end of the print statement.

print("My", "name", "is", "Monty", "Python.", sep="-")



####
#### 2.12
####
####



# 1. Literals are notations for representing some fixed values in code. Python has various types of literals - for example, 
# a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").
# The form of the literal determines the representation (type) Python will use to store it in the memory.

print("2")
print(2)
print(11_111_111)

# 2. The binary system is a system of numbers that employs 2 as the base. Therefore, a binary number is made up of 0s and 1s 
# only, e.g., 1010 is 10 in decimal.

# Octal and hexadecimal numeration systems, similarly, employ 8 and 16 as their bases respectivel2y. The hexadecimal system 
# uses the decimal numbers and six extra letters.

print(0o123)
print(0x123)

# 3. Integers (or simply ints) are one of the numerical types supported by Python. They are numbers written without a 
# fractional component, e.g., 256, or -1 (negative integers).

print(4.0)



# 4. Floating-point numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers 
# that contain (or are able to contain) a fractional component, e.g., 1.27.

print(0.0000000000000000000001)
print(6.62607E-34)

# 5. To encode an apostrophe or a quote inside a string you can either use the escape character, e.g., 'I\'m happy.', or open 
# and close the string using an opposite set of symbols to the ones you wish to encode, e.g., "I'm happy." to encode an apostrophe, 
# and 'He said "Python", not "typhoon"' to encode a (double) quote.

print("I like \"Monty Python\"")

# 6. Boolean values are the two constant objects True and False used to represent truth values 
# (in numeric contexts 1 is True, while 0 is False.

print(True > False)
print(True < False)


# EXTRA

# There is one more, special literal that is used in Python: the None literal. This literal is a so-called NoneType object, and it is 
# used to represent the absence of a value. We'll tell you more about it soon.



# Exercise 1

# What types of literals are the following two examples?

# "Hello ", "007"

# Check
# Exercise 2

# What types of literals are the following four examples?

# "1.5", 2.0, 528, False

# Check
# Exercise 3

# What is the decimal value of the following binary number?

# 1011



####
#### 2.1.3
####
####



# 1. An expression is a combination of values (or variables, operators, calls to functions - you will learn about them soon) 
# which evaluates to a value, e.g., 1 + 2.

# 2. Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations,
 # e.g., the * operator multiplies two values: x * y.

# 3. Arithmetic operators in Python: + (addition), - (subtraction), * (multiplication), / (classic division - returns a float 
# if one of the values is of float type), % (modulus - divides left operand by right operand and returns the remainder of the 
# operation, e.g., 5 % 2 = 1), ** (exponentiation - left operand raised to the power of right operand, 
# e.g., 2 ** 3 = 2 * 2 * 2 = 8), // (floor/integer division - returns a number resulting from division, but rounded down to 
# the nearest whole number, e.g., 3 // 2.0 = 1.0)

# +, -, *, /, //, %, **

print () #examples of each above


print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(5/0)

# 4. A unary operator is an operator with only one operand, e.g., -1, or +3.

# 5. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.

# 6. Some operators act before others - the hierarchy of priorities:

# unary + and - have the highest priority
# then: **, 
# then: *, /, and %, 
# and then the lowest priority: binary + and -.


# 7. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.

# 8. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.


####
#### 2.1.4
####
####



# 1. A variable is a named location reserved to store values in the memory. A variable is created or initialized 
# automatically when you assign a value to it for the first time. (2.1.4.1)

# 2. Each variable must have a unique name - an identifier. A legal identifier name must be a non-empty sequence 
# of characters, must begin with the underscore(_), or a letter, and it cannot be a Python keyword. The first 
# character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive. (2.1.4.1)

# 3. Python is a dynamically-typed language, which means you don't need to declare variables in it. (2.1.4.3) To 
# assign values to variables, you can use a simple 'assignment operator' in the form of the equal (=) sign, i.e., var = 1.

# 4. You can also use 'compound assignment operators' (shortcut operators) to modify values assigned to variables, 
# e.g., var += 1, or var /= 5 * 2. (2.1.4.8)

# 5. You can assign new values to already existing variables using the assignment operator or one of the compound 
# operators, e.g.: (2.1.4.5)

# var = 2
# print(var)

# var = 3
# print(var)

# var += 1
# print(var)

# 6. You can combine text and variables using the + operator, and use the print() function to output strings and variables, e.g.: (2.1.4.4)

# var = "007"
# print("Agent " + var)




# Exercise 1

# What is the output of the following snippet?

# var = 2
# var = 3
# print(var)

# Check
# Exercise 2

# Which of the following variable names are illegal in Python?

# my_var
# m
# 101
# averylongvariablename
# m101
# m 101
# Del
# del

# Check
# Exercise 3

# What is the output of the following snippet?

# a = '1'
# b = "1"
# print(a + b)

# Check
# Exercise 4

# What is the output of the following snippet?

# a = 6
# b = 3
# a /= 2 * b
# print(a)

# Check



####
#### 2.1.5
####
####


# 1. Comments can be used to leave additional information in code. They are omitted at runtime. The information left in source code is addressed to human readers. In Python, a comment is a piece of text that begins with #. The comment extends to the end of line.

# 2. If you want to place a comment that spans several lines, you need to place # in front of them all. Moreover, you can use a comment to mark a piece of code that is not needed at the moment (see the last line of the snippet below), e.g.:

# # This program prints
# # an introduction to the screen.
# print("Hello!")  # Invoking the print() function
# # print("I'm Python.")

# 3. Whenever possible and justified, you should give self-commenting names to variables, e.g., if you're using two variables to store a length and width of something, the variable names length and width may be a better choice than myvar1 and myvar2.

# 4. It's important to use comments to make programs easier to understand, and to use readable and meaningful variable names in code. However, it's equally important not to use variable names that are confusing, or leave comments that contain wrong or incorrect information!

# 5. Comments can be important when you are reading your own code after some time (trust us, developers do forget what their own code does), and when others are reading your code (can help them understand what your programs do and how they do it more quickly).




# Exercise 1

# What is the output of the following snippet?

# print("String #1")
print("String #2")

# Check
# Exercise 2

# What will happen when you run the following code?

# This is
a multiline
comment. #

print("Hello!")




####
####  2.1.6
####
####


# 1. The print() function sends data to the console, while the input() function gets data from the console.

# 2. The input() function comes with an optional parameter: the prompt string. It allows you to write a message
# before the user input, e.g.:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

# 3. When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking 
# (it prompts the user to take action when the console is switched to input mode) until the user has entered an 
# input and/or pressed the Enter key.

# NOTE

# You can test the functionality of the input() function in its full scope locally on your machine. For resource 
# optimization reasons, we have limited the maximum program execution time in Edube to a few seconds. Go to 
# Sandbox, copy-paste the above snippet, run the program, and do nothing - just wait a few seconds to see what happens. 
# Your program should be stopped automatically after a short moment. Now open IDLE, and run the same program there - can you see the difference?

# Tip: the above-mentioned feature of the input() function can be used to prompt the user to end a program. Look at the code below:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

# 3. The result of the input() function is a string. You can add strings to each other using the concatenation (+) operator. 
# Check out this code:

num1 = input("Enter the first number: ") # Enter 12
num2 = input("Enter the second number: ") # Enter 21

print(num1 + num2) # the program returns 1221

# 4. You can also multiply (* - replication) strings, e.g.:

myInput = input("Enter something: ") # Example input: hello
print(myInput * 3) # Expected output: hellohellohello



# Exercise 1

# What is the output of the following snippet?

x = int(input("Enter a number: ")) # the user enters 2
print(x * "5")


# Exercise 2

# What is the expected output of the following snippet?

x = input("Enter a number: ") # the user enters 2
print(type(x))





