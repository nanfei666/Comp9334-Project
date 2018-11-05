import heapq
import sys
import math
import random


def Simulation(mode,Lambda,mu,m,setup_time,delayoff_time,Time_end):
    #systm [0:OFF 1:SetUp 2:BUSY 3:DelayedOFF]
    response_time_cumlative = 0
    num_customer_served = 0
    
    Master_Clock = 0

    server_state=[0 for _ in range(m)]
    next_departure_arrival_time=[0 for _ in range(m)]
    Dispatcher = []

    arrrival_and_departure ={}


    next_departure_time = [float("inf") for _ in range(m)]
    Service_time =[]
    Arrival_time =[]
    
    Set_up_finish_time = [float("inf") for _ in range(m)]
   
    Expiry_time = [float("inf") for _ in range(m)]
    
    UNMARKED=[]
    random.seed(2)
    
    

    a = -(math.log(1-random.random()))/Lambda
    b=0
    for _ in range(0,3):
        b = b-(math.log(1-random.random()))/mu
    
    Arrival_time.append(a)
    Service_time.append(b)

    while Master_Clock < Time_end:
        a = -(math.log(1-random.random()))/Lambda
        b=0
        for _ in range(0,3):
            b = b-(math.log(1-random.random()))/mu
                     
        #print(Arrival_time)
        #print(Service_time)
        Arrival_and_Service=dict(zip(Arrival_time,Service_time))
        


        min_time = [float(min(Arrival_time)),float(min(next_departure_time)), float(min(Set_up_finish_time)),float(min(Expiry_time))]

    
        Next_event_time = min(min_time)
        #print(Next_event_time)
        
        Master_Clock= Next_event_time
        
        if Next_event_time==float(min(Arrival_time)): # next event is arrival
            next_arrival_time = Next_event_time
            #print("Arrival")
            if 3 in server_state:
                Copy_expiry = [0 if x== float("inf") else x for x in Expiry_time]
                max_Tc = max(Copy_expiry) # find max Tc value
                server_index = Expiry_time.index(max_Tc)
                server_state[server_index] = 2
                Expiry_time[server_index] = float("inf") #cancle the Tc
                next_arrival_service_time = Arrival_and_Service[next_arrival_time]
                next_departure_time[server_index] = next_arrival_time + next_arrival_service_time
                next_departure_arrival_time[server_index] = next_arrival_time
                arrival_index = Arrival_time.index(Next_event_time)
                Arrival_time[arrival_index] = float("inf")
                arrrival_and_departure[next_departure_time[server_index]] = next_arrival_time
                #print(next_departure_time)
                #print(next_departure_arrival_time)
            else:
                if 0 in server_state:
                    
                    
                    Dispatcher.append([Master_Clock, Arrival_and_Service[next_arrival_time], "MARKED"])
                    arrival_index = Arrival_time.index(Next_event_time)
                    Arrival_time[arrival_index] = float("inf")
                    
                    
                    #print(Arrival_time)
                     
                    service_index  = server_state.index(0)
                    #next_departure_arrival_time[service_index] = next_arrival_time
                    server_state[service_index] = 1
                    Set_up_finish_time[service_index] = setup_time + Master_Clock
                    #print(next_departure_arrival_time)
                    #print("set_up_finish_time")
                    #print(Set_up_finish_time)
                else:
                    Dispatcher.append([Master_Clock,Arrival_and_Service[next_arrival_time],"UNMARKED" ])
                    arrival_index = Arrival_time.index(Next_event_time)
                    Arrival_time[arrival_index] = float("inf")
                    #print(Dispatcher)
            Arrival_time.append(Master_Clock+a)
            Service_time.append(b)
        if Next_event_time == min(Set_up_finish_time):
            #print("jin le set_up") 
            finish_index= Set_up_finish_time.index(Next_event_time)
            server_state[finish_index]= 2
            Set_up_finish_time[finish_index] = float("inf")
            next_arrival_service_time = Dispatcher[0][1]
            next_departure_time[finish_index] = Master_Clock + next_arrival_service_time
            a= Master_Clock + next_arrival_service_time
            arrrival_and_departure[a]= Dispatcher[0][0]
            del Dispatcher[0]
            
        
        if Next_event_time == float(min(next_departure_time)):
            #print("jin le departure")
            departure_indx = next_departure_time.index(Next_event_time)
            
            response_time_cumlative =response_time_cumlative + Master_Clock - arrrival_and_departure[Next_event_time]
            num_customer_served = num_customer_served+1
            
            #print(response_time_cumlative)
            #print(num_customer_served)
            if len(Dispatcher) == 0:
                
                next_departure_time[departure_indx] = float("inf")
                server_state[departure_indx] = 3
                Expiry_time[departure_indx] = Master_Clock + delayoff_time
                
            else:
                
                next_arrival_service_time = Dispatcher[0][1]
                
                next_departure_arrival_time[departure_indx] =  Next_event_time
                next_departure_time [departure_indx] = Master_Clock + next_arrival_service_time
                b= Master_Clock + next_arrival_service_time
                arrrival_and_departure[b] = Dispatcher[0][0]

                if Dispatcher[0][-1] =="MARKED" :
                    
                    
                    for job in Dispatcher:   ##########
                        if "UNMARKED" in job:
                            UNMARKED.append(Dispatcher.index(job))
                            continue
                    if len(UNMARKED)!= 0:
                        Dispatcher[UNMARKED[0]][-1] ="MARKED"
                        UNMARKED.clear()                        
                    else:
                        copy_setup_time_finish = [0 if x== float("inf") else x for x in Set_up_finish_time]
                        max_finsih_time = max(copy_setup_time_finish)
                        
                        service_index = Set_up_finish_time.index(max_finsih_time)
                        server_state[service_index] = 0
                        Set_up_finish_time[service_index] = float("inf")
                del Dispatcher[0]
        if Next_event_time == min(Expiry_time):
            Expiry_index = Expiry_time.index(Next_event_time)
            server_state[Expiry_index] = 0
            Expiry_time[Expiry_index] = float("inf")

    avg_response_time = response_time_cumlative / num_customer_served
    print(avg_response_time)
    #print(arrrival_and_departure)
              
                
Simulation(1,0.35,1,5,5,0.1,8000)

                   
                        

                




