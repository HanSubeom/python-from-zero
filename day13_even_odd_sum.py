even_sum = 0
odd_sum = 0

for i in range(5):
	number = int(input("숫자를 입력하세요: "))

	if number % 2 == 0:
		even_sum = even_sum + number
	else:
		odd_sum = odd_sum + number

print("짝수 합:", even_sum)
print("홀수 합:", odd_sum)
		
