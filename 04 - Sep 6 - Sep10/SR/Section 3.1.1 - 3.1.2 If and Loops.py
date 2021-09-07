
####
#### Decisions
#### 3.1.1
####


##The comparison (or the so-called relational) operators are used to compare values.
##The table below illustrates how the comparison operators work, assuming that x = 0, y = 1, and z = 0:

##Operator	Description	Example
##==	returns if operands' values are equal, and False otherwise

## x = 0, y = 1, and z = 0:

x == y # False
x == z # True
!=	returns True if operands' values are not equal, and False otherwise	
x != y # True
x != z # False
>	True if the left operand's value is greater than the right operand's value, and False otherwise	
x > y # False
y > z # True
<	True if the left operand's value is less than the right operand's value, and False otherwise	
x < y # True
y < z # False
≥	True if the left operand's value is greater than or equal to the right operand's value, and False otherwise	
x >= y # False
x >= z # True
y >= z # True
≤	True if the left operand's value is less than or equal to the right operand's value, and False otherwise	
x <= y # True
x <= z # True
y <= z # False


## When you want to execute some code only if a certain condition is met, you can use a conditional statement:

## a single if statement, e.g.:

x = 10

if x == 10: # condition
    print("x is equal to 10") # executed if the condition is True


#a series of if statements, e.g.:

x = 10

if x > 5: # condition one
    print("x is greater than 5") # executed if condition one is True

if x < 10: # condition two
    print("x is less than 10") # executed if condition two is True

if x == 10: # condition three
    print("x is equal to 10") # executed if condition three is True

#Each if statement is tested separately.




## an if-else statement, e.g.:

x = 10

if x < 10: # condition
    print("x is less than 10") # executed if the condition is True

else:
    print("x is greater than or equal to 10") # executed if the condition is False

## a series of if statements followed by an else, e.g.:



x = 10

if x > 5: # True
    print("x > 5")

if x > 8: # True
    print("x > 8")

if x > 10: # False
    print("x > 10")

else:
    print("else will be executed")

## Each if is tested separately. The body of else is executed if the last if is False.

## The if-elif-else statement, e.g.:

x = 10

if x == 10: # True
    print("x == 10")

if x > 15: # False
    print("x > 15")

elif x > 10: # False
    print("x > 10")

elif x > 5: # True
    print("x > 5")

else:
    print("else will not be executed")

##If the condition for if is False, the program checks the conditions of the subsequent elif blocks - the first elif block that is True is executed. If all the conditions are False, the else block will be executed.

##Nested conditional statements, e.g.:

x = 10

if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


####
#### Loops
#### 3.1.2
####


## There are two types of loops in Python: while and for:
## the while loop executes a statement or a set of statements as long as a specified boolean condition is true, e.g.:

# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

the for loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set - you will learn about them soon) or other objects that are iterable (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function. Look at the examples below:

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

## You can use the break and continue statements to change the flow of a loop:

## You use break to exit a loop, e.g.:

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

You use continue to skip the current iteration, and continue with the next iteration, e.g.:

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")




## The while and for loops can also have an else clause in Python. The else clause executes after the loop finishes its execution as long as it has not been terminated by break, e.g.:

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

## The range() function generates a sequence of numbers. It accepts integers and returns range objects.
## The syntax of range() looks as follows:

    ## range(start, stop, step), where:

##start is an optional parameter specifying the starting number of the sequence (0 by default)
##stop is an optional parameter specifying the end of the sequence generated (it is not included),
##and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
##Example code:

for i in range(3):
    print(i, end=" ") # outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ") # outputs: 6, 4, 2


