def prime_checker(number):
  if number == 1:
    return False
  if number % 2 == 0:
    return False
  for candidate in range(3, number / 2, 2):
    if number % candidate == 0:
      return False
  return True

  print prime_checker 

  class PrimeChecker(number):
  	def __init__(self, string):
  		self.string = 'string'

  	if 