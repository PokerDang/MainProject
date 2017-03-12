import random
import pylab as plb
position = 0
walk = [position]
steps = 100

for i in xrange(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

plb.plot(walk)

plb.show()