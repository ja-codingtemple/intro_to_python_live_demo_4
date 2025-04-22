tasks = []

# Function to initialize the list with its three default values.
def initializeList():
    global tasks
    # Index #:    0                1                  2
    tasks =  ["Do homework", "Go to the gym", "Get groceries"]
    print(f"INITIAL LIST: {tasks}")

# METHOD 1: remove()
print("\nMETHOD 1:")
initializeList() # Populate the list with the initializeList() function.
tasks.remove("Go to the gym") # Removes the element "Go to the gym" from the list.
print(f"CURRENT LIST: {tasks}")

# METHOD 2: pop()
print("\nMETHOD 2:")
initializeList() # Populate the list with the initializeList() function.
tasks.pop(0) # Removes the element at index 0 in our list, which is "Do homework"
print(f"CURRENT LIST: {tasks}")

# METHOD 3: del
print("\nMETHOD 3:")
initializeList() # Populate the list with the initializeList() function.
del tasks[0] # Deletes the element at index 0 in our list, which is "Do homework"
print(f"CURRENT LIST: {tasks}")

# METHOD 4:
print("\nMETHOD 4:")
initializeList() # Populate the list with the initializeList() function.
for task in tasks:
    # Check if the word "homework" is in the selected task.
    if "homework" in task:
        tasks.remove(task) # If it is, remove the task.
print(f"CURRENT LIST: {tasks}")