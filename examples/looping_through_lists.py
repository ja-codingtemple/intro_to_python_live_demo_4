'''
Each item in a list (otherwise known as an array) is called an element.
Each element in a list has an index number, which is a number that represents its position in the list.
Index numbers begin at 0. So the first element in a list has an index of 0.
'''

#             0              1              2
tasks = ["Do homework", "Go the gym", "Get groceries"]

'''
To retrieve elements by their index number, you must reference the list itself, followed by [], and specify the index in []
'''
print(tasks[0]) # This retrieves "Do homework" by its index of 0.
print(tasks[1]) # This retrieves "Go to the gym" by its index of 1.
print(tasks[2]) # This retrieves "Get groceries" by its index of 2.    
print(len(tasks)) # This prints out the length of the list 'tasks'. Because there are 3 items in the list, the length is 3.

# LOOPING THROUGH A LIST: Method 1:
print("\nMETHOD 1:")
for task in tasks:
    print(task)



    
# LOOPING THROUGH A LIST: Method 2:
print("\nMETHOD 2:")
'''
Here, we create a for-loop that runs for the number of times specified in range()
Because we provided a value of len(tasks) which evaluates to 3, this loop runs 3 times.
'i' is a variable known as an iterator that is used to count as you go through the list.
'i' begins counting from a value of zero.
Due to this, we can plug it into tasks[] to retrieve an element by its index number.
In the first pass of the loop i is equal to 0.
In the second pass, i is equal to 1.
In the third pass, i is equal to 2.
'''
for index in range(len(tasks)):
    print(tasks[index])
    
# LOOPING THROUGH A LIST: Method 3:
print("\nMETHOD 3:")
for index in range(len(tasks)):
    print(f"{index + 1}. {tasks[index]}")
    
# LOOPING THROUGH A LIST: Method 4:
print("\nMETHOD 4:")
for index, task in enumerate(tasks, 1):
    print(f"{index}. {task}")