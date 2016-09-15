import numpy as np
import matplotlib.pyplot as plt
import math

rounds = 100
avg = np.zeros(rounds)
inSemi = 0


for i in range(1, rounds):
    p1 = np.random.random() * math.pi * 2
    p2 = np.random.random() * math.pi * 2
    p3 = np.random.random() * math.pi * 2
    
    if(abs(p1 - p2) < math.pi and abs (p1 - p3) < math.pi and abs(p2 - p3) < math.pi):
        inSemi = inSemi + 1
   
    avg = inSemi / i

plt.plot(avg)
plt.title("Average Number of ")
plt.xlabel("Round")
plt.ylabel("Caps")
plt.show()
