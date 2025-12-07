task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower().strip()

while priority not in ("high", "medium", "low"):
    print("Please enter: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower().strip()

time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

while time_bound not in ("yes", "no"):
    print("Please answer yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

match priority:
    case "high":
        priority_text = "a high priority task"
    case "medium":
        priority_text = "a medium priority task"
    case "low":
        priority_text = "a low priority task"
    case _:
        priority_text = "a task of unknown priority"

# Build message based on time sensitivity
if time_bound == "yes":
    time_text = "that requires immediate attention today!"
else:
    if priority == "low":
        time_text = "Consider doing it when you have free time."
    elif priority == "medium":
        time_text = "Try to schedule it soon."
    else:  # high priority but not time-bound
        time_text = "Aim to work on it soon."

# ONE final print that includes reminder + task + priority + urgency
print(f"Reminder: '{task}' is {priority_text} {time_text}")
