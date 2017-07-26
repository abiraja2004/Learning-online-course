#file = open("Add.asm","r")

lines = [] #Declare an empty list named "lines"
with open ('Add.asm', 'rt') as in_file:  #Open file lorem.txt for reading of text data.
	for line in in_file: #For each line of text store in a string variable named "line", and
		lines.append(line)  #add that line to our list of lines.
		       #print the list object.

#print(lines[0])
#print(lines[1])
#print(len(lines))
for i in range(1,len(lines)):
	print(lines[i])