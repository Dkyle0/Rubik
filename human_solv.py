from s_data import up_r, input_to_cube, spin_cube_left, out_cube, s_r
from out_solution import out_sr
x_l = ["back",  "left", "front", "right", "back"]
s_str = ["front", "back", "up", "down", "left", "right"]

def check_angular(all, sides, sides2, cords):
	c = 0
	i = 0
	for side2 in sides2:
		for side in sides:
			if all[side2][cords[0 + i]][cords[1 + i]] == all[side][1][1]:
				c+= 1
		if i < 7:
			i += 2
	if (c == 3):
		return True
	return False

def cube_done(all):
	for side in s_str:
		for y in range(3):
			for x in range(3):
				if (x == 1 and y == 1):
					x+= 1
				if(all[side][y][x] != all[side][1][1]):
					return False
	return True

def step_one1(all, debug = 0):
	if (all['front'][1][0] == all['front'][1][1] and all['left'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_1")
		input_to_cube(all, ["F"])
	elif  (all['front'][1][2] == all['front'][1][1] and all['right'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_2")		
		input_to_cube(all, ["F'"])
	elif  (all['front'][2][1] == all['front'][1][1] and all['down'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_3")		
		input_to_cube(all, ["F", "F"])
	elif  (all['right'][0][1] == all['front'][1][1] and all['up'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_4")		
		input_to_cube(all, ["U"])
	elif  (all['right'][1][0] == all['front'][1][1] and all['front'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_5")		
		input_to_cube(all, ["R", "U"])
	elif  (all['right'][2][1] == all['front'][1][1] and all['down'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_6")		
		input_to_cube(all, ["R", "R", "U"])
	elif  (all['right'][1][2] == all['front'][1][1] and all['back'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_7")		
		input_to_cube(all, ["R'", "U"])
	elif  (all['back'][0][1] == all['front'][1][1] and all['down'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_8")		
		input_to_cube(all, ["D'", "D'", "F", "F"])
	elif  (all['back'][1][0] == all['front'][1][1] and all['left'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_9")		
		input_to_cube(all, ["L", "L", "F"])
	elif  (all['back'][1][2] == all['front'][1][1] and all['right'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_10")		
		input_to_cube(all, ["R'", "R'", "F'"])
	elif  (all['back'][2][1] == all['front'][1][1] and all['up'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_11")		
		input_to_cube(all, ["U", "U"])
	elif  (all['left'][0][1] == all['front'][1][1] and all['up'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_12")		
		input_to_cube(all, ["U'"])
	elif  (all['left'][1][0] == all['front'][1][1] and all['back'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_13")		
		input_to_cube(all, ["L", "U'"])
	elif  (all['left'][1][2] == all['front'][1][1] and all['front'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_14")		
		input_to_cube(all, ["L'", "U'"])
	elif  (all['left'][2][1] == all['front'][1][1] and all['down'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_15")		
		input_to_cube(all, ["L'", "L'", "U'"])
	elif  (all['up'][2][1] == all['front'][1][1] and all['front'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_16")		
		input_to_cube(all, ["F", "U'", "R", "U"])
	elif  (all['up'][1][2] == all['front'][1][1] and all['right'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_17")		
		input_to_cube(all, ["U", "F", "U'", "R", "U"])
	elif  (all['up'][1][0] == all['front'][1][1] and all['left'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_18")		
		input_to_cube(all, ["U'", "F", "U'", "R", "U"])
	elif  (all['up'][0][1] == all['front'][1][1] and all['back'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_19")		
		input_to_cube(all, ["U", "R'", "F'"])
	elif  (all['down'][0][1] == all['front'][1][1] and all['front'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_20")		
		input_to_cube(all, ["F'", "U'", "R", "U"])
	elif  (all['down'][1][0] == all['front'][1][1] and all['left'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_21")		
		input_to_cube(all, ["D", "F'", "U", "R", "U"])
	elif  (all['down'][1][2] == all['front'][1][1] and all['right'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_22")		
		input_to_cube(all, ["D'", "F'", "U", "R", "U"])
	elif  (all['down'][2][1] == all['front'][1][1] and all['back'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_1_23")		
		input_to_cube(all, ["D", "D", "F'", "U", "R", "U"])

def step_one2(all, debug = 0):
	if (all['right'][1][0] == all['right'][1][1] and all['front'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_1")
		input_to_cube(all, ["R"])
	elif (all['right'][1][2] == all['right'][1][1] and all['back'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_2")		
		input_to_cube(all, ["R'"])
	elif (all['right'][2][1] == all['right'][1][1] and all['down'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_3")		
		input_to_cube(all, ["R", "R"])
	elif (all['back'][2][1] == all['right'][1][1] and all['up'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_4")		
		input_to_cube(all, ["F", "U", "F'"])
	elif (all['back'][1][2] == all['right'][1][1] and all['right'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_5")		
		input_to_cube(all, ["U", "R", "R", "F'", "U'"])
	elif (all['back'][0][1] == all['right'][1][1] and all['down'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_6")		
		input_to_cube(all, ["D'", "R", "R"])
	elif (all['back'][1][0] == all['right'][1][1] and all['left'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_7")		
		input_to_cube(all, ["L", "L", "U", "F", "U'"])
	elif (all['left'][0][1] == all['right'][1][1] and all['up'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_8")		
		input_to_cube(all, ["F", "U", "U", "F'"])
	elif (all['left'][1][0] == all['right'][1][1] and all['back'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_9")		
		input_to_cube(all, ["F", "L", "U", "U", "F'"])
	elif (all['left'][1][2] == all['right'][1][1] and all['front'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_10")		
		input_to_cube(all, ["U", "U", "L'", "U'", "U'"])
	elif (all['left'][2][1] == all['right'][1][1] and all['down'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_11")		
		input_to_cube(all, ["U", "U", "L'", "L'", "U'", "U'"])
	elif (all['front'][1][0] == all['right'][1][1] and all['left'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_12")		
		input_to_cube(all, ["U", "F", "U'"])
	elif (all['front'][1][2] == all['right'][1][1] and all['right'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_13")		
		input_to_cube(all, ["U", "F'", "U'"])
	elif (all['front'][2][1] == all['right'][1][1] and all['down'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_14")		
		input_to_cube(all, ["D", "R", "R"])
	elif (all['up'][1][2] == all['right'][1][1] and all['right'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_15")		
		input_to_cube(all, ["R'", "U", "F'", "U'"])
	elif (all['up'][1][0] == all['right'][1][1] and all['left'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_16")		
		input_to_cube(all, ["L", "U", "F", "U'"])
	elif (all['up'][0][1] == all['right'][1][1] and all['back'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_17")		
		input_to_cube(all, ["U'", "L", "U", "U", "F", "U'"])
	elif (all['down'][0][1] == all['right'][1][1] and all['front'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_18")		
		input_to_cube(all, ["U", "F'", "U'", "R"])
	elif (all['down'][1][0] == all['right'][1][1] and all['left'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_19")		
		input_to_cube(all, ["U", "D", "F'", "U'", "R"])
	elif (all['down'][1][2] == all['right'][1][1] and all['right'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_20")		
		input_to_cube(all, ["U", "D'", "F'", "U'", "R"])
	elif (all['down'][2][1] == all['right'][1][1] and all['back'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_2_21")		
		input_to_cube(all, ["U", "D'", "D'", "F'", "U'", "R"])

def step_one3(all, debug = 0):
	input_to_cube(all, ["B'", "B'"])
	if (all['back'][0][1] == all['back'][1][1] and all['down'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_1")
		input_to_cube(all, ["B", "B"])
	elif (all['back'][1][0] == all['back'][1][1] and all['left'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_2")
		input_to_cube(all, ["B'"])
	elif (all['back'][1][2] == all['back'][1][1] and all['right'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_3")
		input_to_cube(all, ["B"])
	elif (all['left'][0][1] == all['back'][1][1] and all['up'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_4")
		input_to_cube(all, ["L'", "U'", "L", "U"])
	elif (all['left'][1][0] == all['back'][1][1] and all['back'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_5")
		input_to_cube(all, ["U'", "L", "U"])
	elif (all['left'][1][2] == all['back'][1][1] and all['front'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_6")
		input_to_cube(all, ["U'", "L'", "U"])
	elif (all['left'][2][1] == all['back'][1][1] and all['down'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_7")
		input_to_cube(all, ["U'", "L'", "L'", "U"])
	elif (all['front'][1][0] == all['back'][1][1] and all['left'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_8")
		input_to_cube(all, ["U'", "U'", "F", "U", "U"])
	elif (all['front'][1][2] == all['back'][1][1] and all['right'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_9")
		input_to_cube(all, ["U'", "U'", "F'", "U", "U"])
	elif (all['front'][2][1] == all['back'][1][1] and all['down'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_10")
		input_to_cube(all, ["U'", "U'", "F'", "F'", "U", "U"])
	elif (all['right'][1][0] == all['back'][1][1] and all['front'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_11")
		input_to_cube(all, ["U", "R", "U'"])
	elif (all['right'][1][2] == all['back'][1][1] and all['back'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_12")
		input_to_cube(all, ["U", "R'", "U'"])
	elif (all['right'][2][1] == all['back'][1][1] and all['down'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_13")
		input_to_cube(all, ["U", "R'", "R'", "U'"])
	elif (all['up'][0][1] == all['back'][1][1] and all['back'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_14")
		input_to_cube(all, ["U", "U", "F", "U'", "R", "U'"])
	elif (all['up'][1][0] == all['back'][1][1] and all['left'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_15")
		input_to_cube(all, ["L", "U'", "U'", "F", "U", "U"])
	elif (all['down'][0][1] == all['back'][1][1] and all['front'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_16")
		input_to_cube(all, ["U", "U", "F'", "U'", "R", "U'"])
	elif (all['down'][1][0] == all['back'][1][1] and all['left'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_17")
		input_to_cube(all, ["L'", "U'", "U'", "F", "U", "U"])
	elif (all['down'][1][2] == all['back'][1][1] and all['right'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_18")
		input_to_cube(all, ["U'", "U'", "R", "F'", "U", "U"])
	elif (all['down'][2][1] == all['back'][1][1] and all['back'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_3_19")
		input_to_cube(all, ["D'", "U'", "U'", "R", "F'", "U", "U"])

def step_one4(all, debug = 0):
	if (all['left'][1][0] == all['left'][1][1] and all['back'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_1")
		input_to_cube(all, ["L"])
	elif (all['left'][1][2] == all['left'][1][1] and all['front'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_2")
		input_to_cube(all, ["L'"])
	elif (all['left'][2][1] == all['left'][1][1] and all['down'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_3")
		input_to_cube(all, ["L", "L"])
	elif (all['front'][1][0] == all['left'][1][1] and all['left'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_4")
		input_to_cube(all, ["U'", "F", "U"])
	elif (all['front'][1][2] == all['left'][1][1] and all['right'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_5")
		input_to_cube(all, ["U'", "F'", "U"])
	elif (all['front'][2][1] == all['left'][1][1] and all['down'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_6")
		input_to_cube(all, ["U'", "F'", "F'", "U"])
	elif (all['right'][1][0] == all['left'][1][1] and all['front'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_7")
		input_to_cube(all, ["U'", "U'", "R", "U", "U" ])
	elif (all['right'][1][2] == all['left'][1][1] and all['back'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_8")
		input_to_cube(all, ["U'", "U'", "R'", "U", "U" ])
	elif (all['right'][2][1] == all['left'][1][1] and all['down'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_9")
		input_to_cube(all, ["U'", "U'", "R'", "R'", "U", "U" ])
	elif (all['back'][1][0] == all['left'][1][1] and all['left'][1][0] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_10")
		input_to_cube(all, ["L", "L", "U'", "F", "U" ])
	elif (all['back'][1][2] == all['left'][1][1] and all['right'][1][2] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_11")
		input_to_cube(all, ["U", "U", "R", "R", "U", "F'", "U" ])
	elif (all['back'][0][1] == all['left'][1][1] and all['down'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_12")
		input_to_cube(all, ["D", "D", "U'", "F", "F", "U" ])
	elif (all['up'][1][0] == all['left'][1][1] and all['left'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_13")
		input_to_cube(all, ["L", "U'", "F", "U"])
	elif (all['down'][0][1] == all['left'][1][1] and all['front'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_14")
		input_to_cube(all, ["U'", "F", "U", "L'"])
	elif (all['down'][1][0] == all['left'][1][1] and all['left'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_15")
		input_to_cube(all, ["L'", "U'", "F", "U"])
	elif (all['down'][1][2] == all['left'][1][1] and all['right'][2][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_16")
		input_to_cube(all, ["U'", "U'", "R", "U", "F'", "U"])
	elif (all['down'][2][1] == all['left'][1][1] and all['back'][0][1] == all['up'][1][1]):
		if (debug == 1):
			print("one_4_17")
		input_to_cube(all, ["D", "L'", "U'", "F", "U"])

def step_one_simple(all, debug = 0):
	if (all['up'][0][1] != all['up'][1][1] and all['back'][2][1] == all['back'][1][1]):
		if (debug == 1):
			print("step_one_simple_1")		
		for i in range(5):
			input_to_cube(all, ["B"])
			if (all['up'][0][1] == all['up'][1][1] and all['back'][2][1] == all['back'][1][1]):
				break

def step_one_all(all, debug = 0):
	if all['up'][0][1] != all['up'][1][1] or all['up'][1][0] != all['up'][1][1] or all['up'][1][2] != all['up'][1][1] or all['up'][2][1] != all['up'][1][1]:
		step_one_simple(all, debug)
	if (all['front'][0][1] != all['front'][1][1] or all['up'][2][1] != all['up'][1][1]):
		step_one1(all, debug)
	if (all['right'][0][1] != all['right'][1][1] or all['up'][1][2] != all['up'][1][1]):
		step_one2(all, debug)
	if (all['back'][2][1] != all['back'][1][1] or all['up'][0][1] != all['up'][1][1]):
		step_one3(all, debug)
	if (all['left'][0][1] != all['left'][1][1] or all['up'][1][0] != all['up'][1][1]):
		step_one4(all, debug)
	if all['up'][0][1] != all['up'][1][1] or all['up'][1][0] != all['up'][1][1] or all['up'][1][2] != all['up'][1][1] or all['up'][2][1] != all['up'][1][1]:
		print("step_one_error")

def step_two_1(all, debug = 0):
	if check_angular(all, ["left", "front", "up"], ["left", "front", "up"], [0, 2, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_1_1")
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_1_2")
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["up", "front", "right"], [2, 2, 0, 2, 0, 0]):
		if (debug == 1):
			print("two_1_3")
		input_to_cube(all, ["R'", "D'", "R", "D", "D'"])
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["front", "right", "down"], [2, 2, 2, 0, 0, 2]):
		if (debug == 1):
			print("two_1_4")
		input_to_cube(all, ["D'"])
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_1_5")
		input_to_cube(all, ["D'", "D'"])
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["right", "back", "up"], [0, 2, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_1_6")
		input_to_cube(all, ["R", "D", "R'", "D'", "D'", "D'"])
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_1_7")
		input_to_cube(all, ["D"])
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1
	elif check_angular(all, ["left", "front", "up"], ["left", "back", "up"], [0, 0, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_1_8")
		input_to_cube(all, ["L'", "D'", "L", "D", "D"])
		i = 0
		while (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L", "D", "L'", "D'"])
			i+= 1

def step_two_2(all, debug = 0):
	if check_angular(all, ["right", "front", "up"], ["right", "front", "up"], [0, 0, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_2_1")
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["right", "front", "down"], [2, 0, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_2_2")
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_2_3")
		input_to_cube(all, ["D'"])
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["right", "back", "up"], [0, 2, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_2_4")
		input_to_cube(all, ["R", "D", "R'", "D'", "D'"])
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_2_5")
		input_to_cube(all, ["D'", "D'"])
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["left", "back", "up"], [0, 0, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_2_6")
		input_to_cube(all, ["L'", "D'", "L", "D", "D'", "D'"])
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_2_7")
		input_to_cube(all, ["D"])
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1
	elif check_angular(all, ["right", "front", "up"], ["left", "front", "up"], [0, 2, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_2_8")
		input_to_cube(all, ["L", "D", "L'", "D'", "D"])
		i = 0
		while (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R'", "D'", "R", "D"])
			i+= 1

def step_two_3(all, debug = 0):
	if check_angular(all, ["right", "back", "up"], ["right", "back", "up"], [0, 2, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_3_1")
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_3_2")
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_3_3")
		input_to_cube(all, ["D'"])
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["left", "back", "up"], [0, 0, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_3_4")
		input_to_cube(all, ["L'", "D'", "L", "D", "D'"])	
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_3_5")
		input_to_cube(all, ["D'", "D'"])	
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["left", "front", "up"], [0, 2, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_3_6")
		input_to_cube(all, ["L", "D", "L'", "D'", "D'", "D'"])	
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["right", "front", "down"], [2, 0, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_3_7")
		input_to_cube(all, ["D"])
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1
	elif check_angular(all, ["right", "back", "up"], ["right", "front", "up"], [0, 0, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_3_8")
		input_to_cube(all, ["R'", "D'", "R", "D", "D"])
		i = 0
		while (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]) and i < 10:
			input_to_cube(all, ["R", "D", "R'", "D'"])
			i+= 1

def step_two_4(all, debug = 0):
	if check_angular(all, ["left", "back", "up"], ["left", "back", "up"], [0, 0, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_4_1")
		i = 0
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_4_2")
		i = 0
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0]):
		if (debug == 1):
			print("two_4_3")
		i = 0
		input_to_cube(all, ["D'"])
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["left", "front", "up"], [0, 2, 0, 0, 2, 0]):
		if (debug == 1):
			print("two_4_4")
		i = 0
		input_to_cube(all, ["L", "D", "L'", "D'", "D'"])
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["right", "front", "down"], [2, 0, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_4_5")
		i = 0
		input_to_cube(all, ["D'", "D'"])
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["right", "front", "up"], [0, 0, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_4_6")
		i = 0
		input_to_cube(all, ["R'", "D'", "R", "D", "D'", "D'"])
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2]):
		if (debug == 1):
			print("two_4_7")
		i = 0
		input_to_cube(all, ["D"])
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1
	elif check_angular(all, ["left", "back", "up"], ["right", "back", "up"], [0, 2, 2, 2, 0, 2]):
		if (debug == 1):
			print("two_4_8")
		i = 0
		input_to_cube(all, ["R", "D", "R'", "D'", "D"])
		while (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]) and i < 10:
			input_to_cube(all, ["L'", "D'", "L", "D"])
			i+= 1

def step_two_all(all, debug = 0):
	if (all['up'][2][0] != all['up'][1][1] or all['front'][0][0] != all['front'][1][1] or all['left'][0][2] != all['left'][1][1]):
		step_two_1(all, debug)
	if (all['up'][2][2] != all['up'][1][1] or all['front'][0][2] != all['front'][1][1] or all['right'][0][0] != all['right'][1][1]):
		step_two_2(all, debug)
	if (all['up'][0][2] != all['up'][1][1] or all['back'][2][2] != all['back'][1][1] or all['right'][0][2] != all['right'][1][1]):
		step_two_3(all, debug)
	if (all['up'][0][0] != all['up'][1][1] or all['back'][2][0] != all['back'][1][1] or all['left'][0][0] != all['left'][1][1]):
		step_two_4(all, debug)

def step_three_1(all, debug):
	debug = 0
	for i in range(4):
		if (all['front'][2][1] == all['front'][1][1] and all['down'][0][1] == all['left'][1][1]):
			if (debug > 0):
				print("three_left" + " " + str(debug))
			input_to_cube(all, ["D", "L", "D'", "L'", "D'", "F'", "D", "F"])
		if (all['front'][2][1] == all['front'][1][1] and all['down'][0][1] == all['right'][1][1]):
			if (debug  > 1):
				print("three_right" + " " + str(debug))
			input_to_cube(all, ["D'", "R'", "D", "R", "D", "F", "D'", "F'"])
		input_to_cube(all, ["D"])

def step_three_1_all_sides(all, debug = 0):
	for i in range(4):
		if (all['front'][1][0] != all['front'][1][1] or all['front'][1][2] != all['front'][1][1] or all['left'][1][2] != all['left'][1][1] or all['left'][1][0] != all['right'][1][1] ):
			step_three_1(all, i + 1)
		spin_cube_left(all)

def	step_three_ok(all):
	c = 0
	if (all['front'][1][0] == all['front'][1][1] and all['front'][1][2] == all['front'][1][1]):
		c +=1
	if (all['left'][1][0] == all['left'][1][1] and all['left'][1][2] == all['left'][1][1]):
		c +=1
	if (all['right'][1][0] == all['right'][1][1] and all['right'][1][2] == all['right'][1][1]):
		c +=1
	if (all['back'][1][0] == all['back'][1][1] and all['back'][1][2] == all['back'][1][1]):
		c +=1
	if c == 4:
		return (True)
	return (False)


def step_three_all(all, debug = 0):
	i = 0
	step_three_1_all_sides(all, debug)
	while (step_three_ok(all) == False and i < 32):
		if ((all['front'][1][0] != all['front'][1][1] and all['left'][1][2] != all['left'][1][1]) or (all['front'][1][2] != all['front'][1][1] and all['right'][1][0] != all['right'][1][1])):
			if (all['front'][1][0] == all['left'][1][1] and all['left'][1][2] == all['front'][1][1]):
				input_to_cube(all, ["D", "L", "D'", "L'", "D'", "F'", "D", "F"])
				step_three_1_all_sides(all, debug)
			if (all['front'][1][0] == all['right'][1][1] and all['right'][1][0] == all['front'][1][1]):
				input_to_cube(all, ["D'", "R'", "D", "R", "D", "F", "D'", "F'"])
				step_three_1_all_sides(all, debug)
			if (all['right'][1][2] == all['front'][1][1] and (all['back'][1][2] == all['left'][1][1] or all['back'][1][2] == all['right'][1][1])) or (all['back'][1][2] == all['front'][1][1] and (all['left'][1][2] == all['left'][1][1] or all['left'][1][2] == all['right'][1][1])):
				spin_cube_left(all)
				input_to_cube(all, ["D'", "R'", "D", "R", "D", "F", "D'", "F'"])
				spin_cube_left(all)
				spin_cube_left(all)
				spin_cube_left(all)
				step_three_1_all_sides(all, debug)
			if (all['left'][1][2] == all['front'][1][1] and (all['back'][1][0] == all['left'][1][1] or all['back'][1][0] == all['right'][1][1])) or (all['back'][1][0] == all['front'][1][1] and (all['left'][1][0] == all['left'][1][1] or all['left'][1][0] == all['right'][1][1])):
				spin_cube_left(all)
				spin_cube_left(all)
				input_to_cube(all, ["D'", "R'", "D", "R", "D", "F", "D'", "F'"])
				spin_cube_left(all)
				spin_cube_left(all)
				step_three_1_all_sides(all, debug)
		if (all['left'][1][2] == all['right'][1][1] and all['front'][1][0] == all['front'][1][1]):
			input_to_cube(all, ["D", "L", "D'", "L'", "D'", "F'", "D", "F"])
			step_three_1_all_sides(all, debug)
		if (all['right'][1][0] == all['left'][1][1] and all['front'][1][2] == all['front'][1][1]):
			input_to_cube(all, ["D'", "R'", "D", "R", "D", "F", "D'", "F'"])
			step_three_1_all_sides(all, debug)
		spin_cube_left(all)
		i += 1
		step_three_1_all_sides(all, debug)

def step_four_all(all, debug = 0):
	for i in range(12):
		c = 2
		if (all['down'][0][1] == all['down'][1][1] and all['down'][1][2] == all['down'][1][1] and  all['down'][1][0] != all['down'][1][1] and  all['down'][2][1] != all['down'][1][1]):
			if (debug > 0):
				print ("four_1")
			spin_cube_left(all)
		elif (all['down'][0][1] != all['down'][1][1] and all['down'][1][2] == all['down'][1][1] and  all['down'][1][0] != all['down'][1][1] and  all['down'][2][1] == all['down'][1][1]):
			if (debug > 0):
				print ("four_2")
			spin_cube_left(all)
			spin_cube_left(all)
			spin_cube_left(all)
		elif (all['down'][0][1] != all['down'][1][1] and all['down'][1][2] == all['down'][1][1] and  all['down'][1][0] == all['down'][1][1] and  all['down'][2][1] != all['down'][1][1]):
			if (c % 2 == 0):
				input_to_cube(all, ["F'", "R'", "D'", "R", "D", "F"])
			else:
				c += 1
				spin_cube_left(all)
				spin_cube_left(all)
			if (debug > 0):
				print("four_3")
		else:
			spin_cube_left(all)
		if (all['down'][0][1] == all['down'][1][1] and all['down'][1][2] == all['down'][1][1] and all['down'][1][0] == all['down'][1][1] and all['down'][2][1] == all['down'][1][1]):
			break
		input_to_cube(all, ["F'", "R'", "D'", "R", "D", "F"])
	while (all['front'][1][1] != 0):
		spin_cube_left(all)

def sides_help_counter(all):
	c = 0
	if (all['front'][2][1] == all['front'][1][1]):
		c+= 1
	if (all['left'][2][1] == all['left'][1][1]):
		c+= 1
	if (all['right'][2][1] == all['right'][1][1]):
		c+= 1
	if (all['back'][0][1] == all['back'][1][1]):
		c+= 1
	return (c)

def rotate_down(all, debug = 0):
	i = 0
	while (i < 4 and sides_help_counter(all) < 2):
		input_to_cube(all, ["D"])
		if (debug > 0):
			print ("five")
		i += 1

def step_five_all(all):
	rotate_down(all)
	if (sides_help_counter(all) < 4):
		if ((all['front'][2][1] == all['back'][1][1] and all['back'][0][1] == all['front'][1][1]) or (all['right'][2][1] == all['left'][1][1] and all['left'][2][1] == all['right'][1][1])):
			input_to_cube(all, ["R'", "D'", "R", "D'", "R'", "D'", "D'", "R"])
			rotate_down(all)
		if (all['front'][2][1] == all['front'][1][1] and all['right'][2][1] == all['right'][1][1]):
			spin_cube_left(all)
			spin_cube_left(all)
			spin_cube_left(all)
		if (all['front'][2][1] == all['front'][1][1] and all['left'][2][1] == all['left'][1][1]):
			spin_cube_left(all)
			spin_cube_left(all)
		if (all['back'][0][1] == all['back'][1][1] and all['left'][2][1] == all['left'][1][1]):
			spin_cube_left(all)
		input_to_cube(all, ["R'", "D'", "R", "D'", "R'", "D'", "D'", "R", "D'"])
		while (all['front'][1][1] != 0):
			spin_cube_left(all)

def step_six_all(all):
	if not (check_angular(all, ["left", "front", "down"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0]) or check_angular(all, ["left", "back", "down"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0]) or check_angular(all, ["right", "back", "down"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2]) or check_angular(all, ["right", "front", "down"], ["right", "front", "down"], [2, 0, 2, 2, 0, 2])):
		input_to_cube(all, ["D'", "R'", "D", "L", "D'", "R", "D", "L'"])
	if (check_angular(all, ["left", "front", "down"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0])):
		spin_cube_left(all)
		spin_cube_left(all)
		spin_cube_left(all)		
	elif (check_angular(all, ["left", "back", "down"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0])):
		spin_cube_left(all)
		spin_cube_left(all)
	elif (check_angular(all, ["right", "back", "down"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2])):
		spin_cube_left(all)
	elif (check_angular(all, ["right", "front", "down"], ["right", "front", "down"], [2, 0, 2, 2, 0, 2])):
		pass
	i = 0
	while not (check_angular(all, ["left", "front", "down"], ["left", "front", "down"], [2, 2, 2, 0, 0, 0]) and check_angular(all, ["left", "back", "down"], ["left", "back", "down"], [2, 0, 0, 0, 2, 0]) and check_angular(all, ["right", "back", "down"], ["right", "back", "down"], [2, 2, 0, 2, 2, 2]) and check_angular(all, ["right", "front", "down"], ["right", "front", "down"], [2, 0, 2, 2, 0, 2])) and i < 17:
		input_to_cube(all, ["D'", "R'", "D", "L", "D'", "R", "D", "L'"])
		i += 1
	while (all['front'][1][1] != 0):
		spin_cube_left(all)

def step_seven_all(all):
	i = 0
	while (all['front'][2][2] != all['front'][1][1] or all['right'][2][0] != all['right'][1][1] or all['down'][0][2] != all['down'][1][1]) and i < 17:
		input_to_cube(all, ["R", "U", "R'", "U'"])
		i += 1
	input_to_cube(all, ["D'"])
	i = 0
	while (all['front'][2][2] != all['right'][1][1] or all['right'][2][0] != all['back'][1][1] or all['down'][0][2] != all['down'][1][1]) and i < 17:
		input_to_cube(all, ["R", "U", "R'", "U'"])
		i += 1
	input_to_cube(all, ["D'"])
	i = 0
	while (all['front'][2][2] != all['back'][1][1] or all['right'][2][0] != all['left'][1][1] or all['down'][0][2] != all['down'][1][1]) and i < 17:
		input_to_cube(all, ["R", "U", "R'", "U'"])
		i += 1
	input_to_cube(all, ["D'"])
	i = 0
	while (all['front'][2][2] != all['left'][1][1] or all['right'][2][0] != all['front'][1][1] or all['down'][0][2] != all['down'][1][1]) and i < 17:
		input_to_cube(all, ["R", "U", "R'", "U'"])
		i += 1
	input_to_cube(all, ["D'"])

def s_r_optimizator():
	i = 0
	while i < len(s_r):
		tmp = s_r[i]
		if len(s_r) - i > 4:
			x = i
			mx = x + 4
			c = 0
			while x < mx:
				if (tmp == s_r[x]):
					c += 1
				x+= 1
			if (c == 4):
				x = i
				for m in range(4):
					s_r.pop(x)
		i+= 1

def start_function(all):
	result = None
	print('----start cube----')
	out_cube(all)
	print('----process solve----')
	if not cube_done(all):
		if all['up'][0][1] == all['up'][1][1] and all['up'][1][0] == all['up'][1][1] and\
		 all['up'][1][2] == all['up'][1][1] and all['up'][2][1] == all['up'][1][1]:
			while all['front'][0][1] != all['front'][1][1]:
				input_to_cube(all, ["U'"])
		step_one_all(all)
		if not cube_done(all):
			step_two_all(all)
		if not cube_done(all):
			step_three_all(all)
		if not cube_done(all):
			step_four_all(all)
		if not cube_done(all):
			step_five_all(all)
		if not cube_done(all):
			step_six_all(all)
		if not cube_done(all):
			step_seven_all(all)
		if not cube_done(all):
			print("solve error")
		else:
			print("cube solved")
		s_r_optimizator()
		result = out_sr(s_r.copy())
	else:
		print("cube ok")
	print('----end cube----')
	out_cube(all)

	return s_r, result
				