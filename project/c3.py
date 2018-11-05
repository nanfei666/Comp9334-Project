import ass
import datetime

mrt=ass.Simulation_rendom(0.35,1,5,5,0.1,15000)[0]
time_now= datetime.datetime.now()
with open("reproducible_test.txt","w") as w:
    w.write(str('%.3f' % mrt)+'    '+str( time_now))