class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)
		except ValueError:
			raise ValueError('The coordinates must be nonempty')
		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__ (self, v):
		return self.coordinates == v.coordinates


	def plus(self, v):
		new_coordenates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordenates)

	def minus(self, v):
		new_coordenates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordenates)

	def times_scalar(self, c):
		new_coordenates = [c*x for x in self.coordinates]
		return Vector(new_coordenates)



my_vector = Vector([1,2,3])
print(my_vector)