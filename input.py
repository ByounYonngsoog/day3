# name = input("Please enter your name?")
# print("Hello, " + name + "!")

print("사칙연산 >")
num1 = int(input("First number : "))
num2 = int(input("Second number : "))
print("합 : ", num1+num2)
print("차 : ", num1-num2)
print("곱 : ", num1*num2)
print("몫 : ", num1/num2)
print("나머지 : ", num1%num2)

if (num1%2 ==0):
    print(num1, "is Even.")
else:
    print(num1, "is Odd.")


