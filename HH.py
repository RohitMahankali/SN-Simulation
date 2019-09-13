from numpy import *
from pylab import *



def alpha_m(v):
    return .1*(v+40)/(1-exp(-(v+40)/10))

def beta_m(v):
    return 4*exp(-v-65/18)

def alpha_h(v):
    return 0.07*exp(-v-65/20)

def beta_h(v):
    return 1/(exp((-v-35)/10)+1)

def alpha_n(v):
    return .01 * (v + 55) / (1 - exp(-(v + 55) / 10))

def beta_n(v):
    return 0.125 * exp(-v-65/80)



#Simulation parameters
T = 50
dt = 1
times = [i*dt for i in range(int(T/dt)+1)]
#time = arange(0,T+dt,dt)
t_ref = 2
t_rest = 0

#Current
I = [0 for _ in range(len(times))]


for i in range(len(times)):
    if times[i]>=10 and times[i]<=15:
        I[i] = 10

Vth = -55


#Begin code by setting up vars

#Voltage (Potential) Trace over time
V = [-65 for _ in range(len(times))]

#Gating values below
m = alpha_m(0)/(alpha_m(0)+beta_m(0))
n = alpha_n(0)/(alpha_n(0)+beta_n(0))
h = alpha_h(0)/(alpha_h(0)+beta_h(0))

#Max conductance values below
gNaMax = 120
gKMax = 36
gLMax = 0.3

#True conductances (To be plugged into H-H equation)
gNa = 0
gK = 0
gL = 0

#Equilibrium element channel potentials
ENa = 55
EK = -72
EL = -50

#Capacitance of System
C = 1

#Model logic
dV = 0
for i in range(len(V)-1):

    m = alpha_m(V[i]) / (alpha_m(V[i]) + beta_m(V[i]))
    n = alpha_n(V[i]) / (alpha_n(V[i]) + beta_n(V[i]))
    h = alpha_h(V[i]) / (alpha_h(V[i]) + beta_h(V[i]))

    #print (m,n,h)

    gNa = gNaMax * (m ** 3) * h
    gK = gKMax * (n ** 4)
    gL = gLMax

    #print (gNa,gK,gL)
    #print V[i]

    if times[i] > t_rest:
        dV = I[i] - gNa*(V[i]-ENa)-gK*(V[i]-EK)-gL*(V[i]-EL)
        #print dV
        #print dV*.1
        constant = dt/C

        dV = dV * constant
        #print dV
        V[i+1] = V[i] + dV
        print V[i+1]
        m += dt*(alpha_m(V[i])*(1-m) - beta_m(V[i])*m)
        h += dt*(alpha_h(V[i]) * (1 - h) - beta_h(V[i]) * h)
        n += dt * (alpha_n(V[i]) * (1 - n) - beta_n(V[i]) * n)

    if V[i+1] >= Vth:
        V[i+1] = 30
        t_rest = times[i]+t_ref
        m = alpha_m(V[i]) / (alpha_m(V[i]) + beta_m(V[i]))
        n = alpha_n(V[i]) / (alpha_n(V[i]) + beta_n(V[i]))
        h = alpha_h(V[i]) / (alpha_h(V[i]) + beta_h(V[i]))


plot(times,V)
title("Hodgkin-Huxley Model Chart")
xlabel("Time")
ylabel("Membrane Potential")
ylim([-80,35])
xlim([0,30])
show()






