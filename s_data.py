x_r = ["front", "right", "back", "left"]
x_l = ["front", "left", "back", "right"]
y_u = ["front", "up", "back", "down"]
y_d = ["front", "down", "back", "up"]
s_str = ["front", "back", "up", "down", "left", "right"]
s_r = []

def init_all(all):
	all_side = []
	for i in range(6):
		all_side.append([])
		for y in range(3):
			all_side[i].append([])
			for x in range(3):
				all_side[i][y].append(i) #  x + y * 3
	for i in range(6):
		all[s_str[i]] = all_side[i]

def spin_right(all, side, test_mode = 0):
	if test_mode == 1:
		i = 0
		for y in range(3):
			for x in range(3):
				all[side][y][x] = i
				i += 1
		print(all[side][0][0], all[side][0][1], all[side][0][2])
		print(all[side][1][0], all[side][1][1], all[side][1][2])
		print(all[side][2][0], all[side][2][1], all[side][2][2])
		print("-")
	t1 = all[side][0][0]
	t2 = all[side][1][0]
	all[side][0][0] = all[side][2][0]
	all[side][1][0] = all[side][2][1]
	all[side][2][0] = all[side][2][2]
	all[side][2][0] = all[side][2][2]
	all[side][2][1] = all[side][1][2]
	all[side][2][2] = all[side][0][2]
	all[side][1][2] = all[side][0][1]
	all[side][0][2] = t1
	all[side][0][1] = t2
	if test_mode == 1:
		print(all[side][0][0], all[side][0][1], all[side][0][2])
		print(all[side][1][0], all[side][1][1], all[side][1][2])
		print(all[side][2][0], all[side][2][1], all[side][2][2])	

def left_d(all): # L
	t1 = all['front'][0][0]
	t2 = all['front'][1][0]
	t3 = all['front'][2][0]
	all['front'][0][0] = all['up'][0][0]
	all['front'][1][0] = all['up'][1][0]
	all['front'][2][0] = all['up'][2][0]
	all['up'][0][0] = all['back'][0][0]
	all['up'][1][0] = all['back'][1][0]
	all['up'][2][0] = all['back'][2][0]
	all['back'][0][0] = all['down'][0][0]
	all['back'][1][0] = all['down'][1][0]
	all['back'][2][0] = all['down'][2][0]
	all['down'][0][0] = t1
	all['down'][1][0] = t2
	all['down'][2][0] = t3
	spin_right(all, 'left', 0)

def spin_left(all, side, test_mode = 0):
	if test_mode == 1:
		i = 0
		for y in range(3):
			for x in range(3):
				all[side][y][x] = i
				i += 1
		print(all[side][0][0], all[side][0][1], all[side][0][2])
		print(all[side][1][0], all[side][1][1], all[side][1][2])
		print(all[side][2][0], all[side][2][1], all[side][2][2])
		print("-")
	t1 = all[side][0][0]
	t2 = all[side][1][0]
	all[side][0][0] = all[side][0][2]
	all[side][1][0] = all[side][0][1]
	all[side][0][1] = all[side][1][2]
	all[side][0][2] = all[side][2][2]
	all[side][1][2] = all[side][2][1]
	all[side][2][2] = all[side][2][0]
	all[side][2][0] = t1
	all[side][2][1] = t2
	if test_mode == 1:
		print(all[side][0][0], all[side][0][1], all[side][0][2])
		print(all[side][1][0], all[side][1][1], all[side][1][2])
		print(all[side][2][0], all[side][2][1], all[side][2][2])	

def left_u(all): # l'
	t1 = all['front'][0][0]
	t2 = all['front'][1][0]
	t3 = all['front'][2][0]
	i = 1;
	for side in y_d:
			all[side][0][0] = all[y_d[i]][0][0]
			all[side][1][0] = all[y_d[i]][1][0]
			all[side][2][0] = all[y_d[i]][2][0]
			i += 1
			if i > 3:
				i = 0
	all['up'][0][0] = t1
	all['up'][1][0] = t2
	all['up'][2][0] = t3
	spin_left(all, 'left', 0)


def right_u(all): #R
	t1 = all['front'][0][2]
	t2 = all['front'][1][2]
	t3 = all['front'][2][2]
	i = 1;
	for side in y_d:
			all[side][0][2] = all[y_d[i]][0][2]
			all[side][1][2] = all[y_d[i]][1][2]
			all[side][2][2] = all[y_d[i]][2][2]
			i += 1
			if i > 3:
				i = 0
	all['up'][0][2] = t1
	all['up'][1][2] = t2
	all['up'][2][2] = t3
	spin_right(all, 'right', 0)

def right_d(all): #R'
	t1 = all['front'][0][2]
	t2 = all['front'][1][2]
	t3 = all['front'][2][2]
	i = 1;
	for side in y_u:
			all[side][0][2] = all[y_u[i]][0][2]
			all[side][1][2] = all[y_u[i]][1][2]
			all[side][2][2] = all[y_u[i]][2][2]
			i += 1
			if i > 3:
				i = 0
	all['down'][0][2] = t1
	all['down'][1][2] = t2
	all['down'][2][2] = t3
	spin_left(all, 'right', 0)

def up_l(all): #U
	t1 = all['front'][0][0]
	t2 = all['front'][0][1]
	t3 = all['front'][0][2]
	all['front'][0][0] = all['right'][0][0]
	all['front'][0][1] = all['right'][0][1]
	all['front'][0][2] = all['right'][0][2]
	all['right'][0][0] = all['back'][2][2]
	all['right'][0][1] = all['back'][2][1]
	all['right'][0][2] = all['back'][2][0]
	all['back'][2][2] = all['left'][0][0]
	all['back'][2][1] = all['left'][0][1]
	all['back'][2][0] = all['left'][0][2]
	all['left'][0][0] = t1
	all['left'][0][1] = t2
	all['left'][0][2] = t3
	spin_right(all, 'up', 0)

def up_r(all): #U'
	t1 = all['front'][0][0]
	t2 = all['front'][0][1]
	t3 = all['front'][0][2]
	all['front'][0][0] = all['left'][0][0]
	all['front'][0][1] = all['left'][0][1]
	all['front'][0][2] = all['left'][0][2]
	all['left'][0][0] = all['back'][2][2]
	all['left'][0][1] =	all['back'][2][1]
	all['left'][0][2] =	all['back'][2][0]
	all['back'][2][2] = all['right'][0][0]
	all['back'][2][1] = all['right'][0][1]
	all['back'][2][0] = all['right'][0][2]
	all['right'][0][0] = t1
	all['right'][0][1] = t2
	all['right'][0][2] = t3
	spin_left(all, 'up', 0)

def down_r(all): #D
	t1 = all['front'][2][0]
	t2 = all['front'][2][1]
	t3 = all['front'][2][2]
	all['front'][2][0] = all['left'][2][0]
	all['front'][2][1] = all['left'][2][1]
	all['front'][2][2] = all['left'][2][2]
	all['left'][2][0] = all['back'][0][2]
	all['left'][2][1] =	all['back'][0][1]
	all['left'][2][2] =	all['back'][0][0]
	all['back'][0][2] = all['right'][2][0]
	all['back'][0][1] = all['right'][2][1]
	all['back'][0][0] = all['right'][2][2]
	all['right'][2][0] = t1
	all['right'][2][1] = t2
	all['right'][2][2] = t3
	spin_right(all, 'down', 0)

def  down_l(all): #D'
	t1 = all['front'][2][0]
	t2 = all['front'][2][1]
	t3 = all['front'][2][2]
	all['front'][2][0] = all['right'][2][0]
	all['front'][2][1] = all['right'][2][1]
	all['front'][2][2] = all['right'][2][2]
	all['right'][2][0] = all['back'][0][2]
	all['right'][2][1] = all['back'][0][1]
	all['right'][2][2] = all['back'][0][0]
	all['back'][0][2] = all['left'][2][0]
	all['back'][0][1] = all['left'][2][1]
	all['back'][0][0] = all['left'][2][2]
	all['left'][2][0] = t1
	all['left'][2][1] = t2
	all['left'][2][2] = t3
	spin_left(all, 'down')

def front_r(all): #F
	t1 = all['up'][2][0]
	t2 = all['up'][2][1]
	t3 = all['up'][2][2]
	all['up'][2][2] = all['left'][0][2]
	all['up'][2][1] = all['left'][1][2]
	all['up'][2][0] = all['left'][2][2]
	all['left'][0][2] = all['down'][0][0]
	all['left'][1][2] = all['down'][0][1]
	all['left'][2][2] = all['down'][0][2]
	all['down'][0][0] = all['right'][2][0]
	all['down'][0][1] = all['right'][1][0]
	all['down'][0][2] = all['right'][0][0]
	all['right'][0][0] = t1
	all['right'][1][0] = t2
	all['right'][2][0] = t3
	spin_right(all, 'front')

def front_l(all): #F'
	t1 = all['up'][2][0]
	t2 = all['up'][2][1]
	t3 = all['up'][2][2]
	all['up'][2][2] = all['right'][2][0]
	all['up'][2][1] = all['right'][1][0]
	all['up'][2][0] = all['right'][0][0]
	all['right'][0][0] = all['down'][0][2]
	all['right'][1][0] = all['down'][0][1]
	all['right'][2][0] = all['down'][0][0]
	all['down'][0][0] = all['left'][0][2]
	all['down'][0][1] = all['left'][1][2]
	all['down'][0][2] = all['left'][2][2]
	all['left'][0][2] = t3
	all['left'][1][2] = t2
	all['left'][2][2] = t1
	spin_left(all, 'front')

def spin_cube_left(all):
	t1, t2, t3, t4, t5, t6, t7, t8, t9 = all['front'][0][0], all['front'][0][1], all['front'][0][2], all['front'][1][0], all['front'][1][1], all['front'][1][2], all['front'][2][0], all['front'][2][1], all['front'][2][2]
	all['front'][0][0], all['front'][0][1], all['front'][0][2], all['front'][1][0], all['front'][1][1], all['front'][1][2], all['front'][2][0], all['front'][2][1], all['front'][2][2] = all["right"][0][0], all["right"][0][1], all["right"][0][2], all["right"][1][0], all["right"][1][1], all["right"][1][2], all["right"][2][0], all["right"][2][1], all["right"][2][2]
	all["right"][0][0], all["right"][0][1], all["right"][0][2], all["right"][1][0], all["right"][1][1], all["right"][1][2], all["right"][2][0], all["right"][2][1], all["right"][2][2] = all['back'][2][2], all['back'][2][1], all['back'][2][0], all['back'][1][2], all['back'][1][1], all['back'][1][0], all['back'][0][2], all['back'][0][1], all['back'][0][0]
	all["back"][0][0], all["back"][0][1], all["back"][0][2], all["back"][1][0], all["back"][1][1], all["back"][1][2], all["back"][2][0], all["back"][2][1], all["back"][2][2] = all["left"][2][2], all["left"][2][1], all["left"][2][0], all["left"][1][2], all["left"][1][1], all["left"][1][0], all["left"][0][2], all["left"][0][1], all["left"][0][0]
	all['left'][0][0], all['left'][0][1], all['left'][0][2], all['left'][1][0], all['left'][1][1], all['left'][1][2], all['left'][2][0], all['left'][2][1], all['left'][2][2] = t1, t2, t3, t4, t5, t6, t7, t8, t9
	spin_left(all, 'down')
	spin_right(all, 'up')
	s_r.append("y")

def back_l(all): #B
	t1 = all['up'][0][0]
	t2 = all['up'][0][1]
	t3 = all['up'][0][2]
	all['up'][0][2] = all['right'][2][2]
	all['up'][0][1] = all['right'][1][2]
	all['up'][0][0] = all['right'][0][2]
	all['right'][0][2] = all['down'][2][2]
	all['right'][1][2] = all['down'][2][1]
	all['right'][2][2] = all['down'][2][0]
	all['down'][2][0] = all['left'][0][0]
	all['down'][2][1] = all['left'][1][0]
	all['down'][2][2] = all['left'][2][0]
	all['left'][0][0] = t3
	all['left'][1][0] = t2
	all['left'][2][0] = t1
	spin_right(all, 'back')


def back_r(all): #B'
	t1 = all['up'][0][0]
	t2 = all['up'][0][1]
	t3 = all['up'][0][2]
	all['up'][0][2] = all['left'][0][0]
	all['up'][0][1] = all['left'][1][0]
	all['up'][0][0] = all['left'][2][0]
	all['left'][0][0] = all['down'][2][0]
	all['left'][1][0] = all['down'][2][1]
	all['left'][2][0] = all['down'][2][2]
	all['down'][2][0] = all['right'][2][2]
	all['down'][2][1] = all['right'][1][2]
	all['down'][2][2] = all['right'][0][2]
	all['right'][0][2] = t1
	all['right'][1][2] = t2
	all['right'][2][2] = t3
	spin_left(all, 'back')


def out_cube(all):
	print ('       ', all['up'][0][0], all['up'][0][1], all['up'][0][2])
	print ('       ', all['up'][1][0], all['up'][1][1], all['up'][1][2])
	print ('       ', all['up'][2][0], all['up'][2][1], all['up'][2][2])
	print (all['left'][0][0], all['left'][0][1], all['left'][0][2], ' ', all['front'][0][0], all['front'][0][1], all['front'][0][2], ' ', all['right'][0][0], all['right'][0][1], all['right'][0][2], ' ', all['back'][2][2], all['back'][2][1], all['back'][2][0])
	print (all['left'][1][0], all['left'][1][1], all['left'][1][2], ' ', all['front'][1][0], all['front'][1][1], all['front'][1][2], ' ', all['right'][1][0], all['right'][1][1], all['right'][1][2], ' ', all['back'][1][2], all['back'][1][1], all['back'][1][0])
	print (all['left'][2][0], all['left'][2][1], all['left'][2][2], ' ', all['front'][2][0], all['front'][2][1], all['front'][2][2], ' ', all['right'][2][0], all['right'][2][1], all['right'][2][2], ' ', all['back'][0][2], all['back'][0][1], all['back'][0][0])
	print ('       ', all['down'][0][0], all['down'][0][1], all['down'][0][2])
	print ('       ', all['down'][1][0], all['down'][1][1], all['down'][1][2])
	print ('       ', all['down'][2][0], all['down'][2][1], all['down'][2][2])

def input_to_cube(all, input, p = 1):
	for move in input:
		if move == "L":
			left_d(all)
			if p > 0:
				s_r.append("L")
		elif move == "L'":
			left_u(all)
			if p > 0:
				s_r.append("L'")
		elif move == "R":
			right_u(all)
			if p > 0:
				s_r.append("R")
		elif move == "R'":
			right_d(all)
			if p > 0:
				s_r.append("R'")
		elif move == "U":
			up_l(all)
			if p > 0:
				s_r.append("U")
		elif move == "U'":
			up_r(all)
			if p > 0:
				s_r.append("U'")
		elif move == "D":
			down_r(all)
			if p > 0:
				s_r.append("D")
		elif move == "D'":
			down_l(all)
			if p > 0:
				s_r.append("D'")
		elif move == "F":
			front_r(all)
			if p > 0:
				s_r.append("F")
		elif move == "F'":
			front_l(all)
			if p > 0:
				s_r.append("F'")
		elif move == "B":
			back_l(all)
			if p > 0:
				s_r.append("B")
		elif move == "B'":
			back_r(all)
			if p > 0:
				s_r.append("B'")
		else:
			print("error move")
