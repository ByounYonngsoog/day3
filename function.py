def hello(uname="Victoria", uage='10'):
    print("Hello, " + uname)
    print(uage + "years old")

def cal(x,y):
    x = int(x); y = int(y)
    print("두 수 합 :" , x+y)
    print("두 수 차 :" , x-y)
    print("두 수 곱 :" , x*y)
    print("두 수 몫 :" , x/y)
    print("두 수 나머지 :" , x%y)
    print("두 수 거듭제곱 :" , x**y)
 
uname = input("Input your name : ")
uage = input("Input your age : ")

# 일반적인 함수 호출
hello(uname, uage)
# 매개변수가 하나일 경우는 함수에서 age=10으로 처리될수 있음
hello(uname)
# 매개변수가 없는 경우는 초기값을 설정해준대로 출력됨.
hello()
# 매개변수 순서가 바뀔 경우
hello(uage, uname)
hello(uage='10', uname='Nick')

a = input("Number1 : ")
b = input("Number2 : ")
cal(a,b)