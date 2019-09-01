import numpy as np
import matplotlib.pyplot as plt
import math
import random

x=random.uniform(0,7)
c=1
sig = 0.5
fitness=[]
suc = 0
step_iter=5
def fitfunc(x):
    return math.pow(math.pow(x,2) - (7*x),2)

for i in range(500):
    fitness.append(fitfunc(x))
    x1=x+np.random.normal(0,math.pow(sig,2))
    while x1<0 or x1>7:
        x1 = x + np.random.normal(0, math.pow(sig, 2))
    #print(x1)
    if((i%step_iter)==0):
        if(suc/step_iter > 0.2):
            sig=sig/c
        elif(suc/step_iter<0.2):
            sig=sig*c
        suc=0

    if(fitfunc(x1)>fitfunc(x)):
        x=x1
        suc=suc+1

plt.plot(fitness, label="Fitness with Es(1+1)", linewidth=2)

plt.legend()
plt.xlabel('generations')
plt.ylabel('Fitness', multialignment='center')
plt.show()



