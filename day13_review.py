total = 0

for i in range(5):
	number = int(input("숫자를 입력하세요: "))

	if number > 0:
		total += number

print("양수의 합:", total)
