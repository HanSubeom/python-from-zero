total = 0
count = 0

n = int(input("몇 개의 숫자를 입력할까요? "))

for _ in range(n):
	number = int(input("숫자를 입력하세요: "))
	total += number
	count += 1

if count > 0:
	average = total / count
	print("총합:", total)
	print("평균: ", average)
else:
	print("입력된 숫자가 없습니다.")
