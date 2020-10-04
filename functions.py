import numpy as np
import math


def sphere(params):
    sum = 0
    for p in params:
        sum += p ** 2

    return sum


def rastrigin(params):
    sum = 10 * len(params)
    for p in params:
        sum += p ** 2 - 10 * np.cos(2 * math.pi * p)

    return sum


def griewank(params):
    def sum():
        result = 0
        for p in params:
            result += p ** 2 / 4000

        return result

    def prod():
        result = 1
        for i, p in enumerate(params, start=1):
            result *= np.cos(p / math.cos(i))
        return result

    return sum() - prod() + 1


def michalewicz(params, m=10):
    sum = 0
    for i, p in enumerate(params, start=1):
        sum += np.sin(p) * np.sin((i * p ** 2) / math.pi) ** (2 * m)

    return -sum


def zakharov(params):
    def sum1():
        sum = 0
        for p in params:
            sum += p ** 2
        return sum

    def sum2():
        sum = 0
        for i, p in enumerate(params, start=1):
            sum += 0.5 * i * p

        return sum

    tmp = sum2()

    return sum1() + tmp ** 2 + tmp ** 4


def schwefel(params):
    sum = 0
    for p in params:
        sum += p * np.sin(np.sqrt(np.abs(p)))

    return 418.9829 * len(params) - sum


def rosenbrock(params):
    sum = 0
    for i, p in enumerate(params[:-1]):
        sum += 100 * (params[i + 1] - p ** 2) ** 2 + (p - 1) ** 2

    return sum


def ackley(params, a=20, b=0.2, c=2 * math.pi):
    def exp1():
        sum = 0
        for p in params:
            sum += p ** 2

        return np.exp((-b) * np.sqrt((1 / len(params)) * sum))

    def exp2():
        sum = 0
        for p in params:
            sum += np.cos(c * p)

        return np.exp((1 / len(params)) * sum)

    return (-a) * exp1() - exp2() + a + math.exp(1)


def levy(params):
    def w(p):
        return 1 + ((p - 1) / 4)

    sum = 0
    for i, p in enumerate(params, start=1):
        sum += (w(p) - 1)**2 * (1 + 10 * np.sin(math.pi * w(p) + 1)**2)

    return math.sin(math.pi * w(params[0]))**2 + sum + (w(params[-1]) - 1)**2 * (1 + np.sin(2 * math.pi * w(params[-1]))**2)
