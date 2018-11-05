import math
import ass
import numpy as np
import matplotlib.pyplot as plt
Lambda=0.35
mu=1
setup_time = 5
#Tc=[0.1,10.1]
Tc=[0.1,10]
time_end = 15000
L1=[]
L2=[]
for i in range(1,21):
    b=0
    k_response_time=[]
    response_time=[]
    ass.random.seed(i)
    response_time_every_job=ass.Simulation_rendom(Lambda,mu,5,setup_time,Tc[0],time_end)[2]
    with open ("response.txt",'w') as respon:
        for i in response_time_every_job:
            respon.write(str(i))
            respon.write('\n')


    with open("response.txt",'r') as trace:       
        response_time= trace.readlines()[2000:5000]

    for j in range(0,len(response_time)):
        b=b+float(response_time[j])
    mrt=b/len(response_time)
    L1.append(float(mrt))


for i in range(1,21):
    b=0
    k_response_time=[]
    response_time=[]
    ass.random.seed(i)
    response_time_every_job=ass.Simulation_rendom(Lambda,mu,5,setup_time,Tc[1],time_end)[2]
    with open ("response.txt",'w') as respon:
        for i in response_time_every_job:
            respon.write(str(i))
            respon.write('\n')


    with open("response.txt",'r') as trace:       
        response_time= trace.readlines()[2000:5000]

    for j in range(0,len(response_time)):
        b=b+float(response_time[j])
    mrt=b/len(response_time)
    L2.append(float(mrt))
D=[]
for k in range(20):
    D.append(L1[k]-L2[k])
avrg=sum(D)/20
SD=0
for u in range(20):
    SD+=(avrg-D[u])**2
SD=math.sqrt(SD/19)
cr1=avrg-1.729*SD/math.sqrt(20)
cr2=avrg+1.729*SD/math.sqrt(20)
print((cr1,cr2))

# plt.ylim((0,9))
# plt.ylabel("Mean response time of first k jobs")
# plt.title("Lambda="+str(Lambda)+ ", Mu="+str(mu)+ ", Setup_time="+str(setup_time)+", Tc="+str(Tc)+", Time_end="+str(time_end))

# response_time_every_job=[]
# k_response_time=[]
# ass.random.seed(12)
# response_time_every_job=ass.Simulation_rendom(Lambda,mu,5,setup_time,Tc,time_end)[2]
# with open ("response.txt",'w') as respon:
#     for i in response_time_every_job:
#         respon.write(str(i))
#         respon.write('\n')
# b=0
# x=[]
# with open("response.txt",'r') as trace:       
#     response_time= trace.readlines()[0:5000]
# for i in range(0,5000):
#     b=b+float(response_time[i])
#     k_response_time.append(b/(i+1))
#     x.append(i)
# plt.ylabel("Mean response time of first k jobs")
# plt.title("Lambda="+str(Lambda)+ ", Mu="+str(mu)+ ", Setup_time="+str(setup_time)+", Tc="+str(Tc)+", Time_end="+str(time_end)+", Seed=12")

# plt.plot(x,k_response_time)
# plt.show()



# print(len(a))
# with open ("response5.txt",'w') as respon:
#     for i in a:
#         respon.write(str(i))
#         respon.write('\n')
# response_time_traces = np.zeros((nsim,m))
# c=[]
# for i in range(1,6):
#     with open("response"+str(i)+".txt",'r') as trace:       
#         b= trace.readlines()[0:5000]
#         for item in b:
#             c.append(float(item.strip()))
        
#         response_time_traces[i-1] =c
#         c.clear()

# mt=np.mean(response_time_traces,axis=0)
# w=2000
# mt_smooth = [0]* (m-w)


# for i in range(1,m-w+1):
#     if i<=w:
        
#         mt_smooth[i-1]=np.mean(mt[0:2*i-1])
#     else:
#         mt_smooth[i-1] = np.mean(mt[i-w-1:i+w])
# x=range(0,m)
# print(len(x))
# print(len(mt))
# plt.plot(x,mt,linewidth=1)
# plt.title('w='+str(w))
# plt.show()
