class Cal():
    def __init__(self, value):
        self.value = value

    def result(self):
        print(self.value)

    def add(self, input_value):
        self.value += input_value

    def sub(self, input_value):
        self.value -= input_value

    def mul(self, input_value):
        self.value *= input_value  

# 모든경우의 예외처리
    def div(self, input_value):
        try:
            self.value /= "v"
        except:
            print("오류가 발생했습니다.!")
        finally:
            print("실행완료!")

# div 함수 그대로 살리면서 0으로 나누는 것을 처리하고자 할 때
# 상속과 오버라이드 이용해서 해결하는 방법

class SafeCal(Cal):
    def __init__(self, value):
        self.value = value
    def div(self, input_value):
        if (input_value == 0):
            self.value = 0
        else:
            self.value /= input.value


cal1 = Cal(0)
cal1.add(10)
cal1.result()
cal1.div(0)
cal1.result()

# cal1.result()
# cal1.sub(2)
# cal1.result()
# cal1.mul(3)
# cal1.result()
# cal1.div(0)
# cal1.result()

# cal2 = SafeCal(0)
# cal1.add(10)
# cal1.result()
# cal2.div(0)
# cal2.result()
