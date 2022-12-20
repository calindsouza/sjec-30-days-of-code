n=int(input("enter number of triangles"))
for i in range(1,n+1):
    
    side1=int(input("enter frist side value "))
    side2=int(input("enter second value"))
    side3=int(input("entr third value"))
    
    while i%3==1:
        if side1<=side2<=side3:
            print(side1)
        elif side1<=side3<=side2:
            print(side1)
        elif side2<=side1<=side3:
            print(side2)
        elif side2<=side3<=side1:
            print(side2)
        elif side3<=side1<=side2:
            print(side3)
        else:
            print(side3)
        break  
    
    while i%3==2:
        if side1<=side2<=side3:
            print(side2)
        elif side1<=side3<=side2:
            print(side3)
        elif side2<=side1<=side3:
            print(side1)
        elif side2<=side3<=side1:
            print(side3)
        elif side3<=side1<=side2:
            print(side1)
        else:
            print(side2)
        break

    while i%3==0 :
        if side1<=side2>=side3:
            print(side2)
        elif side1<=side3>=side2:
            print(side3)
        elif side2<=side1>=side3:
            print(side1)
        elif side2<=side3>=side1:
            print(side3)
        elif side3<=side1>=side2:
            print(side1)
        else:
            print(side2)
        break      

