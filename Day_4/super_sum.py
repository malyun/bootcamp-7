def super_sum(*args):
	'''
	Returns the sum of numbers.

	e.g
	super_sum() ==> "please enter numbers"
	super_sum of(1, 2, 3) ==> 6
	super_sum("string",)
	super_sum([1,2,3]) ==> 6
	super_sum ([1], [2], [3]) ==>60

	'''

	total = 0

	if not args:
		return 0

	else:
		for x in args:
			if type(x) == list:
				 total += sum(x)
				# x is now ([1, 2, 3])
				# for i in x:
					# total += i
			elif type(x) == str:
				return 0
			else:
				total += x
	return total


