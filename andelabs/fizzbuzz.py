def fizz_buzz(m):

	if m % 3 == 0 and m % 5 == 0:
		return "FizzBuzz"

	elif m % 5 == 0:
		return "Buzz"

	elif m % 3 == 0:
		return "Fizz"
	else:
		return m
