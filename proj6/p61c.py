import numpy as np

trials = 1000000
P = np.array([[.5, .3 , .2], [.2, .6, .2], [.3, .2, .5]])
rolls = np.random.rand(trials)

numGoodDays = 0

state = 2
for i in range(trials):
	sum = 0
	for k in range(3):
		sum = sum + P[state, k]
		if(rolls[i] <= sum):
			state = k
			break
	if(state == 0):
		numGoodDays = numGoodDays + 1

percentGoodDays = numGoodDays / trials
print(" By simulation, the \%  of good days over the long run = " + str(percentGoodDays))

P10000 = np.copy(P)
for i in range(9999):
	P10000 = np.dot(P10000, P)

p = np.array([0,0,1])

A = np.dot(p,P10000)

ans = float(A[0])


print(" By math, the \%  of good days over the long run = " + str(ans))

