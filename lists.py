days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
for day in days:
 user_input = int(input(f"How many steps did you take on {day}? "))
 steps.append(user_input)
print("\nSteps recorded each day:")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")
total_steps = sum(steps)
print(f"\nTotal steps: {total_steps}")
average_steps = total_steps // len(days)
print(f"Average steps: {average_steps}")