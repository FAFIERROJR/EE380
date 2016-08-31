import matplotlib as plt
import numpy as np

fiftyHeads = 0
rounds = 10000

for i in range(rounds):
    instances = 0;
    for i in range(100):
        if(np.random.randint(0,2) == 0):
            instances = instances + 1
    if(instances == 50):
        fiftyHeads = fiftyHeads + 1
        
probability = fiftyHeads / rounds

print(probability)
