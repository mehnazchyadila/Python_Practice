 #  Creating your own Module
"""
We can use this as our own module . Such as 

from area import *  
      OR 
from area import  triangle_area , rectangle_area

print(rectangle_area(20,30))
print(triangle_area(20,30))     
 
"""

def triangle_area(b,h):
    print(f"Area of Triangle  { 0.5 * b * h }")

def rectangle_area(b,h):
    print(f"Area of Triangle  { b * h }")

