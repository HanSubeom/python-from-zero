total = 0
count = 0

while True:
	number = int(input("숫자를 입력하세요. (0입력 시 종료): "))

	if number == 0:
		break

	total += number
	count += 1

if count > 0:
	average = total / count
	print("총합:", total)
	print("평균:", average)

else:
	print("입력된 숫자가 없습니다.")
