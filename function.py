def greet_user(username):
    print("Hello, " + username.title() + "!")

def cal(x,y):
    x = int(x); y = int(y)
    print("두 수 합 :" , x+y)
    print("두 수 차 :" , x-y)
    print("두 수 곱 :" , x*y)
    print("두 수 몫 :" , x/y)
    print("두 수 나머지 :" , x%y)
    print("두 수 거듭제곱 :" , x**y)
 
uname = input("Input your name : ")
greet_user(uname)

a = input("Number1 : ")
b = input("Number2 : ")
cal(a,b)