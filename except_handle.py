# try:
#     a=int(input('enter a number :'))
#     a+=1
#     print(a)
# except:
#     print('input a int')

# while True:
#     try:
#         a=int(input('enter a number :'))
    #     a+=1
    #     print(a)
    #     break
    # except:
    #     print('input a int')

# l=[1,2,3,4,'haha',9]
# sum=0
# for i in l:
#     try:
#        sum+=i
#     except:
#         pass
# print(sum)

try:
    print('1'+'abc')
except NameError:
    print('namerror')
except TypeError:
    print('typerror')
else:
    print('else')
finally:
    print('final')
