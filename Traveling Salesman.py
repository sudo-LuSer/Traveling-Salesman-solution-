import math
import cmath
import matplotlib.pylab as plt 
def distance(x,y,a,b):
	X = (x-a)**2 
	Y = (x-b)**2 
	return math.sqrt(float(X+Y))
XAxis = int(input("where are you in X-Axis :"))
YAxis = int(input("where are you in Y-Axis :"))
N = int(input("Number of cities in map : "))
CitiesCordinates = []
for i in range(0,N):
	z = i+1 
	x = float(input("Enter the x-axis of city number "+str(z)+str(':')))
	y = float(input("Enter the y-axis of city number "+str(z)+str(':')))
	CitiesCordinates.append([x,y,z])
XGraph = [x[0] for x in CitiesCordinates]
YGraph = [y[0] for y in CitiesCordinates]
min = cmath.inf
SavedX = 0
SavedY = 0
sortedMap = []
BESTINDEX = -min
ToDelet=[]
for i in range(0,N):
	for axis in CitiesCordinates:
		if(min > distance(XAxis,YAxis,axis[0],axis[1])):
			min = distance(XAxis,YAxis,axis[0],axis[1])
			SavedX = axis[0]
			SavedY = axis[1]
			BESTINDEX = axis[2]
			ToDelet = axis
	sortedMap.append(BESTINDEX)
	plt.plot(XAxis, YAxis, SavedX, SavedY, marker = 'o')
	XAxis = SavedX
	YAxis = SavedY
	min = cmath.inf
for index in sortedMap:
	print(index)
plt.show()