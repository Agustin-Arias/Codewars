# One Line Task: Circle Intersection
# https://www.codewars.com/kata/5908242330e4f567e90000a3/
from math import *;circleIntersection=lambda x,y,r:int(r*r*(lambda a:a-sin(a))(2*acos(min(1,hypot(x[0]-y[0],x[1]-y[1])/2/r))))
