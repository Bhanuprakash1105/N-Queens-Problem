title = "AI Assignment 2"

screen_size = (None, None)
screen_color = (85, 60, 42)

box_width = box_height = None
rows = columns = None
border_thickness = None

num_of_queens = 4

def set_display_values(width, height, num_of_boxes = None):
	global screen_size, box_width, box_height
	global rows, columns, border_thickness
	if num_of_boxes == None:
		num_of_boxes = num_of_queens
	rows = columns = num_of_boxes
	grid_size = min(width * 0.8, height * 0.8)
	box_width = box_height = grid_size / num_of_boxes
	border_thickness = box_width * 0.05
	box_width -= border_thickness
	box_height -= border_thickness
	screen_size = (grid_size, grid_size)

white_box = (255, 255, 255)
black_box = (0, 0, 0)
queen_color = (0, 102, 255)

sleep_time_sec = 0.5