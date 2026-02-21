total = 0

while True:
	number = int(input("숫자를 입력하세요 (0 입력 시 종료): "))

	if number == 0:
		break

	if number % 2 == 0:
		continue

	total += number

print("합:", total)	
