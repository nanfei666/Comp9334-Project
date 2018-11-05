import random
import math
import matplotlib.pyplot as plt
Lambda=0.35
mu=1
inter_arrival=[]
service=[]
random.seed(2)
x=[]
for i in range(5000):
    a = -(math.log(1-random.random()))/Lambda
    inter_arrival.append(a)
for j in range(len(inter_arrival)):
    x.append(j)

inter_arrival.sort()
inter_arrival.reverse()
plt.plot(x,inter_arrival)
plt.title("inter-arrival distribution")
plt.show()
# for i in range(5000):
#     for _ in range(0,3):
#         b=0
#         b = b-(math.log(1-random.random()))/mu
#         service.append(b)
# for j in range(len(service)):
#     x.append(j)
