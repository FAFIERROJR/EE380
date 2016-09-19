import numpy as np
import matplotlib.pyplot as plt
import math

rounds = 5000
avg = np.zeros(rounds)
inSemi = 0


for i in range(1, rounds):
    p1 = np.random.random() * math.pi * 2
    p2 = np.random.random() * math.pi * 2
    p3 = np.random.random() * math.pi * 2
    
    if(abs(p1 - p2) < math.pi and abs (p1 - p3) < math.pi and abs(p2 - p3) < math.pi):
        inSemi = inSemi + 1
   
    avg[i] = inSemi / i

plt.plot(avg)
plt.title("Average Number of Occurrences of points on a Semicircle");
plt.xlabel("Round")
plt.ylabel("Caps")
plt.annotate("P = " +  str(avg[rounds -1]), xy = (rounds - 5000, avg[rounds - 1] - .2))
plt.show()
