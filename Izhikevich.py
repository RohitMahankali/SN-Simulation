from numpy import *
from scipy import *
from pylab import *

#State variables and initial setup
T = 50
dt = 0.125
t_rest = 0
time = arange(0,T+dt,dt)

'''
tim = []
for i in range(0,T+dt,dt):xx
    tim.append(i)

'''
#a =    9
#print a
##Izhikevich neuron setup
#Vm = 13
#print Vm






Vm = [-70 for _ in range(len(time))]
#print Vm
memRec = [0 for _ in range(len(time))]
Vth = 10
Rm = 1
Cm = 1
Tau = Rm*Cm
TauRef = 2

#input current
I = 17

# a,b,c,d
a = 0.02
b = 0.2
c = -70
d = 8
#Model logic
for i in range(len(time)-1):
    if time[i] > t_rest:
        Vm[i+1] = Vm[i]+(0.04*(Vm[i]**2)+5*Vm[i]+140-memRec[i]+I)*dt
        memRec[i + 1] = memRec[i] + (a * ((b * Vm[i]) - memRec[i])) * dt
        #memRec[i+1] = (a*((b*Vm[i])-memRec[i]))*dt
    if Vm[i+1] >= Vth:
        Vm[i+1] = c
        memRec[i+1]+=d
        t_rest = time[i]+TauRef
	

##Graphing using MatplotLib
plot(time,Vm)
title("Izhikevich Neuron Model")
xlabel("time")
ylabel("Membrane Potential")
ylim([-80,40])
xlim([0,50])
show()



