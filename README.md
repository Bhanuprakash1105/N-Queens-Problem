# N-Queens

**What is N-Queens problem ?**

Given an N x N chess board with N queens where each column contains 1 queen, the solution is to find the positions of queens on the chess board such that no queen is attacking any other queen. Basically, the minimum number of pairs of queens attacking each other should be zero(0), ideally. However, there are a few N values for which there is no solution. When N is equal to 2 or 3, for example, there is no solution, as shown in the image below.

<img src="https://github.com/Bhanuprakash1105/N-Queens-Problem/blob/main/Images/solutions-space.jpg" width="430" height="410">

For more information about N-Queens problem refer ![this link](en.wikipedia.org/wiki/Eight_queens_puzzle) where N = 8

## Technical details

### Technologies used
* python
* pygame
* AI
* ![Stochastic hill climbing algorithm](https://en.wikipedia.org/wiki/Stochastic_hill_climbing)

### Execution description

* After installing the required libraries run the python code `main.py`

* `main.py` can take 2 input arguments N (+ve integer) and flag `-sc` where 'sc' represents shoulder check

* Default value of N = 4 and `-sc` set flag inputs a sample output can be seen below
<img src="https://github.com/Bhanuprakash1105/N-Queens-Problem/blob/main/Images/4x4.jpg" width="640" height="340">

* For value N = 8 and `-sc` set flag inputs a sample output can be seen below
<img src="https://github.com/Bhanuprakash1105/N-Queens-Problem/blob/main/Images/8x8.jpg" width="640" height="340">

* Below figure shows the statistics when the program is executed 20 times with N = 4 and `-sc` FLAG NOT PROVIDED
<img src="https://github.com/Bhanuprakash1105/N-Queens-Problem/blob/main/Images/output_stats.jpg" width="640" height="340">
