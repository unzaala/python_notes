#find area of shapes (circle,square ,triangle, rectangle)
while(True):
    print("enter 1 for area of circle ")
    print("enter 2 for area of square ")
    print("enter 3 for area of triangle ")
    print("enter 4 for area of rectangle ")
    print("enter 5 for exit ")
    choice=int(input("enter your choice = "))
    if (choice==1):
        radius=float(input("enter radius : "))
        area=3.14*radius*radius
        print("area of circle =",area)
    elif(choice==2):
        length=int(input("enter length : "))
        area =length*length
        print("area of square =",area)
    elif(choice==3):
        length=int(input("enter length : "))
        breadth=int(input("enter breadth : "))
        area=1/2*length*breadth
        print("area of triangle =",area)
    elif(choice==4):
        length=int(input("enter length : "))
        breadth=int(input("enter breadth : "))
        area=length*breadth
        print("area of rectangle =",area)
    elif(choice==5):
        break
    else:
        print("invalid choice!!!")
        

