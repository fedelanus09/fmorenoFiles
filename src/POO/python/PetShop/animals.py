class Dog(object):
	def __init__(self):
		self.name = ""
		self.race = ""
		self.age = 0
		self.weight = 0

	def bark(self):
		print(self.name + " dice: guau guau!")
