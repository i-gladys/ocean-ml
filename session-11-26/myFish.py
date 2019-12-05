class Fish:
	def __init__(self, name='Fish',hunger=0,happiness = 10):
		self.name = 'paco' 
		self.hunger = hunger
		self.happiness = happiness
		# add 4 other data fields 
		self.height = height
		self.weight = weight
		self.

	def eat(self):
		# what happens hunger and happiness when the fish eats?
		self.hunger = self.hunger- 1
		self.happiness = self.happiness+1
		print(self.name + " has eaten.")
	def swim(self):
		# what happens to hunger and happiness when the fist swims?
		self.hunger= self.hunger+1
		self.happiness
	#what other things does the fish do besides eat and swim?
fish = Fish()