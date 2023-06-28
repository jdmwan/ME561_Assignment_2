import fluids
velocity = [0.37,0.37,0.37,0.37,0.37,0.25,0.44,1.00,1.00]
Kvalues = [2.2,2.2,2.2,1.8,1.8,1.8,1.8,2.2,2.2]
head = []
headstotal = 0
for i in range(len(velocity)):
    head.append(fluids.core.head_from_K(K = Kvalues[i],V = velocity[i]))
    print(i+1, ": ", head[i])
    if i == 0:
        headstotal += head[i]
print(headstotal)
