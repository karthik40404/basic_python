age=int(input("enter age"))
if age>=18:
    print("yes")
else:
    print("no")    

experiance=int(input("enter the years of work you have done :"))
salary=int(input("enter the salary :"))
if experiance>=5:
    print("yes,give 5% raise")
    print(salary*0.05+salary)
else:
    print("no")      

number=int(input("enter a number :"))
last_digit=number%10
if last_digit%3==0:
    print("the last digit of the number is divisible by 3")
else:
    print("the last digit of the number is not divisible by 3")

day=int(input("enter a number from 1 to 7 : "))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")    
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("invalid number")

city=str(input("enter your city :"))
if city=="delhi":
    print("red fort")
elif city=="agra":
    print("taj mahal")
elif city=="jaipur":
    print("jal mahal")
else:
    print("invaild city")    

unit=int(input("enter your unit you have used :"))
if unit<=100:
    print("no charges")    
elif unit<=200:
    print((unit-100)*5,"you have charges") 
else:
    print((unit-200)*10+500,"you have the charge")