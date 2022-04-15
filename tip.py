print("Welcome to the tip calculator!")
total = input("\nWhat was the total bill?")
tip = input("\nHow much would you tip? 10%, 12%, or 15%?")
people = input("\nHow many people to split among?")

cal_tip = int(total) * (int(tip) / 100)
cal_total = int(total) + cal_tip
cal_split = cal_total / int(people)

message = f"Each person should pay: ${cal_split:.2f}"
print(message)
