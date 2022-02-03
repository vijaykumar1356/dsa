def second_decorator(func):
    def inner(a, b):
        print("passed zero division test")
        return func(a, b)
    return inner


def check_for_zero_division(func):
    def inner(a, b):
        if b == 0:
            return('b can not be zero(Zero Division Error)')
        return func(a, b)
    return inner


@check_for_zero_division
@second_decorator
def divide_method1(a, b):
    return a/b


if __name__ == "__main__":
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(divide_method1(a, b))
