import numpy as np
import matplotlib.pyplot as plt

gravity = 9.8
rounds = 50000
velocity = np.sqrt(980)
f = np.zeros(rounds)
p = np.zeros(rounds)

for i in range(rounds):
    angle = np.random.random() * np.pi / 2
    f[i] =  velocity * velocity / gravity * np.sin(2 * angle)

mean = np.mean(f)
std = np.std(f)


labels= ["mean = " + str(mean)  + " std = " + str(std)]
plt.hist(f, 40, normed = True)
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.legend(labels, loc = 0)
plt.show()