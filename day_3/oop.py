from person import person
from kenyan import Kenyan

p = person('joe', 23)
p2 = person('jane', 23)
p3 = person('george', 40)
print p.say_hello()

a = [('jane', 23), ('joe', 34), ('mal', 18),
	('jacob', 65), ('jee', 18), ('josh', 60)]

b = []

for name, age, in a:
	Person = person(name, age)
	b.append(Person)
#print b
# print person.people_count
# print p2.people_count
for people in b:
	print people.say_hello()

