total = 0
count = 0

while True:
	number = int(input("Enter a number (0 to quit): "))	

	if number == 0:
		break

	if number % 2 == 0:
		continue

	total += number
	count += 1

if count > 0:
	average = total / count
	print("Total:", total)
	print("Average:", average)
else:
	print("No valid numbers entered.") 	
