# std={'name':'akhil','age':'21','place':'ekm'}
# print(std['name'],std['age'],std['place'])
# std['name']='manu'
# print(std)
# std['mark']=20
# print(std)
# for i in std:
#     print(i,std[i])

# d={'name':'anu','age':'23'}
# l=[1,2]
# print(d.fromkeys(l))

# d={'name':'anu','age':'23'}
# d.pop('name')
# print(d)

# d={'name':'anu','age':'23','place':'ekm'}
# d.popitem()
# print(d)

# d={'name':'anu','age':'23','place':'ekm'}
# d.setdefault('mark')
# d.update({'mark':'50'})
# print(d)

# d={'name':'anu','age':'23','place':'ekm'}
# a=d.copy()
# print("copy :",a)
# print(id(a))
# print(id(d))

# table

# dlt=[{'name':'anu','age':30,'place':'clk'},{'name':'kanu','age':24,'place':'tvm'},{'name':'manu','age':45,'place':'kozi'},{'name':'anoop','age':29,'place':'alp'}]
# for i in range(0):
#     name=input('name')
#     age=int(input("age"))
#     place=input('place')
#     dlt.append({'name':name,'age':age,'place':place})
# print("{:<10}{:<10}{:<10}".format("name","age","place"))
# print('_'*25)
# for i in dlt:
#     print("{:<10}{:<10}{:<10}".format(i["name"],i["age"],i["place"]))
# print('\tage>30')
# print("{:<10}{:<10}".format("name","age"))
# print('_'*15)
# for i in dlt:
#     if i['age']>=30:
#         print("{:<10}{:<10}".format(i["name"],i["age"]))

# print('\tage<30')
# print("{:<10}{:<10}".format("name","age"))
# print('_'*15)
# for i in dlt:
#     if i['age']<30:
#         print("{:<10}{:<10}".format(i["name"],i["age"]))


num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
a = input("Enter a number: ") 

for digit in a:
    if digit.isdigit() in num:
        print(num[int(digit)], end=' ')
    else:
        print("Invalid input")
        break
else:
    print() 

# number = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
# a = int(input('Enter a number: '))
# result = ''
# while a >0:
#     digit = a % 10  
#     word = number[digit]  
#     result = word + ' ' + result 
#     a = a // 10 
# result = result
# print(result)
