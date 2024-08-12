import re
# a='welcome'
# print(re.sub('w','W',a))
# print(re.sub('welcome','python',a))
# b=re.split('l',a)
# print(b)
# c='hello world'
# print(re.split('',c))
# print(re.findall('e',a))
# print(re.findall('e',c))
# print(len(re.findall('e',a)))

# d='thank0 you'
# print(re.search('y',d))
# if re.search('o',d):
#     print('yes')
# else:
#     print('no')

# print(re.search('[0-9]',d))




# e='abcd'
# print(re.search('a',e))
# print(re.search('d',e))
# print(re.search('c.',e))
# print(re.search('d.',e))
# print(re.search('a..',e))
# print(re.search('d.',e))
# print(re.search('b.*',e))
# print(re.search('d.*',e))
# print(re.search('b.+',e))
# print(re.search('d.+',e))
# print(re.search('d.?',e))
# print(re.search('b.?',e))

'''using AND method'''
# a="abcD123"
# print(re.search('[a-z]',a))
# print(re.search('[a-z][0-9]',a))

# print(re.search('[a-z][0-9]',a))

# print(re.search('[a-z][A-Z][0-9]',a))

# '''using OR method'''
# b='abcd123'
# print(re.search('[a-z0-9]',b))

# '''for finding the last valuve in list'''

# c='asd123'
# print(re.search('[a-z]$',c))
# print(re.search('[0-9]$',c))
# print(re.search('3$',c))

'''phno validation'''

# a=''
# a=str(input('enter phno :'))
# if len(a)==10 and a.isdigit():
#     if re.search('[6-9].{9}',a):
#         print('valid phone no!')
#     else:
#         print('invalid phno!')
# else:
#     print("invalid")

# a=input('enter a number :')
# if len(a)==10 and a.isdigit() and re.search('[6-9].{9}',a):
#     print('valid')
# else:
#     print('invalid')





'''Password validation'''

a=input('enter password :')
pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]).{8,}$"
if re.search(pattern,a):
    print('valid password!')
else:
    print('invalid password!')
