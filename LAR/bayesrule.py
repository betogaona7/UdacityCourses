
# Positive test
def bayesrule1(p0,p1,p2):
	result = p0*p1 / ((p0*p1)+((1-p0)*(1-p2))
	return result

# Negative test
def bayesrule2:
	result = (p0*(1-p1))/((p0*(1-p1))+((1-p0)*p2))
	return result



p0 = 0.1 #p(c)
p1 = 0.9 #p(pos/c)
p2 = 0.8 #p(pos/-c)
print bayesrule1(p0,p1,p2)


p0 = 0.1 #p(c)
p1 = 0.9 #p(pos/c)
p2 = 0.8 #p(neg/-c)
print bayesrule2(p0,p1,p2)
def mean(data):
	return sum(data)/len(data)

def median(data):
	data = sorted(data)
	index = (len(data)-1)/2
	return data[index]

def mode(data):
	winner = 0
	aux = 0
	for element in data:
		result = data.count(element)
		if result > aux:
			aux = result
			winner = element
	return winner

def variance(data):
	m = mean(data)
    newdata = []
    for element in data:
        dif = element - m
        newdata.append(dif*dif)
    return mean(newdata)

from math import sqrt

def stddev(data):
    va = variance(data)
    return sqrt(va)

import random

def flip(N):
    data = []
    for number in range(0,N):
        number = random.random()
        if number > 0.5:
            data.append(1)
        else:
            data.append(0)
    return data

def flip(N):
	return [random.random() > 0.5 for x in range(N)]

def sample(N):
	return [mean(flip(N)) for x in range(N)]


def calculate_weight(data, z):
	#extract data between lower and upper quatile
	data.sort()
	lowerq = (len(data)-3)/4
	upperq = lowerq * 3 + 3
	newdata = [data[i] for i in range(lowerq, upperq)]

	#fit Gaussian using MLE
	mu = mean(newdata)
	sigma = stddev(newdata)

	#compute x that corresponfs to standar score
	x = mu + z * sigma
	return x

def factor(l):
    return 1.96

def conf(l):
	return factor(l)*sqrt((var(l)/len(l)))

def test(l, h):
    ci = conf(l)
    m = mean(l)
    lowerb = m - ci
    upperb = m + ci
    if h < upperb and h > lowerb:
        return True
    return False

def test(l,h):
	m = mean(l)
	c = conf(l)
	return abs(h-m) <= c


from  random import randint
N = 1000

def simulate(N):
	K = 0
	truth = randint(1,3)
	for i in range(N):
		guess1 = randint(1,3)
		if truth == guess1:
			monte = randint(1,3)
			while monte == truth:
				monte = randint(1,3)
		else:
			monte = 6- truth - guess1
		guess2 = 6 - guess1- monte
		if guess2 == truth:
			K = K + 1
	return float(K)/float(N)
