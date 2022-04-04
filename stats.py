import sys
from random import randint, choices
import matplotlib.pyplot as plt
import const

shoulder_check = False
if len(sys.argv) >= 2 and sys.argv[1].isnumeric():	
	const.num_of_queens = int(sys.argv[1])
if '-sc' in sys.argv:
	shoulder_check = True

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
	queens = init_random_pos_queens(const.num_of_queens)
	num_of_conflicts = evaluation_function(queens)
	# print("\n<< Number of pairs of queens attacking each other = ", num_of_conflicts)
	new_state = generate_successor_states(queens, num_of_conflicts)
	while new_state != None:
		queen, new_loc, num_of_conflicts = new_state
		queens[queen] = new_loc
		# print("\n<< Number of pairs of queens attacking each other = ", num_of_conflicts)
		new_state = generate_successor_states(queens, num_of_conflicts)
	return num_of_conflicts

x = list(range(20))
y = []
for itr in x:
	y.append(main())

figure, axis = plt.subplots(1, 2)

axis[0].plot(x, y, color='green', linewidth = 3, marker='o', markerfacecolor='blue', markersize=8)
axis[0].set_xticks(x)
axis[0].set_yticks(y)
axis[0].set_xlabel('Iteration')
axis[0].set_ylabel('Num of conflicts')
axis[0].set_title(f'{const.num_of_queens} - queens')

y_freq = {}
for i in y:
	y_freq[i] = y_freq.get(i, 0) + 1
x = [k for k in y_freq.keys()]
y = [y_freq[k] for k in y_freq]

axis[1].bar(x, y, tick_label = x, width = 0.8, color = ['blue'])
axis[1].set_xticks(x)
axis[1].set_yticks(y)
axis[1].set_xlabel('Num of conflicts')
axis[1].set_ylabel('Frequency')
axis[1].set_title(f'{const.num_of_queens} - queens')

plt.show()