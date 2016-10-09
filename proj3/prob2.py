import numpy as np 
import matplotlib.pyplot as plt

rounds = 50000
R = 5
P = np.zeros(rounds)

for i in range(rounds):
	I = (np.random.randn() * 3 * .002)
	P[i] = I * I * R

mean = np.mean(P)
std = np.std(P)


labels= ["mean = " + str(mean)  + " std = " + str(std)]
plt.hist(P, 40, normed = True)
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.legend(labels, loc = 0)
plt.show()