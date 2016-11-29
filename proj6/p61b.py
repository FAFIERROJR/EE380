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

P0 = np.array([[0, .3 , .2], [0, .6, .2], [0, .2, .5]])

I = np.identity(3)

diff = np.subtract(I,P0)

inverse = np.linalg.inv(diff)

M = [[1],[1],[1]]

m = np.dot(inverse,M)

mathmean = float((7 - m[2])/m[0] + 1)

print("By math, the expected number of good days = " + str(mathmean))