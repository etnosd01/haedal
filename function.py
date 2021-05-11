def catch():
    print("잡았다!")

catch() #함수_호출

# 매개변수 사용하는 함수
def add(num1, num2):
    return num1 + num2
print(add(1,2))

def add_mul(num1, num2):
    return num1 + num2, num1 * num2
print(add_mul(1,2))

def attack(name):
    print(name, "100만 볼트")
    print(name, "전광석화")
    print(name, "번개")

attack("피카츄")
attack("라이츄")
attack("피츄")
