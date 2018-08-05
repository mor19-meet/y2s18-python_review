# Write your solutions for 1.5 here!
class Superheros:
	def __init__(self, name, superpower,strength ):
		self.name = name
		self.superpower = superpower
		self.strength = strength
	def save_civilian (self, work):
		strength = strength - work
		if (work > strength):																						
			print("Superhero is not strong enough! :(")

super = Superheros("spiderman", "strings", "walls")
print (super.name)
print(super.superpower)

