#1
a=[1,-2,-23,56,34,-9,45]
for i in a:
    if i>=0:
        print("Positive",i)
    else:
        print("Negative",i)
#2
a=int(input("Enter the number:"))
if a%2==0:
    print(a,"Even number")
else:
   print (a,"Odd number")
#3
a=int(input("Enter base:"))
b=int(input("enter exponent"))
c=a**b
print("The power is",c)
#4
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater")
else:
    print("a is greater than b")
#5
Year=int(input("Enter the year:"))
if  (Year%4==0 and Year%100!=0) or Year%400==0:
    print("leap year")
else:
    print("not a leap year")
#6
a=int(input("Enter your grade:"))
if a>=90:
    print("A")
elif a>=80:
    print("B")
elif a>=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F")
#7
age=int(input("Enter your age:"))
if age>=25:
    print("you can do pretty much anything")
elif age>=18:
    print("You can vote but not rent a car")
elif age>=16:
    print("You can drive but not vote")
else:
    print("You can't drive")
#8
for i in range(1,101):
  if (i%3==0 and i%5==0):
    print(i,"FizzBuzz")
  elif (i%3==0):
    print(i,"fizz")
  elif (i%5==0):
    print(i,"Buzz")
#9

Year=int(input("Enter the year:"))
if  (Year%4==0 and Year%100!=0) or Year%400==0:
    print("leap year")
else:
    print("not a leap year")
