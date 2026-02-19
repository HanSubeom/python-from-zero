count_positive = 0
count_negative = 0
count_zero = 0

for i in range(5):
	number = int(input("숫자를 입력하세요: "))

	if number > 0:
		count_positive += 1
	elif number < 0:
		count_negative += 1
	else:
		count_zero += 1

print("양수의 개수:", count_positive)
print("음수의 개수:", count_negative)
print("0의 개수:", count_zero)
