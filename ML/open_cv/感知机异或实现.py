'''
    感知机异或实现, 相同返回 0 不同返回 1
'''


def XOR(x1, x2):
    w1 = w4 = w5 = w6 = 1
    w2 = w3 = -1

    p1 = (x1 * w1) + (x2 * w3)
    p2 = (x1 * w2) + (x2 * w4)

    result = (1 if p1 >= 0.5 else 0) * w5 + (1 if p2 >= 0.5 else 0) * w6

    return 1 if result >= 0.5 else 0


if __name__ == "__main__":
    a = XOR(1, 1)
    print(a)
    a = XOR(1, 0)
    print(a)
    a = XOR(0, 1)
    print(a)
    a = XOR(0, 0)
    print(a)
