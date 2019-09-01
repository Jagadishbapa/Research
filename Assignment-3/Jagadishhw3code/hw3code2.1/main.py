import math
import random
import matplotlib.pyplot as plt

bestarray=[]
avarray=[]
def fitfunc(x):
    return abs(math.pow(math.pow(x,2) - (7*x),2))
def randompop():
    return str(random.choice([0,1]))
def genpairsforcross(initialpop):
    for i in range(0, 6):
        initialpop[i] = (initialpop[i][0], fitfunc(int(initialpop[i][0], 2)), 0)
    print(initialpop)
    sum = 0
    bestsum=0
    for i in range(0, 6):
        sum = sum + initialpop[i][1]
    print(sum)
    for i in range(0, 6):
        if(bestsum<initialpop[i][1]):
            bestsum=initialpop[i][1]
    bestarray.append(bestsum)
    avg=sum/6
    avarray.append(avg)
    for i in range(0, 6):
        initialpop[i] = (initialpop[i][0], initialpop[i][1], initialpop[i][1] / sum)
    print(initialpop)
    for i in range(1, 6):
        initialpop[i] = (initialpop[i][0], initialpop[i][1], initialpop[i - 1][2] + initialpop[i][2])
    return initialpop

def crossover(initialpop,pc):
    print("crossover")
    print(initialpop)
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
            print(s)
            print(s1)
            initialpop[ind] = ("".join(s),initialpop[ind][1],initialpop[ind][2])
            initialpop[ind+1] = ("".join(s1),initialpop[ind+1][1],initialpop[ind+1][2])
        ind=ind+2

    '''
    for lv in range(3):
        prob1 = random.uniform(0, 1)
        print(prob1)
        prob2 = random.uniform(0, 1)
        print(prob2)
        ind = -1
        ind1 = -1
        print("test")
        print(initialpop)
        for i in range(0,6):
            if(prob1<=initialpop[i][2]):
                ind=i
                break
        for i in range(0, 6):
            if(prob2<=initialpop[i][2]):
                ind1=i
                break
        print("indices")
        print(ind)
        print(ind1)
        pcs=random.uniform(0, 1)
        if pcs<=pc:
            rc=random.choice([1,2])
            print(rc)

            s = list(initialpop[ind][0])
            s1 = list(initialpop[ind1][0])
            for i in range(rc,len(initialpop[0][0])):
                swapc=s[i]
                s[i]=s1[i]
                s1[i]=swapc
            print(s)
            print(s1)
            initialpop[ind] = ("".join(s),initialpop[ind][1],initialpop[ind][2])
            initialpop[ind1] = ("".join(s1),initialpop[ind1][1],initialpop[ind1][2])
            print(initialpop)
            '''
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
pc = 0.7
pm = 0.01
#x = [(0, '000'), (1,'001'), (2,'010'), (3,'011'), (4,'100'), (5,'101'), (6,'110'), (7,'111')]

generation=0
initialpop=[]
while generation<=500:
    print("start")
    if generation==0:
        for i in range(6):
            inpopval=''
            for j in range(3):
                inpopval=inpopval+randompop()
            initialpop.append((inpopval,0,0))

    print(initialpop)
    initialpop=genpairsforcross(initialpop)
    print(initialpop)
    print(random.uniform(0,1))
    initialpop=crossover(initialpop,pc)
    initialpop=mutate(initialpop,pm)
    generation=generation+1
    print("end")
print(bestarray)
print(avarray)

line1, = plt.plot(bestarray, label="Best", linestyle='--')
line2, = plt.plot(avarray, label="Average", linewidth=1)
'''
# Create a legend for the first line.
first_legend = plt.legend(handles=[line1], loc=1)

# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

# Create another legend for the second line.
plt.legend(handles=[line2], loc=4)
'''
plt.legend(('Best', 'Average'),
           loc='lower center', shadow=True)
plt.xlabel('generations')
plt.ylabel('Fitness', multialignment='center')
plt.show()
'''
for i in range(0,3)
{
select prob between 0 and 1
select a value in initialpop that has a prob
select prob1 between 0 and 1
select a value in initialpop that has a prob1
crossover(2 values)
add values to initialpop
apply mutation on each value
}
'''
