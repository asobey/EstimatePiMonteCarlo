#! python 3
#! estimatePi - estimating pi using monte carlo simulation

from __future__ import division
from random import random
#from math import pi
#import matplotlib.pyplot as plt

#Simulate rain in square field and counting which fall within inscribed circle defined by x^2 + y^2 = r^2

def rainDrop(fieldLength=1):
    return[random()*fieldLength-.5, random()*fieldLength-.5] #random raindrop in square centered at 0,0

def checkPointInCircle(point, fieldLength=1):
    return (point[0]**2 + point[1]**2 <= (fieldLength/2)**2) #return if true

drops = 0
dropsInCircle = 0

for i in range(1,1000000):
    drops += 1

    if checkPointInCircle(rainDrop()) == True:
        dropsInCircle += 1

    if i < 20:
        pi = 4 * dropsInCircle / drops
        print('pi at %s drops is %s' % (i, pi))
pi = 4 * dropsInCircle / drops
print('pi is %s' % pi)