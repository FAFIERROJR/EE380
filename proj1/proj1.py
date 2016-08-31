import matplotlib.pyplot as plt
import numpy as np

die1 = 0
die2 = 0

A = np.zeros(10000)

numRolls = 0

for i in range(10000):
    numRolls = 0
    die1 = 0
    die2 = 0
    while(die1 + die2 != 7):
        die1 = np.random.randint(1,7)
        die2 = np.random.randint(1,7)
        numRolls += 1
    A[i] = numRolls

print(A)

plt.hist(A, bins = 50, normed = True)
plt.title("Histogram of Rolls Until Seven")
plt.xlabel("Number of Rolls Until A Seven is Rolled")
plt.ylabel("Frequency")

plt.show()
