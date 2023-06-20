import fluids
import pint

GPM = [11,9,8,5,3,2,1]
diameter = [1/2*25.4/1000 , 3/4*25.4/1000, 1*25.4/1000,2*25.4/1000]
flowRate = []
pipeLossRate = 3*144/100 # for pipe loss in below 3/2 inch, in psi/ft
for rate in GPM:
    flowRate.append(rate*6.309e-5)
# bernoullis would be 
# pin +pipeloss = pout
#Pipe17
pressure17 = 50*1000 # 50 kpa
