#!/usr/bin/python3

# COPYRIGHT HERE
import os
import re

# lines list, contains each line in the document.
lines = []

# helper class
class Line:
	def __init__(self, line_num: int, s: str):
		self.line_num = line_num
		self.s = s

# sorts the values according to line number
def sort_func(value: Line):
	return value.line_num

# this will organize the lines. Typically only needed when writing
# and listing a doc.
def organize_lines():
	lines.sort(key=sort_func)

def do_command(line: str):
	line.lower() # lowercase the line, for more consistent matching...
	#line.strip() # remove whitespace

	# TODO turn this to a match statement!
	if line == "exit":
		exit()

	elif line == "list":
		#lines.sort(key=Line.organize)

		# we have an organize function now...
		organize_lines()

		for l in lines:
			print(l.line_num, l.s)

	elif line == "write":
		file_name = input("file name: ")
		f = open(file_name, "w+")

		organize_lines()

		for l in lines:
			_line = str(l.line_num) + " " + l.s + "\n"
			f.write(_line)

		# probably don't need a function to tell you the write succeeded.
		# but can change this later...
		#print("DONE!!!")
	
	elif line == "cls":
		os.system("clear")

def main():
	os.system("clear")
	while True:
		line = input()

		match = re.match(r"(\d*)\s*(.*)", line)
		line_num, s = match.groups()

		# if there is a number at the beginning... 
		if line_num:

			# convert to an integer, so we can sort the numbers by value
			line_num = int(line_num)

			# if the value of string is not None...
			if s:

				# check every line, and make sure it doesn't exist yet
				for l in lines:
					if l.line_num == line_num:
						# or if it does, delete it, then...
						lines.remove(l)
				
				# add the LINE to the list of lines
				lines.append(Line(line_num, s))

			# otherwise if the string is None...
			else:
				# check each line and find a match for line number.
				for l in lines:
					if l.line_num == line_num:
						lines.remove(l)
						break

		# otherwise, it should be some kind of command.
		else:
			do_command(s)

if __name__ == "__main__":
	main()
