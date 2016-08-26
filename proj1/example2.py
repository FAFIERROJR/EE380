from random import randint
flips = [randint(0,1) for r in range(1000)]
heads = sum(flips)
print(heads)
print(1000-heads)
