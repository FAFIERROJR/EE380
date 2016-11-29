import numpy as np

trials = 3000009

flips = np.random.rand(trials)

numFlipsUntilSuccss = 0
numFlipsUntilSuccssArr = list()
cnscHeads = 0
atLeast8 = 0
numSuccesses = 0

for i in range(trials):
	numFlipsUntilSuccss = numFlipsUntilSuccss + 1
	if(flips[i] < .5):
		cnscHeads = cnscHeads + 1
		if(cnscHeads == 3):
			numSuccesses = numSuccesses + 1
			if(numFlipsUntilSuccss >= 8):
				atLeast8 = atLeast8 + 1
			numFlipsUntilSuccssArr.append(numFlipsUntilSuccss)
			numFlipsUntilSuccss = 0
			cnscHeads = 0
	if(flips[i] >= .5):
		cnscHeads = 0

mean = np.mean(numFlipsUntilSuccssArr)
pAtLeast8 = atLeast8 / numSuccesses

print("By simulation, the probability of at least 8 flips until 3 consecutive heads = " + str(pAtLeast8))
print("By simulation, the average number of flips until 3 consecutive heads = " + str(mean))

Q = np.array([[1/2, 1/2, 0], [1/2, 0, 1/2], [1/2 , 0, 0]])
I = np.identity(3)

diff = np.subtract(I,Q)
inverse = np.linalg.inv(diff)
M = np.array([[1],[1],[1]])
A = np.dot(inverse, M)

mathmean = float(A[0])

print("By Markov Chain analysis, the average number of flips until 3 consective heads = " + str(mathmean))

R = np.array([[0],[0],[1/2]])

B = np.dot(inverse, R)

print("The probabities of absortion are given by the following vector")
print(B)