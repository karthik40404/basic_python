# list=[1,2,3,4,3,5,'a','a','d']
# for i in range(len(list)):
#     if list[i] not in list[:i]:
#         print(list[i])

# for i in range(5):
#     a=65+i
#     for j in range(i):
#         print(chr(a),end="\t")
#         a+=j
#     print()   

for i in range(4):
    for j in range(i,-1,-1):
       a=65
       a+=i
       print(chr(65+j),end="\t")
    print()  

