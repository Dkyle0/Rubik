from ursina import *

class Game(Ursina):
	def __init__(self, all, movements, solve):
		super().__init__()
		window.exit_button.enabled = False
		window.fullscreen = True
		window.title = "Rubik"
		Entity(model='quad', scale=60, texture='white_cube', texture_scale=(60, 60), rotation_x=90, y=-5,
				color=color.light_gray)  # plane
		Entity(model='sphere', scale=150, texture='textures/sky0', double_sided=True)  # sky
		EditorCamera()
		camera.world_position = (0, 0, -15)
		self.model, self.texture = 'models/custom_cube', 'textures/rubik_texture'
		self.all = all
		self.solve = solve
		self.one = 0
		self.movements = movements
		self.step = len(solve)
		self.load_game()

	def load_game(self):
		self.create_cube_positions()
		self.CUBES = [Entity(model=self.model, texture=self.texture, position=pos) for pos in self.SIDE_POSITIONS]
		self.PARENT = Entity()
		self.rotation_axes = {"L'": 'x', 'L': 'qx', 'R': 'x', "R'": 'qx', 'U': 'y', "U'": 'qy', 'D': 'qy', "D'": 'y', 'F': 'z', "F'": 'qz', 'B': 'qz', "B'": 'z'}
		self.cubes_side_positons = {'L': self.L, "L'": self.L, 'D': self.D, "D'": self.D, 'R': self.R, "R'": self.R, 'F': self.F, "F'": self.F, 'B': self.B, "B'": self.B,'U': self.U, "U'": self.U}
		self.animation_time = 0.4
		self.rot = 0
		self.action_trigger = True
		self.action_mode = True
		self.message = Text(origin=(0, 19), color=color.black)
		self.toggle_game_mode()
		self.start_state()

	def start_state(self):
		for m in self.movements:
			self.rotate_side_without_animation(m)

	def rotate_side_without_animation(self, side_name):
		cube_positions = self.cubes_side_positons[side_name]
		rotation_axis = self.rotation_axes[side_name]
		self.reparent_to_scene()
		for cube in self.CUBES:
			if cube.position in cube_positions:
				cube.parent = self.PARENT
				if(rotation_axis[0] != "q"):
					exec(f'self.PARENT.rotation_{rotation_axis} = 90')
				else:
					exec(f'self.PARENT.rotation_{rotation_axis[1]} = -90')

	def toggle_game_mode(self):
		self.action_mode = not self.action_mode
		msg = dedent(f"{'ACTION mode ON' if self.action_mode else 'VIEW mode ON'}"
					 f" (to switch - press middle mouse button, to start press space)").strip()
		self.message.text = msg

	def toggle_animation_trigger(self):
		self.action_trigger = not self.action_trigger

	def rotate_side(self, side_name):
		if (side_name != "y"):
			self.action_trigger = False
			cube_positions = self.cubes_side_positons[side_name]
			rotation_axis = self.rotation_axes[side_name]
			self.reparent_to_scene()
			for cube in self.CUBES:
				if cube.position in cube_positions:
					cube.parent = self.PARENT
					if(rotation_axis[0] != "q"):
						eval(f'self.PARENT.animate_rotation_{rotation_axis}(90, duration=self.animation_time)')
					else:
						eval(f'self.PARENT.animate_rotation_{rotation_axis[1]}(-90, duration=self.animation_time)')
			invoke(self.toggle_animation_trigger, delay=self.animation_time + 0.11)
		else:
			self.spin_y()

	def reparent_to_scene(self):
		for cube in self.CUBES:
			if cube.parent == self.PARENT:
				world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation
				cube.parent = scene
				cube.position, cube.rotation = world_pos, world_rot
		self.PARENT.rotation = 0

	def create_cube_positions(self):
		self.L = {Vec3(-1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
		self.D = {Vec3(x, -1, z) for x in range(-1, 2) for z in range(-1, 2)}
		self.F = {Vec3(x, y, -1) for x in range(-1, 2) for y in range(-1, 2)}
		self.B = {Vec3(x, y, 1) for x in range(-1, 2) for y in range(-1, 2)}
		self.R = {Vec3(1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
		self.U = {Vec3(x, 1, z) for x in range(-1, 2) for z in range(-1, 2)}
		self.SIDE_POSITIONS = self.L | self.D | self.F | self.B | self.R | self.U

	def animation_solve(self):
		t = self.animation_time
		for m in self.solve:
			invoke(self.rotate_side, m, delay=t + 0.11)
			t += self.animation_time + 0.11
		invoke(self.toggle_animation_trigger, delay=t + 0.11)

	def spin_y(self):
		self.action_trigger = False
		self.reparent_to_scene()
		for cube in self.CUBES:
			cube.parent = self.PARENT
			self.PARENT.animate_rotation_y(90, self.animation_time)
		invoke(self.toggle_animation_trigger, delay=self.animation_time + 0.11)

	def input(self, key):
		if (key == "arrow_left" and self.one == 1 and self.action_mode and self.action_trigger):
			if self.step > 0:
				if self.step >= len(self.solve):
					self.step = len(self.solve) - 1
				else:
					self.step -= 1
				if len(self.solve[self.step]) == 2 or self.solve[self.step] == "y":
					self.rotate_side(self.solve[self.step][0])
				else:
					self.rotate_side(self.solve[self.step] + "'")
		if (key == "arrow_right" and self.one == 1 and self.action_mode and self.action_trigger):
			if (self.step == -1):
				self.step += 1
			if self.step < len(self.solve):
				self.rotate_side(self.solve[self.step])
				self.step += 1
		if (key == "space" and self.action_trigger and self.one == 0):
			self.animation_solve()
			self.one = 1
		if (key == "w" and self.action_mode and self.action_trigger and self.one != 1):
			self.spin_y()
			self.one = 2
		if (key == "1" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("L")
			self.one = 2
		if (key == "4" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("L'")
			self.one = 2
		if (key == "3" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("R'")
			self.one = 2
		if (key == "6" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("R")
			self.one = 2
		if (key == "0" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("D")
			self.one = 2
		if (key == "." and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("D'")
			self.one = 2
		if (key == "7" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("U")
			self.one = 2
		if (key == "9" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("U'")
			self.one = 2
		if (key == "2" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("B")
			self.one = 2
		if (key == "5" and self.action_mode and self.action_trigger and self.one != 1):
			self.rotate_side("B'")
			self.one = 2
		if (key == "escape"):
			exit()
		if key == 'mouse2':
			self.toggle_game_mode()
		super().input(key)
