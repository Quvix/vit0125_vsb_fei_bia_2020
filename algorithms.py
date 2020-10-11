import random
import numpy

def blind_search(d, min, max, function, g_max, np):
    def generate():
        return [random.uniform(min, max) for x in range(d)]

    args = list()
    fitness = None

    #fitness = (result or [None])[-1]
    for i in range(g_max):
        arg_best = None
        for j in range(np):
            arg = generate()
            val = function(arg)

            if fitness is None or val < fitness:
                fitness = val
                arg_best = arg

        if arg_best is not None:
            args.append(arg_best)
        else:
            args.append(args[-1])

    return args

def hill_climbing(d, min, max, function, g_max, np, sigma = 0.1):
    def generate_neighbors(x):
        neighbors = []

        normals = []

        for i in range(len(x)):
            normals.append(numpy.random.normal(x[i], sigma, np))

        for i in range(np):
            p = []
            for j in range(len(x)):
                p.append(normals[j][i])

            neighbors.append(p)
        return neighbors


    result = list()

    x0 = [random.uniform(min, max) for x in range(d)]
    fitness = function(x0)

    for i in range(g_max):
        for nb in generate_neighbors(x0):
            val = function(nb)

            if val < fitness:
                x0 = nb
                fitness = val

        result.append(x0)

    return result


def simulated_annealing(d, min, max, function, t_zero = 100, t_min = 0.5, alpha = 0.95, sigma = 0.1):
    def get_neighbor(i):
        return [numpy.random.normal(e, sigma) for e in x]

    t = t_zero
    result = list()
    x = [random.uniform(min, max) for x in range(d)]
    result.append(x)

    while t > t_min:
        x_1 = get_neighbor(x)

        check = True
        for e in x_1:
            if e < min or e > max:
                check = False
                break

        if not check:
            continue

        if function(x_1) < function(x):
            x = x_1
        else:
            r = random.uniform(0, 1)
            if r < numpy.e ** -((function(x_1) - function(x)) / t):
                x = x_1

        t = t * alpha
        result.append(x)

    return result

