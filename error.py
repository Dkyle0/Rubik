import sys
launching_program = "python3 rubik.py"
usage = """Usage:\t {0} <Rubik's cube movements> <flags>\n\n
		-h\thuman algorithm\n
		-e\textended input\n
		-t\tdo not run the visualizer\t
		-r\trandom cube rotations
		-d\tmode for developers to display human algorithms (only works with the -h flag)
		Examples:\n
		{0} "U D L F' R2"
		{0} "U D L F' R2 u d' l2 (f r2)4" "-e"
		{0} "10" "-rh\"""".format(launching_program)


def error_exit(error_msg, example_usage = False):
	print("Error: {}".format(error_msg))
	if example_usage:
		print(usage)
	sys.exit()
