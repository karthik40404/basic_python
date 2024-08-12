'''single inheritence'''

# class A:
#     def a1(self):
#         print('a1')
# class B(A):
#     def b1(self):
#         print('b1')        

# class synn:
#     def __init__(self) -> None:
#         print('register')
#     def py(s):
#         print('py in synn')
#     def ph(s):
#         print('ph in synn')

# class nov(synn):
#     def dm (s):
#         print("dm")
#     def web(s):
#         print('web')

# manu=synn()
# manu.py()

# sanu=nov()
# sanu.web()

'''multiple inheritence'''

# class A:
#      def a1(self):
#          print('a1')
# class B:
#      def b1(self):
#          print('b1')  
# class C(A,B):
#      def c1(self):
#          print('c1')  
    
# class synn:
#     def __init__(self) -> None:
#         print('register')
#     def py(s):
#         print('py in synn')
#     def ph(s):
#         print('ph in synn')

# class nov:
#     def dm (s):
#         print("dm in nov")
#     def web(s):
#         print('web in nov')

# class std(nov,synn):
#     def reg(self):
#         print('std reg')

# manu=synn()
# manu.py()

# sanu=nov()
# sanu.web()

# anu=std()
# anu.ph()

'''multilevel inheritence'''

# class A:
#      def a1(self):
#          print('a1')
# class B(A):
#      def b1(self):
#          print('b1')  
# class C(B):
#      def c1(self):
#          print('c1') 

# class synn:
#     def __init__(self) -> None:
#         print('register')
#     def py(s):
#         print('py in synn')
#     def ph(s):
#         print('ph in synn')

# class nov(synn):
#     def dm (s):
#         print("dm in nov")
#     def web(s):
#         print('web in nov')

# class staff(nov):
#     def reg(self):
#         print('std reg')

# manu=synn()
# manu.ph()

# sanu=nov()
# sanu.dm()

# anu=staff()
# anu.reg()

'''heirarchial inheritence'''

# class A:
#      def a1(self):
#          print('a1')
# class B(A):
#      def b1(self):
#          print('b1')  
# class C(A):
#      def c1(self):
#          print('c1') 

# class synn:
#     def __init__(self) -> None:
#         print('register')
#     def py(s):
#         print('py in synn')
#     def ph(s):
#         print('ph in synn')

# class nov(synn):
#     def dm (s):
#         print("dm in nov")
#     def web(s):
#         print('web in nov')

# class staff(synn):
#     def reg(self):
#         print('std reg')

# manu=synn()
# manu.ph()

# sanu=nov()
# sanu.web()

# anu=staff()
# anu.py()

'''hybrid inheritence'''

# class A:
#      def a1(self):
#          print('a1')
# class B:
#      def b1(self):
#          print('b1')  
# class C(A,B):
#      def c1(self):
#          print('c1') 
# class F:
#      def f1(self):
#          print('f1') 
# class D(B,F):
#      def d1(self):
#          print('d1') 
# class E(C,D,A,B,F):
#      def e1(self):
#          print('e1') 




