# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        message = f"'{task}' is a high priority task"
    case 'medium':
        message = f"'{task}' is a medium priority task"
    case 'low':
        message = f"'{task}' is a low priority task"
    case _:
        message = "Invalid priority. Please enter high, medium, or low."

# Modify the reminder based on time sensitivity
if time_bound == 'yes':
    message += " that requires immediate attention today!"
elif time_bound == 'no':
    message += ". Consider completing it when you have free time."

# Provide the customized reminder
print(f"Reminder: {message}")
