"""
Author: Noah Hamblen
Date: 6/25/25
File Name: Hamblen_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand.
"""

# List of tasks related to running a lemonade stand
tasks = [
    "Clean up and track earnings", # End-of-day wrap up
    "Buy lemons and sugar", # Getting ingredients
    "Set up the stand", # Preparing the stand
    "Make fresh lemonade", # Mixing the product
    "Sell to customers" # Business operations
]

# Print all tasks
print("\nLemonade Stand Tasks:\n")
for task in tasks:
    print("-", task)

print("\nWeekly Schedule:\n")

# List of days in the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Loop through each day and assign tasks
for i in range(len(days)):
    day = days[i]
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: It's your day off, you should rest!")
    else:
        task = tasks[i % len(tasks)]  # Cycle through tasks if needed
        print(f"{day}: {task}")