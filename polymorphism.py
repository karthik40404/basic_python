# class sample:
#     def display(self):
#         print('sample class dis')
#     def s1(s):
#         print('sample class s1')

# class demo(sample):
#     def display(self):
#         print('start')
#         super().display()
#         print('demo class display')

#     def d1(s):
#         print('demo class d1')

# obj=demo()
# obj.display()

# class sample:
#     def __init__(self,name,age):
#         print('sample class dis')
#         print(name,age)
#     def s1(s):
#         print('sample class s1')

# class demo(sample):
#     def __init__(self,name,age):
#         print(name,age)
#         print('start')
#         super().__init__(name,age)
#         print('demo class display')

#     def d1(s):
#         print('demo class d1')

# obj=demo('anna',45)

class sample:
    def display(self,name,age):
        print('sample class dis')
        print(name,age)
    def s1(s):
        print('sample class s1')

class demo(sample):
    def display(self,name,age):
        print('start')
        super().display(name,age)
        print('demo class display')

    def d1(s):
        print('demo class d1')

obj=demo()
obj.display('anna',45)