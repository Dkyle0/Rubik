from os import replace
import sys
import random
from error import error_exit
from s_data import init_all, input_to_cube, s_str, out_cube
from human_solv import start_function

fase_cc = ["up", "right", "front", "down", "left", "back"]
machine_algorithm = True
flags = False
extended_input = False
only_terminal = False
random_twist = False
developer = False
ran_len = 25
valid_flags = "-hetrd"
valid_movements = ["U", "U'",
					"D", "D'",
					"L", "L'",
					"F", "F'",
					"R", "R'",
					"B", "B'"]
valid_symb_movements = "UDLFRB"
valid_extra_symb = "'"
extended_symb_movements = "udlfrb"

# def parsing_exteded_movements(result):
# 	for i, muve in enumerate(result):


def parsing_movements(movements):
	brackets = False	#True для открытой скобки, None - закрытой, False - отсутствие скобок
	block = list()
	result = list()
	string = movements.split(' ')
	if len(string) <= 0:
		error_exit('Misuse of spaces\n' + movements, example_usage=True)

	digit = ""		#Если строка пустая, то количество равно единице

	for s in string:
		tmp = ""
		
		for c in s:
			if (len(tmp) == 0 and (c in valid_symb_movements or (extended_input and c in extended_symb_movements))) or (len(tmp) == 1 and c in valid_extra_symb):
				tmp += c
			elif c.isdigit() and (c == '2' or (extended_input and brackets is None)):
				digit += c
			elif extended_input and c == '(' and not brackets:
				brackets = True
			elif extended_input and c == ')' and brackets:
				brackets = None
			else:
				error_exit("Undefined character in {movements} -> {s} -> \'{c}\'".format(movements=movements, s=s, c=c), example_usage=True)

		if extended_input and brackets:
			block.append(tmp)
		else:
			if len(digit) > 0:
				count = int(digit)
			else:
				count = 1
			if count > 0:
				digit = ""
				if extended_input and brackets is None:
					block.append(tmp)
					for i in range(count):
						for elem in block:
							result.append(elem)
					block.clear
				else:
					for i in range(count):
						result.append(tmp)
			else:
				error_exit("Wrong input: {movements}".format(), example_usage=True)
	
	if len(result) == 0:
		error_exit("Wrong input: {movements}".format(), example_usage=True)
	elif not (brackets is False):
		error_exit("Incorrect use of brackets: {movements}".format(), example_usage=True)
	return result

def parsing_flags(string):
	global machine_algorithm
	global extended_input
	global only_terminal
	global random_twist
	global developer
	for c in string:
		if not (c in valid_flags):
			return False
		if c == 'h':
			machine_algorithm = False
		elif c == 'e':
			extended_input = True
		elif c == 't':
			only_terminal = True
		elif c == 'r':
			random_twist = True
		elif c == 'd':
			developer = True
	return True

def to_CubieCube(cube):
	CubieCube_name = list()
	for face in s_str:
		CubieCube_name.append(face[0].upper())

	cubestring = ""
	for face in fase_cc:
		if face == 'back':
			for x in cube[face][::-1]:
				for y in x[::-1]:
					cubestring += CubieCube_name[y]
		else:
			for x in cube[face]:
				for y in x:
					cubestring += CubieCube_name[y]
	return cubestring

def visual_parser(movements):
	r = []
	if movements == None:
		return (r)
	if len(movements) > 2:
		for m in movements.split(" "):
			if len(m) == 1:
				r.append(m)
			elif len(m) == 2 and m[1] != "'":
				r.append(m[0])
				r.append(m[0])
			elif len(m) == 2 and m[1] == "'":
				r.append(m[0] + m[1])
	else:
		if len(movements) == 1:
			r.append(movements)
		elif len(movements) == 2 and movements[1] != "'":
			r.append(movements[0])
		elif len(movements) == 2 and movements[1] == "'":
			r.append(movements[0] + movements[1])
	return (r)

def main():
	global random_twist
	global ran_len
	number_arguments = len(sys.argv)
	if 2 <= number_arguments <= 3:
		if number_arguments == 3:
			str_flags = sys.argv[2]
			if str_flags[0] != '-' or not parsing_flags(str_flags):
				print(parsing_flags(str_flags))
				error_exit(error_msg = "Flags misused\n", example_usage=True)
		argv1 = sys.argv[1]
		if random_twist:
			if argv1.isnumeric:
				ran_len = int(argv1)
				if ran_len < 1:
					error_exit("Wrong input: {ran_len}\nVery small number".format())
			else:
				error_exit("Wrong input: {argv1}".format(), example_usage=True)
		elif argv1 == '-r':
			random_twist = True
		else:
			movements = parsing_movements(argv1)

		if random_twist:
			movements = list()
			max_rand_num = len(valid_movements) - 1
			input_str = ""
			for i in range(0, ran_len):
				twist = valid_movements[random.randint(0, max_rand_num)]
				input_str += twist + " "
				movements.append(twist)
			print(input_str[0:-1:1])
			
	else:
		error_exit(error_msg="Wrong number of arguments")
	cube = {}
	init_all(cube)
	input_to_cube(cube, movements, 0)
	if machine_algorithm:
		from solver import solve
		print('----start cube----')
		out_cube(cube)
		print('----process solve----')
		cubestring = to_CubieCube(cube)
		solution_str = solve(cubestring)
		solution = visual_parser(solution_str)
		if len(solution_str) > 0:
			print("Solution:")
			print(solution_str)
		print('----end cube----')
		input_to_cube(cube, solution)
		out_cube(cube)
		if not only_terminal:
			from d3 import Game
			game = Game(cube, movements, solution)
			game.run()
	else:
		solution, solution_str = start_function(cube)
		if not only_terminal:
			from d3 import Game
			if developer:
				game = Game(cube, movements, solution)
			else:
				game = Game(cube, movements, visual_parser(solution_str))
			game.run()

if __name__ == '__main__':
	main()