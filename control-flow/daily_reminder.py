#Input Phase
while True:
    
    task = input("Enter your task: ").strip().lower()

    priority = input("Enter priority (high, medium, low): ").strip().lower()

    time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            if time_bound == 'yes':
                print(f"⚠️ Reminder: '{task}' is a HIGH priority task that requires immediate attention today!")
            else:
                print(f"⚠️ Reminder: '{task}' is a HIGH priority task. Please prioritize it soon.")

        case "medium":
            if time_bound == 'yes':
                print(f"📌 Reminder: '{task}' is a MEDIUM priority task and time-sensitive. Schedule it today.")
            else:
                print(f"📌 Reminder: '{task}' is a MEDIUM priority task. Try to complete it within the week.")

        case "low":
            if time_bound == 'yes':
                print(f"🕓 Reminder: '{task}' is a LOW priority task but is time-sensitive. Don’t delay.")
            else:
                print(f"📝 Note: '{task}' is a LOW priority task. Handle it when you’re free.")

        case _:
            print(f"❌ Invalid priority: '{priority}'. Please enter 'high', 'medium', or 'low'.")

    #play again
    play_again = input("Would you like to input another task? (Yes or no): ")
    if play_again != 'yes':
        print("Hope to you seen, thanks for the time! ")
        break