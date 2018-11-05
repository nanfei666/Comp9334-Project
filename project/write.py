
def Simulation(mode,Arrival_time,Service_time,m,setup_time,delayoff_time):
    #systm [0:OFF 1:SetUp 2:BUSY 3:DelayedOFF]
    with open('arrival_3.txt','r') as arrival:
        Arrival_time_before = [line.strip()for line in arrival]
        Arrival_time = list(map(eval,Arrival_time_before))
    with open ('service_3.txt','r') as service:
        Service_time_before = [line.strip()for line in service]
        Service_time = list(map(eval,Service_time_before))

    
    response_time_cumlative = 0
    num_customer_served = 0
    
    Master_Clock = 0

    server_state=[0 for _ in range(m)]
    next_departure_arrival_time=[0 for _ in range(m)]
    Dispatcher = []

    arrrival_and_departure ={}


    next_departure_time = [float("inf") for _ in range(m)]
    
    Set_up_finish_time = [float("inf") for _ in range(m)]
   
    Expiry_time = [float("inf") for _ in range(m)]
    
    UNMARKED=[]
    
        
    
    #Arrival_and_Service=dict(zip(Arrival_time,Service_time)) # a dict contain arrival and service time
    
    #while len(arrrival_and_departure)<len(Arrival_time):
    while Arrival_time.count(float("inf")) != len(Arrival_time) or  Set_up_finish_time.count(float("inf"))!=len(Set_up_finish_time) or Expiry_time.count(float("inf"))!=len(Expiry_time) or server_state.count(0)!= len(server_state) : 
        print(arrrival_and_departure)
        Arrival_and_Service=dict(zip(Arrival_time,Service_time))   
        
        min_time = [float(min(Arrival_time)),float(min(next_departure_time)), float(min(Set_up_finish_time)),float(min(Expiry_time))]

        #print(next_departure_time)

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
                    #print(Set_up_finish_time)
                else:
                    Dispatcher.append([Master_Clock,Arrival_and_Service[next_arrival_time],"UNMARKED" ])
                    arrival_index = Arrival_time.index(Next_event_time)
                    Arrival_time[arrival_index] = float("inf")
                    #print(Dispatcher)
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
            #print(arrrival_and_departure[Next_event_time])
            
            response_time_cumlative =response_time_cumlative + Master_Clock - arrrival_and_departure[Next_event_time]
            num_customer_served = num_customer_served+1
            
            # print("responsetime_cum",response_time_cumlative)
            # print("number_of_serviced",num_customer_served)
            # print(len(arrrival_and_departure))
            # print(Arrival_time)
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
                    del Dispatcher[0]
                    
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
        if Next_event_time == min(Expiry_time):
            Expiry_index = Expiry_time.index(Next_event_time)
            server_state[Expiry_index] = 0
            Expiry_time[Expiry_index] = float("inf")

    avg_response_time = response_time_cumlative / num_customer_served
    print(avg_response_time)
    
 
    return avg_response_time

Simulation(1,1,1,3,50,100)