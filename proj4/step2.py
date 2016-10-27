import numpy as np
import matplotlib.pyplot as plt 

rounds = 50000
alpha = 1/25
box = np.zeros(rounds)
x = np.zeros(12)
success = 0

for i in range(rounds):
	for j in range(12):
		x[j]= -1 * np.log(np.random.rand())/ alpha
		box[i] = box[i] + x[j]
	if(box[i] >= 365):
		success = success + 1

mean = np.mean(box)
std = np.std(box)

plt.hist(box, bins = 50, normed = True)
plt.legend(["mean = " + str(mean) + " std = " + str(std) + " p = " + str(success/rounds)])
plt.show()

