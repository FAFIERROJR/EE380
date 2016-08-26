import numpy as np
total_flips = 1000
heads = 0
tails = 0
for f in range(total_flips):
    coin = np.random.randint(0,2)
    if(coin == 0):
        heads = heads + 1
    else:
        tails = tails + 1
print(heads)
print(tails)
