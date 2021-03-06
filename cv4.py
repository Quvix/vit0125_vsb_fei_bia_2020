import random
import math
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generateCities(n, min, max):
    return [(random.uniform(min, max), random.uniform(min, max)) for x in range(n)]

def calculateDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

def generateIndividual(cities):
    lst = copy.deepcopy(cities)
    random.shuffle(lst)
    return lst

def generatePopulation(cities, np):
    return [generateIndividual(cities) for x in range(np)]

def evaluate(individual):
    sum = 0
    for i in range(len(individual) - 1):
        sum += calculateDistance(individual[i], individual[i + 1])
    sum += calculateDistance(individual[len(individual) - 1], individual[0])

    return sum

def mutate(individual):
    if random.random() < 0.5:
        idx = range(len(individual))
        i1, i2 = random.sample(idx, 2)
        individual[i1], individual[i2] = individual[i2], individual[i1]
    return individual

def getRandomParent(population, exclude):
    return population[random.choice([e for e in range(len(population)) if e != exclude])]

def offspring(parent_A, parent_B):
    line = random.randint(0, len(parent_A) - 1)
    slice = parent_A[:line]
    return slice + [x for x in parent_B if x not in slice]


def animate(i, l, points):
    print(i)
    a = list(map(list, zip(*result[i])))
    l.set_data(a[0], a[1])

def getBest(population):
    best = population[0]
    for e in population:
        if evaluate(e) < evaluate(best):
            best = e
    return best



MIN = 0
MAX = 100
NP = 100
G = 10
D = 20

result = []
cities = generateCities(D, MIN, MAX)
population = generatePopulation(cities, NP)

for i in range(G):
    new_population = copy.deepcopy(population)
    for j in range(NP):
        parent_A = population[j]
        parent_B = getRandomParent(population, j)
        offspring_AB = mutate(offspring(parent_A, parent_B))

        if evaluate(offspring_AB) < evaluate(parent_A):
            new_population[j] = offspring_AB

    population = new_population
    result.append(getBest(population))


fig = plt.figure()
ax = plt.axes(xlim=(MIN, MAX), ylim=(MIN, MAX))
l, = plt.plot([], [], '-o')
anim = animation.FuncAnimation(fig, animate, frames=len(result), interval=100, fargs=(l, [result]))
anim.save("ga_tsp_{0}gen.gif".format(len(result)), writer='pillow')





