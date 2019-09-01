import math
import random
import matplotlib.pyplot as plt

avarray=[]
avarray1=[]
avarray2=[]
avarray3=[]
def fitfunc(x,y):
    print(x,y)
    if(x==5):
        return math.pow(x,2) + math.pow(y,2)
    else:
        return (1/abs(math.pow(x-5,2))) + math.pow(y,2)
def randompop():
    return str(random.choice([0,1]))
def genpairsforcross(initialpop,n):
    for i in range(0, n):
        initialpop[i] = (initialpop[i][0], fitfunc(int(initialpop[i][0][:3], 2), int(initialpop[i][0][3:], 2)), 0)
    sum = 0
    for i in range(0, n):
        sum = sum + initialpop[i][1]
    avg=sum/n
    avarray.append(avg)
    for i in range(0, n):
        initialpop[i] = (initialpop[i][0], initialpop[i][1], initialpop[i][1] / sum)
    for i in range(1, n):
        initialpop[i] = (initialpop[i][0], initialpop[i][1], initialpop[i - 1][2] + initialpop[i][2])
    return initialpop

def crossover(initialpop,pc,n):
    #loop for 3 times
    print(initialpop)
    crossnewpop=[]
    for i in range(n):
        prob1=random.uniform(0,1)
        for lv in range(n):
            if prob1 <= initialpop[lv][2]:
                crossnewpop.append(initialpop[lv])
                break
    initialpop=crossnewpop.copy()
    ind=0
    for i in range(int(n/2)):

        prob1 = random.uniform(0,1)
        if(prob1<pc):
            rc = random.choice([1, 2, 3, 4, 5])
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

def mutate(initialpop,pm,n):

    for ind in range(n):
        pms = random.uniform(0, 1)
        if(pms<pm):
            s = list(initialpop[ind][0])
            rc = random.choice([0, 1, 2, 3, 4, 5])
            if s[rc]=='0':
                s[rc]='1'
            else:
                s[rc]='0'
                initialpop[ind]=("".join(s),initialpop[ind][1],initialpop[ind][2])
    for i in range(n):
        initialpop[i] = (initialpop[i][0],0,0)
    return initialpop




n=[10]
pc = 0.7
pm = 0.01
#x = [(0, '000'), (1,'001'), (2,'010'), (3,'011'), (4,'100'), (5,'101'), (6,'110'), (7,'111')]

for z in n:
    generation=0
    initialpop=[]
    while generation<=2000:
        if generation==0:
            for i in range(z):
                inpopval=''
                for j in range(6):
                    inpopval=inpopval+randompop()
                initialpop.append((inpopval,0,0))
        initialpop=genpairsforcross(initialpop,z)
        initialpop=crossover(initialpop,pc,z)
        initialpop=mutate(initialpop,pm,z)
        generation=generation+1

avarray1=avarray.copy()

avarray.clear()



plt.plot(avarray1, label="Average fitness", linewidth=2)

plt.legend()
plt.xlabel('generations')
plt.ylabel('Fitness', multialignment='center')
plt.show()

