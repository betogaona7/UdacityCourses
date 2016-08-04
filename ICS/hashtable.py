
""" Hastable, in search engine was modified by a dictionary, a built-in hastable """ 

def split_string(source, splitlist):
	output = []
	atsplit = True # At a split point 
	for char in source: # Iterate through string by each letter
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				#add character to last word 
				output[-1] = output[-1] + char
	return output


#line 52 if url not in entry[1]:
#			entry[1].append(url)

# counting clicks
def hashtable_update(htable,key,value):
	bucket = hashtable_get_bucket(htable, key)
	for entry in bucket:
		if entry[0] == key:
			entry[1] = value
			return None
	bucket,append([key,value])
	

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for element in bucket:
        if key in element:
            return element[1]
    return None

def hashtable_add(htable,key,value):
   	bucket = hashtable_get_bucket(htable,key)
   	bucket.append([key,value])
    return htable  
    
    
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


""" Another functions, each one is a new problem """

def rabbits(n):
	if n < 1: #no rabbits dead yet 
		return 0
	else:
		if n == 1 or n == 2: # Base case defined in problem statment 
			return 1 
		else:
			return rabbits(n-1) + rabbits(n-2) - rabbits(n-5) #formula for problem statment 

def hexes_to_udacioness(n, spread, target):
	if n >= target:
		return 0
	else:
		return 1 + hexes_to_udacioness(n * ( 1 + spread), spread, target)


def deep_count(p):
	sum = 0
	for e in p:
		sum = sum + 1
		if is_list(e):
			sum = sum + deep_count(e)
	return sum


def longest_repetition(input_list):
	best_element = None
	length = 0
	current = None
	current_length = 0
	for element in input_list:
		if current != element:
			current = element
			current_length = 1
		else:
			current_length = current_length + 1
		if current_length > length:
			best_element = current
			length = current_length
	return best_element

def deep_reverse(p):
	if is_list(p):
		result = []
		for i in range(len(p)-1, -1, -1):
			result.append(deep_reverse(p[i]))
		return result
	else:
		return p