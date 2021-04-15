import os
directory = input ("Enter the name of your directory/folder: ")
if os.path.isdir(directory):
	for filename in os.listdir(directory):
		filename = directory + '/' + filename 
		if os.path.isfile(filename):
			file = open(filename, 'r')
			contents = file.read () 
			if "fraud" in contents.lower():
				print (filename)
else:
	print("not in directory")
		
