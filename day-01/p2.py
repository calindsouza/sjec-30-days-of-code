a=int(input("enter starting value"))
b=int(input("enter ending value"))
for i in range(a,b+1):
    if i%3==0:
        print("Foo")
    elif i%2==0:
        print("Bar")
    else:
        print("Baz") 