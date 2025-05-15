#1
myName="Savithri"
My_age=22
print(myName,My_age)
#2
a=10
b=20
print("sum",a+b)
#3
pi=3.14
r=8
areaofcircle=pi*r**2
print(areaofcircle)
#4
length=10
width=5
areaofrectangle=length*width
print("Area",areaofrectangle)
#5
height=8
base=10
areaoftriangle=(height*base)/2
print("Area",areaoftriangle)
#6
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
op=input()
if op=="add":
    print("add",a+b)
elif op=="sub":
    print("sub",a-b)
elif op=="multiply":
    print("Multiply",a*b)
elif op=="div":
    print("Div",a/b)
else:
    print("Invalid operation")
#7
a=50
a+=5
a-=5
a*=5
a/=5
print("Final ans",a)
#8
a=50
a+=5
a-=10
print("Final ans",a)
#9
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#10
a=True
b=False
print( a and b)
print(a or b)
print(not a)
#11
#Usingthirdvariable
a=10
b=20
c=a
a=b
b=c
print("a:",a,"b:",b)
#Withoutusingthirdvariable
a=20
b=50
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)
#12
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
sum=a+b+c
avg=sum/3
print("Average",avg)
#13
a=10
b=30
c=12
d=3
a1=a+b
a2=a1*c
a3=a2/d
print("Final",a3)
#14
maths=int(input("Enter your maths mark:"))
science=int(input("Enter your science mark:"))
social=int(input("Enter your social mark:"))
tamil=int(input("Enter your tamil mark:"))
english=int(input("Enter your english mark:"))
total=(maths+science+social+tamil+english)
print("Total Marks",total)
avg=total/5
print("Average mark is ",avg)