import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
nsim = 5     # number of simulation
m = 20000 # number of data points in each simulation
response_time_traces = np.zeros((nsim,m))
print(type(response_time_traces))
c=[]
for i in range(1,6):
    with open("trace"+str(i),'r') as trace:
        b= trace.readlines()
        for item in b:
            c.append(float(item.strip()))
            #print(float(item.strip()))
            
        response_time_traces[i-1] =c
        c.clear()
    
print(response_time_traces[0])
mt=np.mean(response_time_traces,axis=0)
#print(mt[0])
w=5000
mt_smooth = [0]* (m-w)


for i in range(1,m-w+1):
    if i<=w:
        
        mt_smooth[i-1]=np.mean(mt[0:2*i-1])
    else:
        mt_smooth[i-1] = np.mean(mt[i-w-1:i+w])
x=range(0,m-w)
#print(len(x))
#print(len(mt_smooth))

plt.plot(x,mt_smooth,linewidth=3)

plt.title('w='+str(w))
plt.show()
