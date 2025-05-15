#1
def sayhello():
    print("Hello World")
sayhello()

def sayhello(a):
    print(a)
sayhello("Hello Savithri")
#2
def add(a,b):
    print("Sum",a+b)
add(10,20)
#3
def multiply(x,y):
    c=x*y
    print("Multiply",c)
multiply(20,30)
#4
def mul(a,b):
    c=a*b
    print(c)
mul(10,5)
#5
def div(a,b):
    c=a/b
    print("Division",c)
div(20,2)
#6
def factorial(n):
    fact=1
    if n==0 or n==1:
        return 1
    else:
       return n*factorial(n-1)
print("Factorial of 3:",factorial(3))
print("Factorial of 5:",factorial(5))
#7
def sq(a):
    c=a*a
    print("Square",c)
sq(20)