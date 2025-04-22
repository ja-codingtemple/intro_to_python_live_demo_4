# Create the original list.
tasks = ["Do homework", "Go to the gym", "Get groceries"]
# Print out the list.
print(tasks)

# Prompt the user to add an item to the list, save their response in a variable called 'new_task'
new_task = input("What do you want to add to your to-do list? ")
# Append the value of new_task to the list.
tasks.append(new_task)
# Print out the list.
print(tasks)

# Append "Walk the dog" to the list.
tasks.append("Walk the dog")
# Print out the list.
print(tasks)