import numpy as np
import pylab as mat
## setup parameters and state variables
T = 50 # total time to simulate (msec)
dt = 0.125 # simulation time step (msec)
time = np.arange(0, T+dt, dt) # time array
t_rest = 0 # initial refractory time
## LIF properties
Vm = [0 for _ in range(len(time))] # potential (V) trace over time
Rm = 4.5 # resistance (kOhm)
Cm = 10 # capacitance (uF)
tau_m = Rm*Cm # time constant (msec)
tau_ref = 4 # refractory period (msec)
Vth = 1 # spike threshold (V)
V_spike = 0.5 # spike delta (V)
## Input stimulus
I = 0.8 # input current (A)

#To count number of spikes
spikeCt = 0 #COUNTING NUMBER OF SPIKES PER ITERATION
spikes = [] #LIST TO TRACK SPIKERS PER RUN FOR EACH CURRENT LEVEL TESTED
coll = [I,I+1.0,I+3.0,I+5.0] #TO TEST FIRING RATE FOR DIFFERENT CURRENT INPUT LEVELS

## iterate over each time step
#Uncomment below section to test for firing rate vs. current level as per the collection above, "coll"
'''
for item in coll:
    for i, t in enumerate(time):
        if t > t_rest:
            #Vm[i] = Vm[i - 1] + I / Cm * dt
            Vm[i] = Vm[i-1] + (-Vm[i-1] + item*Rm) / tau_m * dt
        if Vm[i] >= Vth:
            spikeCt+=1
            Vm[i] += V_spike
            t_rest = t + tau_ref
    spikes.append(spikeCt)
'''

for i, t in enumerate(time):
    if t > t_rest:
        #Vm[i] = Vm[i - 1] + I / Cm * dt
        Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
    if Vm[i] >= Vth:
        Vm[i] += V_spike
        t_rest = t + tau_ref

# plot membrane potential trace
mat.plot(time, Vm)
mat.title('Leaky Integrate-and-Fire')
mat.ylabel('Membrane Potential')
mat.xlabel('Time')
mat.ylim([0,2])
mat.show()

#TO PLOT FIRING RATE VS. CURRENT LEVEL; uncomment to test
'''
mat.plot(coll, spikes)
mat.title('Leaky Integrate-and-Fire')
mat.ylabel('Number of Spikes')
mat.xlabel('Input Current')
mat.ylim([0,50])
mat.show()
'''
