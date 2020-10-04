import math, time, random
import numpy as np  #1
ntrials=10000 #2
dist=0
start_time=time.process_time()
for i in range(ntrials):      #3
    x1=np.random.random(ntrials)
    y1=np.random.random(ntrials)
    z1=np.random.random(ntrials)
    x2=np.random.random(ntrials)
    y2=np.random.random(ntrials)
    z2=np.random.random(ntrials)
    dist+=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))#4
dist/=ntrials
e_time=time.process_time()-start_time
ex_dist=1/105*(4+17*math.sqrt(2)-6*math.sqrt(3)+21*math.log(1+math.sqrt(2))+42*math.log(2+math.sqrt(3))-7*math.pi)
print("Ntrials=%d Ave dist=%9.7f Exact dist=%9.7f Elapsed time=%6.2f"%(ntrials,dist,ex_dist,e_time)) #5 & Extra Credit


