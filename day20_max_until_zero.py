max_value = None

while True:
    number = int(input("Enter a number (0 to quit): "))

    if number == 0:
        break

    if max_value is None:
        max_value = number
    elif number > max_value:
        max_value = number

if max_value is None:
    print("No numbers entered.")
else:
    print("Max:", max_value)
