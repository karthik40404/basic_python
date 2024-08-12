a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
if a>b:
    if a>c:
       print(a)
    else:
       print(c) 
else:
    if b>c:
        print(b)
    else:
        print(c)              


a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
d=int(input("enter a number :"))
if a>b:
    if a>c:
        if a>d:
            print(a,"is the largest number")
        else:
            print(d,"is the largest number")
    else:
        if c>d:
            print(c,"is the largest number")
        else:
            print(d,"is the largest number")        
else:
    if b>c:
        if b>d:
         print(b,"is the largest number")
        else:
         print(d,"is the largest number")    
    else:
        if c>b:
         print(c,"is the largest number")
        else:
         print(b,"is the largest number")   
   
a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
d=int(input("enter a number :")) 
if a>b and a>c and a>d:
    print(a,"is the largest number")
elif b>c and b>d and b>a:
    print(b,"is the largest number")
elif c>a and c>b and c>d:
    print(c,"is the largest number")
else:
    print(d,"is the largest number")  


a=("welcome home")
f=input("enter a word ")
if f in a:
    print("yes")
else:
    print("no")

a=input("enter a word :")
if len(a)>=8 and len(a)<=12:
    print("valid")
else:
     print("invalid")

