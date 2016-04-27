people = [
	('joe', 78),
	('janet', 90),
	('brian', 67)
]

def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "i am {} and {} y/o".format(name, age)

def max_min(A):
	'''
	return  max value - min value
	e.g [10, 20, -5, 6, 50, 8]
	''' 
	#return max (A) - min(A)
	max_, min_, = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i

		if i < min_:
			min_ = i

	return max_ - min_


