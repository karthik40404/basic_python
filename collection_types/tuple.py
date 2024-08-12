# t=(1,2,3)
# print(type(t))
# t1=1,
# print (type(t1))

# t=1,2,3
# num=int(input("enter a number :"))
# if num in t:
#     print("present")
# else:
#     print("not")


# t=1,2,3
# for i in t:
#     print(i)


# t=1,2,3,4
# print (t.index(2))

# t=1,2,3,4,3
# print (t.count(3))


# t=("kart",123,['kar',20])
# print(t[2])

# t=("kart",123,['kar',20])
# t[2][1]=21
# print(t[2][1])


# t=1,2,3,4,5
# a=list(t)
# a.insert(1,5)
# a.append(4)
# a.remove(4)
# t=tuple(a)
# print(t)

t=1,1,2,3,4,5,5
unique_list = []
for item in t:
    if item not in unique_list:
        unique_list.append(item)
t=tuple(unique_list)
print(t)
