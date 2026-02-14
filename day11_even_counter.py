count = 0

for i in range(5):
	number = int(input(f"{i+1}번째 숫자를 입력하세요:"))

	if number % 2 == 0:
		count = count +1

print("짝수 개수:", count)

