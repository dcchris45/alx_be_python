# Ask the user for the task they want to do
task = input("Enter your task: ")

# Ask for the priority and convert the answer to lowercase
priority = input("Priority (high/medium/low): ").lower().strip()

# Make sure the user enters a valid priority
while priority not in ("high", "medium", "low"):
    print("Please enter: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower().strip()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Validate the time-bound response
while time_bound not in ("yes", "no"):
    print("Please answer yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Use match-case to choose the base message depending on the priority
match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Note: '{task}' is a low priority task"
    case _:
        base_message = f"Reminder: '{task}' has an unknown priority"

# Add urgency if the task is time-bound
if time_bound == "yes":
    final_message = base_message + " that requires immediate attention today!"
else:
    # Modify message depending on the priority when not time-bound
    if priority == "low":
        final_message = base_message + ". Consider doing it when you have free time."
    elif priority == "medium":
        final_message = base_message + ". Try to schedule it soon."
    else:  # high priority but not time-bound
        final_message = base_message + ". Aim to work on it soon."

# Print the final reminder
print()
print(final_message)
