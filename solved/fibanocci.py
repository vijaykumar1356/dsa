def method1():
    """This is done using generator"""
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = a + c
        yield c


if __name__ == '__main__':
    f = method1()
    for i in range(10):
        print(next(f))
