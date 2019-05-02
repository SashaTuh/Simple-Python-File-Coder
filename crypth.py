#!/usr/bin/env

import os

def code_f(file_name, code):
	check_inputs(file_name, code)

	code = int(code)
	file = open(file_name).read()
	coded_list = [] #list of letter in coded form
	for letter in file:
		letter_int = ord(letter)
		coded_list.append(letter_int * code)
		print(str(letter_int * code))

	file = open(file_name, "w")
	for num in coded_list:
		file.write(str(num) + " ")
	file.close()

	print("[!] File was successfully coded")

def decode_f(file_name, code):
	check_inputs(file_name, code)

	code = int(code)
	decode_list = []
	file = open(file_name, "r").read()
	file_write = open(file_name, "w")
	file = file.split(" ")
	for letter in file:
		if(letter == ""):
			break
		letter = chr(int(int(letter) / code))
		print(letter)
		file_write.write(letter)
	file_write.close()

	print("[!] File was successfully decoded")

def check_inputs(file_name, code): #if all inputs are clear
	try:
		file = open(file_name).read()
	except:
		print("[!] File is unreadable") #if file is unreadable or isn't in folder
		input("Press any key to exit...")
		exit()

	try:
		code = int(code)
	except:
		print("[!] Use only numbers")
		input("Press any key to exit...")
		exit()

def start():
	print("[*] Code file or decode [c/d]") #c - code, d - decode
	command = input() #choose commands c or d
	if(command == 'c'): #code file, initializete code and name of a file
		code = input("[?] Choose your password to code a file: ")
		name = input("[?] Enter name of your file(with extension): ")
		code_f(name, code) #code

	elif(command == 'd'):
		code = input("[?] Enter our password: ")
		name = input("[?] Enter name of your file(with extension): ")
		decode_f(name, code)

	else:
		os.system("CLS") #clear and restart
		print("[!] c - code, d - decode")
		start() #restart

if(__name__ == "__main__"):
	start()