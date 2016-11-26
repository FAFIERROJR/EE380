import numpy as np

trials = 100000
P = np.array([[.5, .3 , .2], [.2, .6, .2], [.3, .2, .5]])
rolls = np.random.rand(trials,7)
numGoodDaysA = np.zeros(trials)

for i in range(trials):
	state = 2
	goodDays = 0
	for j in range(7):
		sum = 0
		for k in range(3):
			sum = sum + P[state, k]
			if(rolls[i,j] <= sum):
				state = k
				break
		if(state == 0):
			goodDays = goodDays + 1
	numGoodDaysA[i] = goodDays

mean = np.mean(numGoodDaysA)

print(" By simulation, the expected number of good days = " + str(mean)) 