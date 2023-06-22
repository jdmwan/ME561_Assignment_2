import fluids.core as core
import fluids.friction as friction
import math
pi = math.pi
kinVisc = 8.917e-7
countLength = 0
relRough = 0.001
GPM = [11,11,11,11,11,9,8,5,2,2,2,3,3,1,5,3,2]
diameter = [1/2, 3/4, 1,2]
lengths = [5,13,4,0,0.75,6,2.5,1.5,3,2,1.75,2.5,1.25,1.25,6.25,3,4.25]
pipeDiameter = []
for index in range(len(lengths)):
    lengths[index] = lengths[index]*3.2808399
flowRate = []
pipeLossRate = 3*144/100 # for pipe loss in below 3/2 inch, in psi/ft
for rate in GPM:
    flowRate.append(rate)
# bernoullis would be 
# pin +pipeloss = pout
#Pipe17
pressure17 = 50*20.88543 # 50 kpa to psf
Losses17 = pipeLossRate*lengths[16]
pressure16 = 100*20.88543 # 50 kpa to psf
Losses16 = pipeLossRate*lengths[15]
pressure15 = pressure16 + pressure17 + Losses16 + Losses17
# print(pressure17)
# print(flowRate)
for L in lengths:
    
    for D in diameter:
        if D <= 1.5:
            Velocity =  0.4084*flowRate[countLength] / D/D
            # print(Velocity)
            Red = core.Reynolds(V = Velocity/3.2808399, D=D/0.3048, nu = kinVisc)
            # print(Red)
            f = friction.friction_factor(Re = Red, eD = relRough/D/0.3048)
            
            newD = Velocity**2 * f * 100 / 3 / 2/ 9.81
            print(newD)
            if newD - D <0:
                print("hi")
                pipeDiameter.append(D)
                break
            

        else:
            pipeDiameter.append(D)
            

    
    countLength += 1
print(pipeDiameter)