import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#I learned how to plot gaussian from
#http://stackoverflow.com/questions/23447262/
#fitting-a-gaussian-to-a-histogram-with-matplotlib-
#and-numpy-wrong-y-scaling

dice = 1
rounds = 50000

plt.figure(1)

n1 = np.zeros(rounds)
for i in range(rounds):
	for j in range(dice):
		n1[i] = (int)(np.random.rand() * 6 + 1) * dice

#mean = np.mean(n1) * dice
#std = np.std(n1) * np.sqrt(dice)
#x = np.linspace(min(n1),max(n1),100)
#plt.plot(x,mlab.normpdf(x,mean,std), color = "red")
plt.hist(n1, normed=True)

plt.figure(2)
dice = 2
n2 = np.zeros(rounds)
for i in range(rounds):
	for j in range(dice):
		n2[i] = n2[i] + (int)(np.random.rand()*6 + 1) * dice


#mean = np.mean(n1) * dice
#std = np.std(n1) * np.sqrt(dice)
#x = np.linspace(min(n2),max(n2),100)
#plt.plot(x,mlab.normpdf(x,mean,std), color = "red")
plt.hist(n2, normed=True)

plt.figure(3)
dice = 3
n3 = np.zeros(rounds)
for i in range(rounds):
	for j in range(dice):
		n3[i] = n3[i] + (int)(np.random.rand()*6 + 1) * dice

#mean = np.mean(n1) * dice
#std = np.std(n1) * np.sqrt(dice)
#x = np.linspace(min(n3),max(n3),100)
#plt.plot(x,mlab.normpdf(x,mean,std), color = "red")
plt.hist(n3, normed=True)


plt.figure(6)
dice = 6
n6 = np.zeros(rounds)
for i in range(rounds):
	for j in range(dice):
		n6[i] = n6[i] + (int)(np.random.rand()*6 + 1) * dice

#mean = np.mean(n1) * dice
#std = np.std(n1) * np.sqrt(dice)
#x = np.linspace(min(n6),max(n6),100)
#plt.plot(x,mlab.normpdf(x,mean,std), color = "red")
plt.hist(n6, normed=True)

plt.figure(40)
dice = 40
n40 = np.zeros(rounds)
for i in range(rounds):
	for j in range(dice):
		n40[i] = n40[i] + (int)(np.random.rand()*6 + 1) * dice

#mean = np.mean(n1) * dice
#std = np.std(n1) * np.sqrt(dice)
#x = np.linspace(min(n40),max(n40),100)
#plt.plot(x,mlab.normpdf(x,mean,std), color = "red")
plt.hist(n40, normed=True)

plt.show()