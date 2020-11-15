import random
import math
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

def generateCities(n, min, max):
    return [(random.uniform(min, max), random.uniform(min, max)) for x in range(n)]

def calculateDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

def evaluate(ant):
    sum = 0
    for i in range(len(ant) - 1):
        sum += calculateDistance(ant[i], ant[i + 1])

    return sum

def distance_matrix(cities):
    m = numpy.zeros((len(cities), len(cities)))
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                distance = calculateDistance(cities[i], cities[j])
                m[i][j] = distance
                m[j][i] = distance
            else:
                m[i][j] = 0

    return m

def get_best(cities, ants):
    def transform(x):
        return [cities[y] for y in x]

    best = transform(ants[0])
    for e in ants:
        transformed = transform(e)
        if evaluate(transformed) < evaluate(best):
            best = transformed
    return best

def animate(i, l, points):
    print(i)
    a = list(map(list, zip(*result[i])))
    l.set_data(a[0], a[1])

MIN = 0
MAX = 100
D = 20
G = 100
P = 0.5

result = []
cities = generateCities(D, MIN, MAX)
pheromone_matrix = numpy.full((D, D), 1)

for i in range(G):
    m = distance_matrix(cities)
    inverse_distances = numpy.divide(pheromone_matrix, m, out=numpy.zeros_like(m), where=m != 0)
    ants = []
    for j in range(D):
        visibility_matrix = copy.deepcopy(inverse_distances)
        visibility_matrix[:, j] = 0
        visited_cities = [j]

        for k in range(D - 1):
            sum = 0
            options = []
            for l in range(len(visibility_matrix[visited_cities[-1]])):
                val = visibility_matrix[visited_cities[-1]][l]
                if val > 0:
                    options.append(l)
                    sum += pheromone_matrix[visited_cities[-1]][l] * (val**2)

            probabilities = []
            for l in range(len(visibility_matrix[visited_cities[-1]])):
                val = visibility_matrix[visited_cities[-1]][l]
                if val > 0:
                    probabilities.append(val**2 / sum)

            next = random.choices(options,probabilities)
            visibility_matrix[:, next[0]] = 0
            visited_cities.append(next[0])

        visited_cities.append(visited_cities[0])
        ants.append(visited_cities)

    result.append(get_best(cities, ants))

    pheromone_matrix = pheromone_matrix * (1 - P)
    for j in range(D):
        distance = evaluate([cities[x] for x in ants[j]])
        for k in range(len(ants[j]) - 1):
            pheromone_matrix[ants[j][k], ants[j][k + 1]] += 1 / distance


print([evaluate(x) for x in result])

fig = plt.figure()
ax = plt.axes(xlim=(MIN, MAX), ylim=(MIN, MAX))
l, = plt.plot([], [], '-o')
anim = animation.FuncAnimation(fig, animate, frames=len(result), interval=100, fargs=(l, [result]))
anim.save("aco_tsp_{0}gen.gif".format(G), writer='pillow')








