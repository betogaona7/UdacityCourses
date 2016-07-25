
import os
import re

def rename_files():
	# Get files name from a folder
	file_list = os.listdir(r"/home/alberto/Desktop/prank")
	#print(file_list)
	save_path = os.getcwd()
	os.chdir(r"/home/alberto/Desktop/prank")
	# For each file, rename filename
	for file_name in file_list:
		new_name = re.sub('[0123456789]','',file_name)
		os.rename(file_name, new_name) 
	os.chdir(save_path)

rename_files()
