import fluids


GPM = [11,9,8,5,3,2,1]
diameter = [1/2*25.4/1000 , 3/4*25.4/1000, 1*25.4/1000,2*25.4/1000]
lengths = [5,13,4,0,0.75,6,2.5,1.5,3,2,1.75,2.5,1.25,1.25,6.25,3,4.25]
flowRate = []
pipeLossRate = 3*144/100 # for pipe loss in below 3/2 inch, in psi/ft
for rate in GPM:
    flowRate.append(rate*6.309e-5)
# bernoullis would be 
# pin +pipeloss = pout
#Pipe17
pressure17 = 50*20.88543 # 50 kpa to psf
Losses17 = pipeLossRate*lengths[16]
pressure16 = 100*20.88543 # 50 kpa to psf
Losses16 = pipeLossRate*lengths[15]
pressure15 = pressure16 + pressure17 + Losses16 + Losses17
print(pressure17)
