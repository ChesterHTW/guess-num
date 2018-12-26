import random

r = random.randint(1, 100)
while True:
	num = input('請猜一個數字：')
	num = int(num)
	if unm == r:
		print('猜對了！')
		break
	elif num > r:
		print('比答案大')
	elif unm < r:
		print('比答案小')