import math
import fluids
pi = math.pi
kinVisc = 8.917e-7
roughness = 0.001/1000
# dIn = [2,2,2,2,2,1,1,0.75,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.5,0.5]
dIn = [1,1,1,1,1,1,1,0.75,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.5,0.5]
lengths = [5,13,4,0.75,6,4,2.5,1.5,3,2,1.75,2.5,1.25,1.25,6.25,3,4.25]
print(len(lengths))
dia = []
for d in dIn:
    dia.append(d*25.4/1000)
# print(dia)
# GPM = [11,11,11,11,11,9,8,5,2,2,2,3,3,1,5,3,2]
GPM = [3,3,3,3,3,3,2,2,2,2,2,0,0,1,0,0,0]
flowrate = []
for rate in GPM:
    flowrate.append(rate * 6.309E-5)
# print(flowrate)
velocity = []
for i in range(len(flowrate)):
    area = (dia[i]/2)**2*pi
    velocity.append(flowrate[i]/area)
print(velocity)
Red = []
for i in range(len(velocity)):
    Red.append(fluids.core.Reynolds(D = dia[i], V=velocity[i],nu=kinVisc))
# print(Red)
f = []
Klosses = []
heads = []
for i in range(len(velocity)):
    if Red[i] != 0:
        f.append(fluids.friction.friction_factor(Re=Red[i], eD = roughness/dia[i]))
        Klosses.append(fluids.core.K_from_f(fd=f[i], L = lengths[i], D=dia[i]))
        heads.append(fluids.core.head_from_K(K = Klosses[i], V = velocity[i] ))
    else:
        f.append(0)
        Klosses.append(0)
        heads.append(0)
heads[0] = heads[0] 
heads[10] = heads[10] 
# print(f)
# print(Klosses)
# print(heads)
# print(velocity[10]**2 / 2 / 9.81)
headstotal = 0
for i in range(len(heads)): 
    if i<2:
        headstotal += heads[i]
# print(headstotal)