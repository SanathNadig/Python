import math

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (math.pi * self.radius**2 * self.height)   
    
    def surface_area(self):
        return ( 2 * math.pi * self.radius * (self.radius + self.height))

cyl = Cylinder(2,3)

print ('the volume of the cylinder is {c:1.2f}'.format(c=cyl.volume()))
print ('the surface area is {c:1.2f} \n \n'.format(c=cyl.surface_area()))

class Line:
    
    def __init__(self,coor1,coor2):
        self.x1,self.y1 = coor1
        self.x2,self.y2 = coor2
    
    def distance(self):
        return (math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))
    
    def slope(self):
        return ((float(self.y2 - self.y1))/(self.x2 - self.x1))

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print ('the distance between the 2 points is {d:1.2f}'.format(d=li.distance()))
print ('the slope of the line joining the 2 points is {s:1.2f}'.format(s=li.slope()))