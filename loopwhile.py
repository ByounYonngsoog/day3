message = ''
# while message != 'quit':
#     message = input("typing you message: ")
#     print(">"  + message)

# while True:
#     message = input("typing you message: ")
#     print(">"  + message)
#     if message == 'quit':
#         break 

# number = 1
# while number < 10:
#     number = number + 1
#     if (number%2 == 0):
#         continue
#     print(number)

number = 0
num = int(input("Input number : "))
while number < num:
    number = number + 1
    if (number%2 != 0):
        continue
    print(number,end=' ')
