"""
Author: Karishma Shinde
Title: This code is for testing the point is inside the polygon or outside the polygon
Date Created: 18-06-2020
"""

#'''Code with input'''
from shapely.geometry import Point, Polygon
# Create Point objects
p1 = Point(0,0)
#p1=Point(3,8)
coords = [[-3,2], [-2,-0.8], [0,1.2], [2.2,0], [2,4.5]]
#coords = [[1,0], [8,3], [8,8], [1,5]]
poly = Polygon(coords)

print(p1)
print(poly)

print(p1.within(poly))

     
'''Code with user define value.input is taken by user'''
from shapely.geometry import Point, Polygon

# Create Point objects
p1 = Point(0,0)
#p1=Point(3,8)

# Create a Polygon
listLeng =int(input("Enter the number of sides of Polygon:"))
listLen = 2
coords = [[float(input("Enter side: ")) for _ in range(listLen)] for _ in range(listLeng)]
print(coords)
#coords = [[-3,2], [-2,-0.8], [0,1.2], [2.2,0], [2,4.5]]
poly = Polygon(coords)

print(p1)
print(poly)
#whitin keyword is used to check the availability of point
print(p1.within(poly))