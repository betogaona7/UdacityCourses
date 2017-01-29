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

	def __getitem__(self, i):
		return self.coordinates[i]

	def __iter__(self):
		return self.coordinates.__iter__()

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

	def is_orthogonal_to(self, v, tolerance=1e-10):
		return abs(self.dot(v)) < tolerance

	def is_parallel_to(self, v):
		return (self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == 3.1416)

	def is_zero(self, tolerance=1e-10):
		return self.magnitude() < tolerance


	def component_parallel_to(self, basis):
		try:
			u = basis.normalized()
			weight = self.dot(u)
			return u.times_scalar(weight)
		except Exception as e:
			raise e

	def component_orthogonal_to(self, basis):
		try:
			projection = self.component_parallel_to(basis)
			return self.minus(projection)
		except Exception as e:
			raise e

	def cross(self, v):
		try:
			x_1, y_1, z_1 = self.coordinates
			x_2, y_2, z_2 = v.coordinates
			new_coordenates = [y_1*z_2 - y_2*z_1,
							   -(x_1*z_2 - x_2*z_1),
							   x_1*y_2 - x_2*y_1]
			return Vector(new_coordenates)
		except ValueError as e:
			msg = str(e)
			if msg == "need more than 2 values to unpack":
				self_embedded_in_R3 = Vector(self.coordinates + ('0',))
				v_embedded_in_R3 = Vector(v.coordinates + ('0',))
				return self_embedded_in_R3.cross(v_embedded_in_R3)
			elif msg == "too many values to unpack" or msg == "need more than 1 value to unpack":
				raise Exception("Only defined in two and three dimensions.")
			else:
				raise e

	def area_of_triangle_with(self, v):
		return self.area_of_parallelogram_with(v)/2

	def area_of_parallelogram_with(self,v):
		cross_product = self.cross(v)
		return cross_product.magnitude()

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
#print(v.dot(w))

v = Vector([-5.955,-4.904, -1.874])
w = Vector([-4.496,-8.755,7.103])
#print(v.dot(w))

v = Vector([3.183,-7.627])
w = Vector([-2.668, 5.319])
#print(v.angle_with(w))

v = Vector([7.35,0.221,5.188])
w = Vector([2.751,8.259,3.985])
#print(v.angle_with(w,True))

v = Vector([-2.328,-7.284,-1.214])
w = Vector([-1.821,1.072,-2.94])
#print("Orthogonal: ", v.is_orthogonal_to(w))
#print("Parallel: ", v.is_parallel_to(w))


#print("#1")
v = Vector([3.039, 1.879])
w = Vector([0.825, 2.036])
#print(v.component_parallel_to(w))

#print("#2")
v = Vector([-9.88, -3.264, -8.159])
w = Vector([-2.155, -9.353, -9.473])
#print(v.component_orthogonal_to(w))

#print("#3")
v = Vector([3.009, -6.172, 3.692, -2.51])
w = Vector([6.404, -9.144, 2.759, 8.718])
vpar = v.component_parallel_to(w)
vort = v.component_orthogonal_to(w)
#print("Parallel component ", vpar)
#print("Orthogonal component ", vort)

v = Vector([8.462,7.893,-8.187])
w = Vector([6.984, -5.975,4.778])
#print(v.cross(w))

v = Vector([-8.987,-9.838,5.031])
w = Vector([-4.268,-1.861,-8.866])
#print(v.area_of_parallelogram_with(w))

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
#print(v.area_of_triangle_with(w))
