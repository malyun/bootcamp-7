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
for i in f:
	print  numb(*i)

 