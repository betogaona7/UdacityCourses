
#Recursive
def fibonacci_recursive(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

#print (fibonacci_recursive(36))

#Iterative 
def fibonacci_iterative(n):
	current = 0
	after = 1
	for i in range(0,n):
		current, after = after, current + after
	return current

print (fibonacci_iterative(36))

