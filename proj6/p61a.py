import numpy as np

P = np.array([[.5, .3 , .2], [.2, .6, .2], [.3, .2, .5]])


trials = 100000
mediumDays= 0

rolls = np.random.rand(trials,3)
ThursdayState = np.zeros(trials)
for i in range(trials):
	state = 1
	for j in range(3):
		sum = 0
		for k in range(3):
			sum = sum + P[state, k]
			#print(rolls[i,j])
			#print(P[state,k])
			if(rolls[i,j] <= sum):
				state = k
				#print(state)
				break
			#print(state)
	#print(state)
	if(state == 1):
		mediumDays = mediumDays + 1
	ThursdayState[i] = state
print(" By simulation, P(Thursday is a medium day) = " + str( mediumDays / trials)) 

MediumDay = np.array([0,1,0])

P3 = np.copy(P)
for i in range(2):
	P3 = np.dot(P3,P)
Thursday = np.dot(MediumDay, P3)

print(" By math, P(Thursday is a medium day) = " + str( Thursday[1])) 