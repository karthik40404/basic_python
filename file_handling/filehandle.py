# t=open('python_programs/file_handling/new1.txt','w')
# t.write('124k'+'lkjhgfd')

# t=open('python_programs/file_handling/new2.txt','w')
# a=int(input("enter the limit :"))
# for i in range(a):
#     b=input("enter the name :")
#     t.write(b+"\n")

# t=open('python_programs/file_handling/new3.txt','a')
# t.write("blah")

# t=open('python_programs/file_handling/new3.txt','r') #'r' is used for read
# print(t.read(1))
# print('-'*20)
# print(t.read(5))

# t=open('python_programs/file_handling/new1.txt','r') 
# print(t.readline(1))
# print('-'*20)
# print(t.readline())
# print(t.readline(6))

# t=open('python_programs/file_handling/new1.txt','r') 
# print(len(t.readlines()))

# t=open('python_programs/file_handling/new1.txt','r')
# l=len(t.readlines())
# t.seek(0)
# for i in range(l):
#     a=t.readline().strip()
#     print(a[::-1])

# t=open('python_programs/file_handling/new1.txt','r')
# l=len(t.readlines())
# t.seek(0)
# c=0
# for i in range(l):
#     a=t.readline().strip()
#     b=a.split()
#     print(len(b))
#     # print(a[::-1])
#     c+=1
# print(c)
# t.close()

# t=open('python_programs/file_handling/new1.txt','r')
# l=len(t.readlines())
# t.seek(0)
# word=0
# for i in range(l):
#     a=t.readline().strip()
#     for j in a:
#         if j ==' ':
#             word+=1
#     print(a[::-1])
#     word+=1
# print(word)

# t=open('python_programs/file_handling/new1.txt','r')
# l=len(t.readlines())
# t.seek(0)
# word=0
# let=0
# for i in range(l):
#     a=t.readline().strip()
#     for j in a:
#             if j=='':
#                   word+=1
#             else:
#                   let+=1
#     print(a)
#     word+=1
# print(word)
# print(let)

# t=open('python_programs/file_handling/new1.txt','r')
# l=len(t.readlines())
# t.seek(0)
# word=0
# let=0
# cap=0
# for i in range(l):
#     a=t.readline().strip()
#     for j in a:
#             if j=='':
#                   word+=1
#             else:
#                   let+=1
#                   if j.isupper():
#                         cap+=1       
#     print(a)
#     word+=1
# print(word)
# print(let)
# print(cap)
# print("lower",let-cap)