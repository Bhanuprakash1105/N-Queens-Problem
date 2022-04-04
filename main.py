import pygame
import sys
from time import sleep
from random import randint, choices
import const

shoulder_check = False
flat_limit = 16 # default num_of_queens = 4 so flat limit = 4 * 4 = 16
if len(sys.argv) >= 2 and sys.argv[1].isnumeric():	
	const.num_of_queens = int(sys.argv[1])
	flat_limit = const.num_of_queens * const.num_of_queens
if '-sc' in sys.argv:
	shoulder_check = True

pygame.init()
const.set_display_values(pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(const.screen_size)
screen.fill(const.screen_color)
pygame.display.set_caption(const.title)

def toggle_color(color):
	if color == const.white_box:
		return const.black_box
	return const.white_box

def generate_boxes():
	boxes = {}
	box_color = {}
	x, y = 0, 0
	color = const.white_box
	for i in range(0, const.rows):
		x = 0
		for j in range(0, const.columns):
			loc = (i, j)
			boxes[loc] = (const.border_thickness + x, const.border_thickness + y, const.box_width, const.box_height)
			box_color[loc] = color
			pygame.draw.rect(screen, color, boxes[loc])
			x += const.box_width + const.border_thickness
			color = toggle_color(color)
		if const.rows % 2 == 0:
			color = toggle_color(color)
		y += const.box_height + const.border_thickness
	pygame.display.update()
	return boxes, box_color

def draw_circle(color, box_loc):
	a, b, c, d = box_loc
	midx = (2 * a + c) / 2
	midy = (2 * b + d) / 2
	center = (midx, midy)
	radius = min(const.box_width, const.box_height) * 0.25
	pygame.draw.circle(screen, color, center, radius)
	pygame.display.update()

def reset_box_color(boxes, loc, color):
	pygame.draw.rect(screen, color, boxes[loc])
	pygame.display.update()

def update_queen_on_chess_board(boxes, loc):
	draw_circle(const.queen_color, boxes[loc])
	pygame.display.update()

def init_random_pos_queens(n):
	queens = []
	for column in range(n):
		row = randint(0, n - 1)
		queens.append((row, column))
	return queens

def evaluation_function(queens):
	num_of_queens = len(queens)
	num_of_conflicts = 0
	for i in range(num_of_queens):
		for j in range(i + 1, num_of_queens):
			if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
				num_of_conflicts += 1
			elif abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
				num_of_conflicts += 1
	return num_of_conflicts

def generate_successor_states(queens, prev_num_of_conflicts):
	if prev_num_of_conflicts == 0:
		return None
	num_of_queens = len(queens)
	# num_of_successor_states = num_of_queens * (num_of_queens - 1)
	successor_states = []
	total_num_of_conflicts = 0
	for i in range(num_of_queens):
		current_loc = queens[i]
		for j in range(1, num_of_queens):
			new_loc = ((current_loc[0] + j) % num_of_queens, current_loc[1])
			queens[i] = new_loc
			new_num_of_conflicts = evaluation_function(queens)
			queens[i] = current_loc
			if (new_num_of_conflicts < prev_num_of_conflicts)\
				 or (shoulder_check and (new_num_of_conflicts <= prev_num_of_conflicts)):
				state = (i, new_loc, new_num_of_conflicts)
				successor_states.append(state)
				if new_num_of_conflicts == 0:
					return state
				total_num_of_conflicts += new_num_of_conflicts
	if len(successor_states) == 0:
		return None
	state_weights = []
	for state in successor_states:
		num_of_conflicts = state[2]
		weightage = (total_num_of_conflicts - num_of_conflicts) / total_num_of_conflicts
		state_weights.append(weightage)
	new_state = choices(population=successor_states, weights=state_weights)[0]
	return new_state

def main():
	boxes, box_color = generate_boxes()
	queens = init_random_pos_queens(const.num_of_queens)
	for queen_loc in queens:
		update_queen_on_chess_board(boxes, queen_loc)
	num_of_conflicts = evaluation_function(queens)
	print("\n<< Number of pairs of queens attacking each other = ", num_of_conflicts)
	new_state = generate_successor_states(queens, num_of_conflicts)
	global flat_limit
	while new_state != None and flat_limit > 0:
		flat_limit -= 1
		sleep(const.sleep_time_sec)
		queen, new_loc, num_of_conflicts = new_state
		reset_box_color(boxes, queens[queen], box_color[queens[queen]])
		sleep(const.sleep_time_sec)
		update_queen_on_chess_board(boxes, new_loc)
		queens[queen] = new_loc
		print("\n<< Number of pairs of queens attacking each other = ", num_of_conflicts)
		new_state = generate_successor_states(queens, num_of_conflicts)
	if flat_limit == 0:
		print("\n<< Reached flat limit, stopped execution")
main()

def stop_display():
	for event in pygame.event.get():
		if event.type == pygame.QUIT: return True
	return False
while not stop_display():
	pass