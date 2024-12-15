#!/usr/bin/python3
import os
import sys
import re

# list contains each line in the document
lines = []

# helper class
class Line:
	def __init__(self, line_num: int, s: str):
		self.line_num = line_num
		self.s = s

# sorts the values according to line number
def sort_func(value):
	return value.line_num

# this will organize the lines. Typically only needed when writing
# and listing a doc.
def organize_lines():
	lines.sort(key=sort_func)

def read_file(file_name):
	f = open(file_name, "r")

	for line in f.readlines():
		match = re.match(r"(\d*)\s*(.*)", line)
		line_num, s = match.groups()

		# convert the line number to an integer
		line_num = int(line_num)

		# then append the available lines
		lines.append(Line(line_num, s))

		# finally organize the lines
		organize_lines()

# helper functions
# clears the screen on all platforms
def clear_screen():
	# only for linux or mac systems
	if os.name == "posix":
		os.system("clear")

	# only for windows systems
	elif os.name == "nt":
		os.system("cls")

def do_command(line: str):
	line = line.lower() # lowercase the line to match it correctly
	line = line.strip() # remove whitespace
	commands = line.split(" ")
	print(commands)

	# don't do anything if it's just whitespace.
	if line != "":
		match line:
			# exit the program
			case "exit":
				exit()

			case "list":
				# we have an organize function that we use to organize lines
				organize_lines()

				for l in lines:
					print(l.line_num, l.s)

			# write to a file
			case "write":
				file_name = input("file name: ")
				f = open(file_name, "w")

				organize_lines()
					
				for l in lines:
					_line = str(l.line_num) + " " + l.s + "\n"
					#_line = l.s + "\n"
					f.write(_line)

				# probably don't need a function to tell you the write succeeded.
				# but can change this later...
				#print("SUCCESSFUL")

			case "cls":
				clear_screen()

			case "words":
				total_words = 0
				for l in lines:
					total_words += len(l.s.split())
				print("words:", total_words)

			case _:
				print(line, "is not a recognized command!")

def main(arg = None):
	if arg:
		read_file(arg)

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

						# or if it does, delete it first. Then...
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

	# if there is not 2 arguments
	if len(sys.argv) == 2:
		try:
			# attempt to open the file
			main(sys.argv[1])

		# if it cannot open...
		except FileNotFoundError:
			print("File '" + sys.argv[1] + "' not found!")
			exit(1)

	# if there are no command line arguments
	elif len(sys.argv) == 1:
		main()

