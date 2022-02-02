
def method1(n: int):
    """This is done using recursion"""
    if n < 1:
        return n
    elif n == 1:
        return 1
    return n * method1(n-1)


if __name__ == '__main__':
    n = int(input('Enter an Integer: '))
    print(method1(n))
