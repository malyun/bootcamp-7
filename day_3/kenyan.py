from person import person

class Kenyan(person):
	corrupt = False

	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt:
			return "yes"
		return "No"

k = Kenyan('Miguna', 23)

k.probe(True)
print "is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()