a = [10, 40, -9, 45, 60, 89]

for i in a:
	print i

# a, b print in reverse

i = len(a)

while i > 0:
	print a[i - 1]
	i -= 1

for index in range(len(a) -1, -1, -1):
	print a[index]

b = [(2, 4), (5, 10), (6, 20), (50,50)]

'''
x: 2, y: 4
x: 5, y: 10
'''

for x, y in b:
 	 # print 'x:{}'.format(x), 'y:{}'.format(y)
	print 'x: {}, y: {}'.format(x, y)

def numb(x = '', y = '', z = ''):

	if x == False:
		return 'y: {}, z: {}'.format(y, z)
	elif y == False:
		return 'x: {}, z: {}'.format(x, z)
	elif z == False:
		return 'x: {}, y: {}'.format(x, y)
	return 'x: {}, y: {}, z:{}'.format(x, y, z)

f =  [(10, 20, 40), (10, 40), (4, 5, 50)]
'''
  x:10, y:20, z:40
  x:10, y:40
  x:4, y:5, z:50
  '''
	# for i in f:
		# if len(i) == 2:
			# print 'x:{}, y:{}, z:{}'.format(x, y, z)
	# else:
		# print 'x:{}, y:{}, '.format(x, y)
for i in f:
	print  numb(*i)

 