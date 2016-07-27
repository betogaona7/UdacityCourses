def read_text():
	text = open("/home/alberto/Desktop/movie_quotes.txt", "r")
	lines = text.readlines()
	text.close()


	#contents_of_file_o = quotes.read()
	contents_of_file_c = ""


	index = 0
	for line in lines:
		while(index < len(line)):
			contents_of_file_c += str(ord(line[index]))
			index += 1
		index = 0

	#print("Original: " + contents_of_file_o)
	print("\nCopy: " + contents_of_file_c)

	#quotes.close()

read_text()