for n in range(30,301):
	if n % 13 ==0 and n % 7 ==0:
		print("a-z")
	elif n % 13 == 0:
		print('xyz')
	elif n % 7 ==0:
		print('abc')
	else:
		print(n)
