import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np

rounds = 5000
avg = np.zeros(rounds)
inSemi = 0

p = np.zeros(3)
for i in range(1, rounds):
    for j in range(3):
        p[j] = np.random.random() * 2 * 180

    p = np.sort(p)     
    if(p[1] - p[0] == 180):
        inSemi = inSemi + 1
    else:
        if(p[1] - p[0] <= 180):
            delta1 = p[1] -p[0]
            if(p[0] - p[2] + 360 + delta1 <= 180 or p[2]- p[1] + delta1 <= 180):
                inSemi = inSemi + 1
        else:
            inSemi = inSemi + 1
    avg[i] = inSemi / i

plt.plot(avg)
plt.title("Average Number of Occurrences of points on a Semicircle");
plt.xlabel("Round")
plt.ylabel("Caps")
plt.annotate("P = " +  str(avg[rounds -1]), xy = (rounds - 2000, avg[rounds - 1] - .2))
plt.show()
print("p = ")
print(avg[rounds - 1])