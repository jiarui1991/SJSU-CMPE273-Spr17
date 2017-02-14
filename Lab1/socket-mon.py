import psutil
import collections
from collections import Counter
import numpy as np

container = []
i = 0

#Create 2D string array to store connection results

for c in psutil.net_connections(kind='inet'): 
	if c.raddr is not () and c.laddr is not ():
		 laddr = "%s@%s" % (c.laddr)  
		 raddr = ""
		 if c.raddr:
			  raddr = "%s@%s" % (c.raddr)
		 container.append([])
		 container[i].append(c.pid)
		 container[i].append(laddr)
		 container[i].append(raddr)
		 container[i].append(c.status)
		 i += 1

#sort the array by pid frequency
t = tuple(y[0] for y in container)
counter = collections.Counter(t)
res = sorted(container, key=lambda x:counter[x[0]], reverse=True)

#print out the sorted array
for el in res:
    print (el)



