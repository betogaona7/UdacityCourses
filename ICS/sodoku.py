#Correct1 = [[1,2,3,4],
#		  [2,4,1,3],
#		  [3,1,4,2],
#		  [4,3,2,1]]

#Correct2 = [[1,2,3],
#          [2,3,1],
#          [3,1,2]]

#Incorrect1 = [[1,2,3,4],
#              [2,3,1,3],
#              [3,1,2,3],
#              [4,4,4,4]]

#Incorrect2 = [ [1,2,3,4],
#               [2,3,1,4],
#               [4,1,2,3],
#               [3,4,1,2]]

#incorrect3 = [[1,2,3,4,5],
#              [2,3,1,5,6],
#              [4,5,2,1,3],
#              [3,4,5,2,1],
#              [5,6,4,3,2]]

#incorrect4 = [['a','b','c'],
#              ['b','c','a'],
#              ['c','a','b']]

#incorrect5 = [ [1, 1.5],
#               [1.5, 1]]

def valid_row(row, list_numbers):
    for element in list_numbers:
        if element not in row:
            return False
    return True
    
def check_sudoku(sodoku):
    list_numbers = []
    #fill list_numbers
    cont = 0
    while cont < len(sodoku):
        cont += 1
        list_numbers.append(cont)
    #Check horizontal 
    for horizontal_row in sodoku:
        if not valid_row(horizontal_row, list_numbers):
            return False
    #Check vertical
    cont1, cont2 = 0, 0
    vertical_row = []
    while(cont1 < len(sodoku)):
        while cont2 < len(sodoku):
            vertical_row.append(sodoku[cont2][cont1])
            cont2 += 1
        print (vertical_row)
        if not valid_row(vertical_row, list_numbers):
            return False
        vertical_row = []
        cont1 += 1
        cont2 = 0
    return True

print(check_sudoku(sodoku))

""" Another form: """
"""
def check_sodoku(p):
	n = len(p) # Extract size of grid 
	digit = 1  # Start with 1
	while digit <= n: # Go through each digit 
		i = 0
		while i < n: # Go through each row and column
			row_count = 0
			col_count = 0
			j = 0
			while j < n: # For each entry in ith row/column
				if p[i][j] == digit: # Check row count 
					row_count = row_count + 1 
				if p[j][i] == digit:
					col_count = col_count + 1
				j += 1
			if row_count != 1 or col_count != 1:
				return False 
			i += 1 # Next row/column
		digit += 1
	return True # Nothing was wrong!
"""
