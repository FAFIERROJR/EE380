import numpy as np

trials = 1000000
P = np.array([[.5, .3 , .2], [.2, .6, .2], [.3, .2, .5]])
rolls = np.random.rand(trials)

daysElapsed = 0
daysElapsedA = list()

state = 2
for i in range(trials):
	sum = 0
	for k in range(3):
		sum = sum + P[state, k]
		if(rolls[i] <= sum):
			state = k
			break
	daysElapsed = daysElapsed + 1
	if(state != 2):
		daysElapsedA.append(daysElapsed)
		daysElapsed = 0
		state = 2

mean = np.mean(daysElapsedA)
print(" By simulation, the expected number days until it gets better = " + str(mean))
P0 = np.array([[0, .3 , .2], [0, .6, .2], [0, .2, .5]])

I = np.identity(3)

diff = np.subtract(I,P0)

inverse = np.linalg.inv(diff)

M = [[1],[1],[1]]

m0 = np.dot(inverse,M)

P1 = np.array([[.5, 0 , .2], [.2, 0, .2], [.3, 0, .5]])

I = np.identity(3)

diff = np.subtract(I,P1)

inverse = np.linalg.inv(diff)

M = [[1],[1],[1]]

m1= np.dot(inverse,M)


mathmean = float(1/(1/m0[2] + 1/m1[2]))

print(" By math, the expected number days until it gets better= " + str(mathmean)) 
