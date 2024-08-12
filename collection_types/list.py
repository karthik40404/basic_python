# l=[1,2,"welcome",1,3]
# print(l[2])

# l=[1,2,"welcome",1,3]
# if 2 in l:
#     print("is there")
# else:
#     print("is not there")    

# l=[1,2,"welcome",1,3]
# for i in l:
#     print(i)    
# print(type(l))
# print(len(l))

# l=[1,2,"welcome",1,3]
# l[2]="hello"
# print(l)


# l=[1,2,"welcome",1,3]
# del l[4]
# print(l)

# '''list methods'''


# L=[]
# L.append(20)
# L.append(24)
# print(L)



# L=[]
# L.append(20)
# L.append(24)
# L.insert(1,50)
# L.insert(4,[29,48,5])
# print(L)



# L=[]
# L.append(20)
# L.append(24)
# L.insert(1,50)
# L.insert(4,[29,48,5])
# L.extend([100,200,50])
# print(L)


# L=[]
# L.append(20)
# L.append(24)
# L.append(246)
# L.append(55)
# L.insert(1,50)
# L.insert(4,[29,48,5])
# L.extend([100,200,50])
# L.remove(20)
# L.remove([29,48,5])
# print(L)


# name=[]
# a=int(input("enter the limit :"))
# for i in range(a):
#     b=str(input("enter the name"))
#     name.append(b)
#     print(name)



# name=[]
# while True:
#     print('1.add\n2.display\n3.update\n4.delete\n5.exit')
#     choice=int(input("enter your choice :"))
#     if choice==1:
#         limit=int(input('enter the limit :'))
#         for i in range(limit):
#             b=str(input("enter a names :"))
#             name.append(b)
#     elif choice==2:
#         for i in name:
#             print(i)
#     elif choice==3:
#         old_name=input('enter name to update :')
#         if old_name in name:
#             new_name=input('new_name :')
#             pos=name.index(old_name) 
#             name[pos]=new_name
#     elif choice==4:
#         old_name=input('enter name:')
#         if old_name in name:
#             name.remove(old_name)      
 
# list=[1,2,3,4,3,5]
# for i in range(len(list)):
#     if list[i] not in list[:i]:
#         print(list[i])

# l1=[1,2,3,2,3,4]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)


# l=[1,2,3,4,5,'q','s','d']
# print("list: ",l)
# sum=0
# for i in l:
#     if type(i) in (int,float):
#         sum+=i
# print("sum = ",sum)

# numbers=[15,22,8,99,19,42]
# print('numbers')
# largest_number=numbers[0]
# for i in range(1,len(numbers)):
#     if numbers[i]>largest_number:
#         largest_number=numbers[i]
# print('the largest number is :', largest_number)
