from math import sqrt

def aux (x):
	ret = [0]*3
	ret[x % 3] = (-1) ** (x//3)
	return ret
	
def aux1 (x):
	ret = [1/3]*3
	ret[0] *= (-1)**(x % 2)
	ret[1] *= (-1)**((x % 4) // 2)
	ret[2] *= (-1)**(x//4)
	return ret
	
def dist (p, q):
	return sqrt (sum ((px - qx) ** 2.0 for px, qx in zip(p, q)))

def recsearch (start, amount):
     for x in range (start, 14):
         amount.append (points[x])
         if len (amount) != 4:
             recsearch (x + 1, amount)
         else:
             distances = set ()
             for y in amount:
                 for z in amount:
                     if y != z:
                         d = dist (y, z)
                         distances.add (d)
             if len (distances) == 1:
                 print (amount)
         amount.pop ()

points = []
for x in range (6):
	points.append (aux (x))
for x in range (8):
	points.append (aux1 (x))
recsearch (0, [])
