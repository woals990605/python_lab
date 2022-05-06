# 함수 (클래스 내부에 있는 것이 아닌 것들을 함수)

def add():
    print("더하기")


def minus():
    return 1


add()
n = minus()

print(n)


def multi(n1, n2=3):
    print(f"곱하기{n1}*{n2}")


multi(3, 2)

multi(2)


def my_dict(**data):  # dict 변환 문법
    print(data)
    pass


my_dict(id=1, username="ssar")  # key값 있어야된다.

n1 = 1


def vartest():
    global n1
    n1 = 2


vartest()
print(n1)
