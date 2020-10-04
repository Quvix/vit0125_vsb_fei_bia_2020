import random
import numpy

def blind_search(d, g_max, np, min, max, function):
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

def hill_climbing(d, g_max, np, min, max, function, sigma = 0.1):
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




