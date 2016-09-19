import numpy as np
import matplotlib.pyplot as plt
import math

rounds = 5000
complete = False
collection = np.zeros(5)
capsCollected = 0
AvgCapsUntilComplete = np.zeros(rounds)
count = 0

for i in range(1,rounds):
    for j in range(5):
        collection[j] = 0
    while(True):
        count = 0
        cap = np.random.randint(0,5)
        capsCollected = capsCollected + 1
        collection[cap] = 1
        for k in range(5):
            count =  count + collection[k]
        if(count == 5):
            break
    AvgCapsUntilComplete[i] = capsCollected / i

plt.plot(AvgCapsUntilComplete)
plt.title("Average Number of Caps Collected Until Complete Set")
plt.xlabel("Round")
plt.ylabel("Caps")
plt.axis([1,rounds,1, 20])

plt.annotate("P = " +  str(AvgCapsUntilComplete[rounds -1]), xy = (rounds - 2000, AvgCapsUntilComplete[rounds - 1] -2 ))
plt.show()
