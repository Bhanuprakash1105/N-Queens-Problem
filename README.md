# N-Queens

**What is N-Queens problem ?**

Given N x N chess board with N queens where each column contains 1 queen the solution is about finding the positions of queens in the chess board such that no queen is attacking any other queen. Basically minimum number of pairs of queens attacking each other and ideally that value should zero(0). But there are few values of N for which the solution doesn't exists for example when N = 2, 3 there is not solution as shown in below image.

<img src="https://github.com/Bhanuprakash1105/N-Queens-Problem/blob/main/Images/solutions-space.jpg" width="430" height="410">

For more information about N-Queens problem refer ![this link](https://en.wikipedia.org/wiki/Eight_queens_puzzle) where N = 8

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
