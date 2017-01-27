from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

	CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimension = len(self.coordinates)
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
		return sqrt(sum(coordinates_squared))

	def normalized(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(Decimal('1.0')/Decimal(magnitude))
		except ZeroDivisionError:
			raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

	def dot(self, v):
		return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

	def angle_with(self, v, in_degrees=False):
		try:
			u1 = self.normalized()
			u2 = v.normalized()
			angle_in_radians = acos(u1.dot(u2))

			if in_degrees:
				degrees_per_ratian = 180./pi
				return angle_in_radians * degrees_per_ratian
			else:
				return angle_in_radians
		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception("Cannot compute an angle with the zero vector")
			else:
				raise e
		




v = Vector([8.218, -9.341])
w = Vector([-1.129,2.111])

#print(v.plus(w))

v = Vector([1.671, -1.012, -0.138])
c = 7.41

#print(v.times_scalar(c))

v = Vector([8.813, -1.331,-6.247])
#print(v.magnitude())

v = Vector([5.581,-2.136])
#print(v.direction())

v = Vector([7.887,4.138])
w = Vector([-8.802, 6.776])
print(v.dot(w))

v = Vector([-5.955,-4.904, -1.874])
w = Vector([-4.496,-8.755,7.103])
print(v.dot(w))

v = Vector([3.183,-7.627])
w = Vector([-2.668, 5.319])
print(v.angle_with(w))

v = Vector([7.35,0.221,5.188])
w = Vector([2.751,8.259,3.985])
print(v.angle_with(w,True))