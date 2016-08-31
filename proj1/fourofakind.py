import matplotlib as plt
import numpy as np

rounds = 100000
A = np.arange(1,53)
B = np.zeros(5)
fourOfAKind = 0
instances = 0

for i in range(rounds):
    A = np.random.permutation(A)
    instances = 0
    for i in range(5):
        B[i] = A[i] % 13
    B = np.sort(B)
    for i in range(5):
        if B[i] == B[3]:
            instances = instances + 1
    if instances == 4:
        fourOfAKind = fourOfAKind + 1

probability = fourOfAKind / rounds
print(probability)
