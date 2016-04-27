def funky(a, b):
	print a + b

funky("mal", "yun")
funky(6, 10)
funky(4, 6)
funky([2,3], [4,5])

a = {1: "apples", 2:"mangoes"}
b = {3: "bananas", 4:"oranges"}

def funky(a, b):
	x = dict(a, **b)
	print x

funky(a, b)