### Use Python 3.6.4


import ass
### Obtain the number of test
with open('num_tests.txt','r') as num:
    number_of_test = num.readline()  

###  Obtain what the mode will be    
for i in range(1,int(number_of_test)+1):
    with open('mode_'+str(i)+'.txt','r') as arrival:
        mode = arrival.readline()  
    
   
    with open('para_'+str(i)+'.txt','r') as paramental:
        paramental_list = [line.strip() for line in paramental]
         ## when mode is trace, obtain the parameters
        if len(paramental_list) == 3:   
            m = int(paramental_list[0])
            setup_time = float(paramental_list[1])
            delayoff_time = float(paramental_list[2])   
         ## when mode is random, obtain the parameters
        if len(paramental_list) == 4:
            m = int(paramental_list[0])
            setup_time = float(paramental_list[1])
            delayoff_time = float(paramental_list[2])
            Time_end = float(paramental_list[3])
    ## Obtain the arrival time and service time when trace mode
    if mode == "trace":       
        with open('arrival_'+str(i)+'.txt','r') as arrival:
            Arrival_time_before = [line.strip()for line in arrival]
            Arrival_time = list(map(eval,Arrival_time_before))
        with open ('service_'+str(i)+'.txt','r') as service:
            Service_time_before = [line.strip()for line in service]
            Service_time = list(map(eval,Service_time_before))
 
    ## Obtain the lambda and mu when random mode
    if mode =="random":
        with open('arrival_'+str(i)+'.txt','r') as arrival:
            Lambda = float(arrival.readline())
        with open('service_'+str(i)+'.txt','r') as service:
            mu = float(service.readline())
    ## create the mrt.txt and departure.txt when trace
    if mode=="trace":
        ## use Simulation function in ass.py
        mrt,arrrival_and_departure=ass.Simulation(Arrival_time,Service_time,m,setup_time,delayoff_time)
        ## create mrt file to write the mean response time
        with open('mrt_'+str(i)+'.txt','w') as f:
            f.write(str('%.3f' % mrt))
        ## crete departure file to write departure time and coresponding arrival time
        with open('departure_'+str(i)+'.txt','w') as w:
            for key,value in arrrival_and_departure.items():
                
                w.write(str('%.3f' % value)+'    '+str('%.3f' % key))
                w.write('\n')
                        
    ## create the mrt.txt and departure.txt when random   
    if mode =="random":
        ## use Simulation_random function in ass.py
        mrt,arrrival_and_departure,response_time_every_job = ass.Simulation_rendom(Lambda,mu,m,setup_time,delayoff_time,Time_end)
        ## create mrt file to write the mean response time
        with open('mrt_'+str(i)+'.txt','w') as f:
            f.write(str('%.3f' % mrt))
        ## crete departure file to write departure time and coresponding arrival time 
        with open('departure_'+str(i)+'.txt','w') as w:
            for key,value in arrrival_and_departure.items():
                w.write(str('%.3f' % value)+'    '+str('%.3f' % key))
                w.write('\n')
        
    




        



    

            




    