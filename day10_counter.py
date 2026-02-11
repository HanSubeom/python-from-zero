count = 0

for i in range(5):
	age = int(input("나이를 입력하세요: "))

	if age >= 20:
		count = count + 1

print("성인의 수:", count)
