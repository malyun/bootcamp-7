def data_type(x):
	'''
	Takes in an argument, x:
	-for an integer,return x ** 2
	-for a float, return x / 2
	-for a string, returns "hello" + x
	-for a boolean, return "boolean "
	-for a long, return "long"
	'''

	if type(x) == int:
		return x ** 2
	elif  type(x) == float:
			return x / 2
	elif type(x) == str:
		return "hello " + x
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"
	else:
		pass

print data_type(27)
print data_type(1.5)
print data_type("Andela")
print data_type(False)
print data_type(1562729287655555555555555555555555555555555555555)

