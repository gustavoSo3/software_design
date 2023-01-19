
class Cat:
	"""A class to represent a Cat
	"""

	def __init__(self, name : str, age: int):
		"""A new cat will be created
		"""
		self.name = name
		self.age = age
		self.accesories = [
			"Hello there",
			3.1415,
			{
				"enemy": "dog"
			},
			[
				"NICE",
			],
		]

	def __repr__(self) -> str:
		return f"The cat: {self.name}, is {self.age} years old."


def main():

	tom = Cat("Tom", 3)
	luna = Cat("Luna", 8)

	print(tom)
	print(luna)


if __name__ == "__main__":
	main()
