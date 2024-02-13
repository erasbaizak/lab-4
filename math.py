import math
#1ex
degree= float(input("Input degree: "))
radian = degree * (math.pi / 180)
print(radian)
#2ex
height=int(input("height: "))
first=int(input("first: "))
second=int(input("second: "))
print((first+second)*(height/2))
#3ex
sides = int(input("sides: "))
length = float(input("length of a side: "))
area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
print(area)
#4ex
length=(float(input("length: ")))
heigth=float(input("heigth: "))
print(float(length*heigth))