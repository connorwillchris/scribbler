#!/usr/bin/python3

# COPYRIGHT HERE
import os
import re

lines = []

class Line:
	def __init__(self, line_num, s):
		self.line_num = line_num
		self.s = s

	def organize(self):
		return self.line_num

def do_command(line: str):
	line.lower()

	if line == "exit":
		exit(0)

	elif line == "list":
		lines.sort(key=Line.organize)
		for l in lines:
			print(l.line_num, l.s)

	elif line == "write":
		file_name = input("file name: ")
		f = open(file_name, "w+")

		for l in lines:
			_line = str(l.line_num) + " " + l.s + "\n"
			f.write(_line)
		print("finished")
	
	elif line == "cls":
		os.system("clear")

def main():
	os.system("clear")
	while True:
		line = input()

		match = re.match(r"(\d*)\s*(.*)", line)
		line_num, s = match.groups()
		if line_num:
			if s:
				lines.append(Line(line_num, s))
			else:
				for l in lines:
					if l.line_num == line_num:
						lines.remove(l)
						break
		else:
			do_command(s)

if __name__ == "__main__":
	main()
