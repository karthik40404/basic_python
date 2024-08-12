class person():
    def __init__(self) -> None:
        print('register')

class employee(person):
    def log(self):
        print('login')

class manager(employee):
    def add(self):
        print('add employee')

class departmenthead(manager,employee):
    def monitor(self):
        print('monitoring')

class hr_manger(departmenthead):
    def manage(self):
        print('managing')

sanu=employee()
sanu.log()

manu=hr_manger()
manu.manage()

ani=departmenthead()
manu.add()