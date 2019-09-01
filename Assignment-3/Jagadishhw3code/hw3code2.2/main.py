import math
import random
import matplotlib.pyplot as plt

avarray=[]
avarray1=[]
avarray2=[]
avarray3=[]
def fitfunc(x):
    return abs(math.pow(math.pow(x,2) - (7*x),2))
def randompop():
    return str(random.choice([0,1]))
def genpairsforcross(initialpop):
    for i in range(0, 6):
        initialpop[i] = (initialpop[i][0], fitfunc(int(initialpop[i][0], 2)), 0)
    sum = 0
    bestsum=0
    for i in range(0, 6):
        sum = sum + initialpop[i][1]
    avg=sum/6
    avarray.append(avg)
    for i in range(0, 6):
        initialpop[i] = (initialpop[i][0], initialpop[i][1], initialpop[i][1] / sum)
    for i in range(1, 6):
        initialpop[i] = (initialpop[i][0], initialpop[i][1], initialpop[i - 1][2] + initialpop[i][2])
    return initialpop

def crossover(initialpop,pc):
    #loop for 3 times
    crossnewpop=[]
    for i in range(6):
        prob1=random.uniform(0,1)
        for lv in range(6):
            if prob1 <= initialpop[lv][2]:
                crossnewpop.append(initialpop[lv])
                break
    initialpop=crossnewpop.copy()
    ind=0
    for i in range(3):

        prob1 = random.uniform(0,1)
        if(prob1<pc):
            rc = random.choice([1, 2])
            s = list(initialpop[ind][0])
            s1 = list(initialpop[ind+1][0])
            for i in range(rc,len(initialpop[0][0])):
                swapc=s[i]
                s[i]=s1[i]
                s1[i]=swapc
            initialpop[ind] = ("".join(s),initialpop[ind][1],initialpop[ind][2])
            initialpop[ind+1] = ("".join(s1),initialpop[ind+1][1],initialpop[ind+1][2])
        ind=ind+2
    return initialpop

def mutate(initialpop,pm):

    for ind in range(6):
        pms = random.uniform(0, 1)
        if(pms<pm):
            s = list(initialpop[ind][0])
            rc = random.choice([0, 1, 2])
            if s[rc]=='0':
                s[rc]='1'
            else:
                s[rc]='0'
            initialpop[ind]=("".join(s),initialpop[ind][1],initialpop[ind][2])
    for i in range(6):
        initialpop[i] = (initialpop[i][0],0,0)
    return initialpop




n=6
pc = [0.7,0.2,0.9]
pm = 0.01
average3arrays = []
#x = [(0, '000'), (1,'001'), (2,'010'), (3,'011'), (4,'100'), (5,'101'), (6,'110'), (7,'111')]

for z in pc:
    print(z)
    generation=0
    initialpop=[]
    while generation<=500:
        if generation==0:
            for i in range(6):
                inpopval=''
                for j in range(3):
                    inpopval=inpopval+randompop()
                initialpop.append((inpopval,0,0))

        initialpop=genpairsforcross(initialpop)
        initialpop=crossover(initialpop,z)
        initialpop=mutate(initialpop,pm)
        generation=generation+1

    if z==0.7:
        print("entering0.7")
        avarray1=avarray.copy()
        print(avarray1)
    if z==0.2:
        print("entering0.2")
        avarray2=avarray.copy()
        print(avarray2)
    if z==0.9:
        print("entering")
        avarray3=avarray.copy()
    avarray.clear()

line1, = plt.plot(avarray1, label="pc=0.7", linewidth=2)
line2, = plt.plot(avarray2, label="pc=0.2", linewidth=2)
line3, = plt.plot(avarray3, label="pc=0.9", linewidth=2)

plt.legend(('pc=0.7', 'pc=0.2', 'pc=0.9'),
           loc='lower center', shadow=True)
plt.xlabel('generations')
plt.ylabel('Fitness', multialignment='center')
plt.show()

