#1
for i in range(1,11):
     print(i)
#2
for i in range(1,20):
     if i%2==0:
          print("even",i)
#3
for i in range(1,20):
     if i%2!=0:
          print("odd",i)
#4
n=5
num=1
for i in range(1,n+1):
    num*=i
print("Factorial of 5",num)
#5
count=0
for i in range(1,101):
    count+=i
    print(count)
#6
a=[10,20,30,40,50,30]
total=0
for i in a:
    total+=i
    avg=total/len(a)
print("Average",avg)     
#7
#Square
n=5
for i in range(n):
    row=""
    for j in range(n):
        row+="*"
    print(row) 
#Rectangle
n=5
p=10
for i in range(n):
    row=""
    for j in range(p):
        row+="*"
    print(row)  
#8   
for i in range(1,6):
    print(i)    
#9
for i in range(1,11):
    print("Natural numbers",i)  
#10
a=[1,2,3,1]
for i in range(len(a)):
    if a[i]==a[i-1]:
        print("true")
        break
    else:
        print("false")
#11
a=[5,8,15,27,35,50,80,34,12]
for i in a:
 if i%5==0:
       print(i)
#12
a1=input()
if a1 in ("a","e","i","o","u"):
   print("vowel")
else:
   print("consonant")
#13
odd=[]
even=[]
for i in range(10,56):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(len(even),"even")
print(len(odd),"odd")
#14
for i in range(1,26):
    if i%5==0:
        print(i,"Divisible by 5")
    else:
        print(i,"Not divisible by 5")
#15
num=[3,5,7,0,1]
factorial=[]
for i in num:
    fact=1
    for j in range(1,i+1):
        fact*=j
    factorial.append(fact)
print(factorial)
#16
a=int(input())
b=int(input())
c=a+b
d=a*b
if (d>500):
  print(c)
else:
  print(d)
#17
b=int(input("Enter the number2:"))
c=int(input("enter the number3:"))
if (b>c):
    print("b is greater")
else:
    print("C is greater")
#18
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("enter the number3:"))
if (a>b and a>c):
    print("A is greatest of all")
elif (b>a and b>c):
    print("B is greatest of all")
else:
    print("c is greatest of all")
#19
a=[23,4,-6,23,-9,21,3,-45,-8]
pos=[]
neg=[]
for i in a:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)