

# for i in range (10):
#     print(i)



# for i in range(10):
#     print("welcome")



# for i in range(1,11):
#     print(i)



# for i in range(1,11,2):
#     print(i)    



# a=int(input("enter a number :"))
# b=int(input("enter a number :"))
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(sum)



# a=int(input("enter a number :"))
# b=int(input("enter a number :"))
# sum=0
# for i in range(a,b+1):
#     if i%2!=0:
#         print(i)
#         sum+=i   
# print("sum=",sum)         



# a=int(input("enter a number :"))
# b=int(input("enter a number :"))
# sum=0
# even=0
# odd=0
# for i in range(a,b+1):
#     if i%2!=0:
#         sum+=i    
#     if i%2==0:
#         even+=i
#     odd+=i
# print("odd number",sum)
# print("even number",even)
# print("natural number",odd)

    
# a=int(input("enter a number :"))
# mul=1
# for i in range(1,a+1):
#     mul*=i
# print(mul) 

# a=int(input("enter a number :"))
# for i in range(1,11):
#  print(i,"*",a,"=",a*i)

# for i in range(1,5):
#      print("*"*i)

# for i in range(3):
#      for j in range(3):
#           print("*")

# for i in range(3):
#      for j in range(3):
#         print("*",end="\t")
#      print()      

# for i in range(4):
#     for j in range(4):
#         print(j,end="\t")
#     print()    

# for i in range(4):
#      for j in range(4):
#           print(i,end="\t")    
#      print()     

# for i in range(4):
#      for j in range(4):
#           print(j,end="\t")    
#      print()     

# a=0
# for i in range(3):
#     for j in range(3):              
#          print(a,end="\t")
#          a+=1
#     print("\n")     

# for i in range(4):
#     a=2
#     for j in range(3):
#         if i%2==0:
#          print(j,end="\t")
#         else:
#            print(a,end="\t")
#            a-=1
#     print("\n")        

# a=0
# for i in range(3):
#     for j in range(3):              
#          print(a,end="\t")
#          a+=2
#     print("\n")     

# for i in range(4):
#      for j in range(4):
#           print(i+j,end="\t")
#      print()              

# """alternate"""

# for i in range(4):
#      a=i
#      for j in range(4):
#           print(a,end="\t")
#           a+=1
#      print()     

# for i in range(1,4):
#     for j in range(i):
#        print(j+1,end="\t")
#     print()   

# for i in range(1,4):
#     for j in range(i):
#        print(i,end="\t")
#     print()   

# for i in range(1,4):
#     for j in range(i):
#        i-=1
#        print(i+1,end="\t")
#     print() 

# a=0
# for i in range(1,5):
#     for j in range(i):
#         print(a**2,end="\t")
#         a+=1
#     print()    
  
# for i in range(3):
#     a=65
#     for j in range(4):
#         print(chr(a),end="\t")
#         a+=1
#     print()   

# for i in range(3):
#     a=65+i
#     for j in range(3):
#         print(chr(a),end="\t")
#     print("\n")   

# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end="\t")
#         a+=1  
#     print() 


# for i in range(1,4):
#     for j in range(i):
#        a=64
#        a+=i
#        print(chr(a),end="\t")
#     print()  

# for i in range(1,4):
#     for j in range(i):
#        a=65
#        a+=j
#        print(chr(a),end="\t")
#     print()  

# a=65
# for i in range(1,4):
#     b=a
#     for j in range(i):
#         print(chr(b),end="\t")
#         b-=1
#     print()
#     a+=1

# a=0
# for i in range(1,5):
#     b=a
#     for j in range(i): 
#      print(b,end="")
#      b-=1 
#      print("",end="") 

# for i in range(1,4):
#     for j in range(i):
#        print(j+1,end="\t")
#     print() 
# for i in range(2,0,-1):
#     for j in range(i):      
#        print(j+1,end="\t")
#     print()   

# for i in range(4):
#     for j in range(i): 
#        print("*",end="") 
#     print()
# for i in range(2,0,-1):
#     for j in range(i): 
#        print("*",end="") 
#     print()

# for i in range(1,4):
#     for j in range(i):
#        a=65
#        a+=j
#        print(chr(a),end="\t")
#     print()  
# for i in range(2,0,-1):
#     for j in range(i):
#        a=65
#        a+=j
#        print(chr(a),end="\t")
#     print()  

# a=0
# b=1
# for i in range(8):
#     print(a)
#     c=a+b
#     a=b
#     b=c
# print()    

# a=0
# b=1
# for i in range(8):
#     print(a)
#     a,b=b,a+b
# print()    


# for i in range(5):
#     print(i*i,end="\t")
# print("\n")

# for i in range(6):
#     print(i*3,end="\t")
# print("\n")

# squares=[]
# for i in range(6):
#     squares.append(i*i)
#     for square in squares:
#      print(square,end="")    