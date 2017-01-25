import math as m

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
	
	def magnitude(self):
		coordinates_squared =[x**2 for x in self.coordinates]
		return m.sqrt(sum(coordinates_squared))

	def direction(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(1./magnitude)
		except ZeroDivisionErro:
			raise Exception("Cannot normalize the zero vector")



v = Vector([8.218, -9.341])
w = Vector([-1.129,2.111])

#print(v.plus(w))

v = Vector([1.671, -1.012, -0.138])
c = 7.41

#print(v.times_scalar(c))

v = Vector([8.813, -1.331,-6.247])
print(v.magnitude())

v = Vector([5.581,-2.136])
print(v.direction())