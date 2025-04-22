'''
In Python when we use the + (addition operator) with two strings, it concatenates them, meaning it just combines the strings.
'''
print("dog" + "cat")
print("5" + "10")

'''
This is a method of retrieving user input and immediately casting their responses to the type Integer with the int() function.
'''
num1 = int(input("Please enter a number: ")) 
num2 = int(input("Please enter another number: "))

print(num1 + num2)

'''
When you use the addition operator (+) in Python, both sides of the equation must have the same data type, otherwise it will not compile, and it will generate an error.
You can utilize a concept here called Type Casting where we forcibly treat a value as if it is of another data type to resolve this.
For example, we can cast something to the type String with the str() function, or we can cast something to the type Integer with the int() function. 
'''
print("100" + str(100)) # Casting the value 100 to the type String.
print(int("100") + 100) # Casting the value "100" to the type Integer.


'''
If you need to print values of multiple different data types in a single print() statement, it is recommended that you use print(f) because this can allow you
to print out different data types without type casting.
'''
string = "Test"
number = 500

print(f"The value of string is {string} and the value of number is {number}")