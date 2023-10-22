def out_sr(s_r):
	combination = [{"", ""},
					{"'", "'"},
					{"", "'"},
					{"2", "2"},
					{"2", ""},
					{"2", "'"}]
	after_union = ["2", "2", None, None, "'", ""]
	side_faces = ["L", "F", "R", "B"]
	new = []
	hand_right = None
	hand_left = None
	y = 0
	for index, value in enumerate(s_r):
		if value == "y":
			y += 1
			continue
		if value[0] in side_faces:
			c_index = side_faces.index(value[0])
			if len(value) > 1:
				s_r[index] = side_faces[(c_index + y) % 4] + value[1::]
			else:
				s_r[index] = side_faces[(c_index + y) % 4]

	while len(s_r) > 0 or not (hand_right is None):
		if hand_right == None:
			hand_right = s_r.pop(0)
		if hand_right == "y":
			hand_right = None
			continue
		if len(new) > 0:
			hand_left =  new.pop()
			c_right = hand_right[0]
			c_left = hand_left[0]
			if c_right == c_left:
				if len(hand_left) < 2:
					left = ""
				else:
					left = hand_left[1]
				if len(hand_right) < 2:
					right = ""
				else:
					right = hand_right[1]
				tmp = {left, right}
				if tmp in combination:
					i = combination.index(tmp)
					if after_union[i] is None:
						hand_right = None
					else:
						hand_right = c_right + after_union[i]
					hand_left = None
				else:
					new.append(hand_left)
					hand_left = None
					new.append(hand_right)
					hand_right = None
			else:
				new.append(hand_left)
				hand_left = None
				new.append(hand_right)
				hand_right = None
		else:
			new.append(hand_right)
			hand_right = None

	print("Number of spins in the solution:", len(new))
	print("Solution:")
	result = " ".join(new)
	print(result)
	return (result)