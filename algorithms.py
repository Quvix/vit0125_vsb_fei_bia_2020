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






