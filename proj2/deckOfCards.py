import numpy as np
import matplotlib.pyplot as plt
import math

rounds = 5000

deck = np.arange(1,53)
foundAtArray = np.zeros(rounds)

foundAt = 0

for i in range(1, rounds):
    deck = np.random.permutation(deck)
    for j in range(52):
        foundAt = foundAt + 1
        if(deck[j] % 13 == 0):
            break
    foundAtArray[i] = foundAt/i
print(foundAtArray[rounds - 1])
plt.plot(foundAtArray)
plt.title("Average Turns Until Ace")
plt.xlabel("Round")
plt.ylabel("Turns")
plt.axis([1,rounds,1, int(math.ceil(foundAtArray[rounds-1]))])
plt.show()
