time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
total = 0
heart_rates = []
for time in time_slots:
    heart_rate = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
    while heart_rate < 40 or heart_rate > 180:
        confirm = input(
            f"The heart rate {heart_rate} BPM seems unusual. Are you sure? (Y or N): ")
        if confirm == "Y" or confirm == "y":
            break
        else:
            heart_rate = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
    heart_rates.append([time, heart_rate])
for i in range(len(heart_rates)):
    print(f"In the {heart_rates[i][0]}, your heart rate was {heart_rates[i][1]} BPM")
    total += heart_rates[i][1]
average = total / len(heart_rates)
print(f"Average heart rate today: {average:.2f} BPM")