#           Index 0          Index 1          Index 2
tasks = ["Do homework", "Go to the gym", "Get groceries"]

# Print out each item in the list with a number beside it starting from 1.
for item_number, task in enumerate(tasks, 1):
    print(f"{item_number}. {task}")

# Prompt the user for which task they want to delete. Cast the type to 'integer'. input() returns a string by default.
choice = int(input("Which task do you want to delete? "))
# Reduce the value of choice by 1 to account for the fact that index numbers count up from 0 and the user is seeing a list counting up from 1.
choice = choice - 1
# Delete element from the list by its index.
del tasks[choice]

# Print tasks.
print(tasks)