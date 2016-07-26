
# Program that detects curse words in a text.
import urllib
import urllib.request

def read_text():
	quotes = open("/home/alberto/Desktop/movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	data = {}
	data['text'] = text_to_check
	url_values = urllib.parse.urlencode(data)

	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + url_values)
	output = connection.read()
	output = str(output)

	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")
	connection.close()


read_text()
