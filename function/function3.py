'''operator'''
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def mod(a,b):
#     return a%b
# def numbers():  
#     a=int(input('enter a number :'))  
#     b=int(input('enter a number :')) 
#     return a,b 
# while True:
#     print("1.add,2.sub,3.mul,4.div,5.mod,6.exit")
#     choice=int(input('enter your choice :'))
#     if choice==1:
#         a,b=numbers()
#         print(add(a,b))
#     elif choice==2:
#         a,b=numbers()
#         print(sub(a,b))
#     elif choice==3:
#         a,b=numbers()
#         print(mul(a,b))
#     elif choice==4:
#         a,b=numbers()
#         print(div(a,b))
#     elif choice==5:
#         a,b=numbers()
#         print(mod(a,b))
#     elif choice==6:
#         break

'''Lambda function'''

# add=lambda a,b:a+b
# print(add(2,7))    

# add=lambda a,b:a+b
# sub=lambda a,b:a-b
# mul=lambda a,b:a*b
# div=lambda a,b:a/b
# mod=lambda a,b:a%b
# def numbers():  
#     a=int(input('enter a number :'))  
#     b=int(input('enter a number :')) 
#     return a,b 
# while True:
#     print("1.add,2.sub,3.mul,4.div,5.mod,6.exit")
#     choice=int(input('enter your choice :'))
#     if choice==1:
#         a,b=numbers()
#         print(add(a,b))
#     elif choice==2:
#         a,b=numbers()
#         print(sub(a,b))
#     elif choice==3:
#         a,b=numbers()
#         print(mul(a,b))
#     elif choice==4:
#         a,b=numbers()
#         print(div(a,b))
#     elif choice==5:
#         a,b=numbers()
#         print(mod(a,b))
#     elif choice==6:
#         break

'''Build in function'''
'''map function'''
# l=[1,2,3,4,5,6]

# data=list(map(lambda a:a**2,l))#build in function
# print(data)

# l=[1,2,3,4,5,6]
# def fun(a):# normal function
#     return a**2
# data1=map(fun,l)
# print(list(data1))

'''filter function'''

# l=[1,2,3,4,5,6]
# data=list(filter(lambda a:a%2==0,l))#build in function
# print(data)

# def function(a):# normal function
#     return a%2==0
# data1=filter(function,l)
# print(list(data1))

# l=['apple','mango']#string
# data=list(filter(lambda a:a[0]=='a',l))
# print(data)

'''reduce function'''

import functools
l=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total*value,l)
print(data)