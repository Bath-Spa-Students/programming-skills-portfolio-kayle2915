import math 
# finding the area of triangle using herons equation 

def triangle_area_heron(a,b,c):

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a ) * (s - b ) * (s - c))
    return area 

a = float(input("enter the A side of triangle: "))
b = float(input("enter the B side of triangle: "))
c = float(input("enter the C side of triangle: "))

print(" the area of the triangle is", triangle_area_heron(a,b,c))



