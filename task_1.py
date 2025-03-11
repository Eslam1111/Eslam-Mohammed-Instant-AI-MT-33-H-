Base = float(input("enter the Bace"))
Hight = float(input("enter the hight"))
area = (Base*Hight)/2
print(area)


#------------------------------------------------------------
x = int(input("enter the integer x"))
y = int(input("enter the integer y"))
print( f"befor changes {x},{y}")
swap = x
x = y
y = swap
print( f"After changes 1 : {x},{y}")
#or 
x, y = y, x
x, y = y, x
print(f"After changes 2 : {x} {y}")

#------------------------------------------------------------

kilometers = float(input("Enter the distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")