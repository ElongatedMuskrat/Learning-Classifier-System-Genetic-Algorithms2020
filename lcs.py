from datetime import datetime

import math
import random


def makeInitialPop(short, populationSize):
    tempper = pow(2,len(short))
    if populationSize > tempper:
        print("It is impossible to create ", populationSize, " unique binary variations of a word that is ", len(short), "characters long.")
        return
    population = []
    temp = ""
    while len(population) < populationSize:
    #for x in range(populationSize):
        temp = ""
        for index in range(len(short)):
            gen = random.randint(0,1)
            temp += str(gen)
        if temp not in population:
            population.append(temp)
            print(temp)
        #else:

            #print("Woah no posers brah. You gotta be unique to join our crew!")
    return population


def roulette(short, longo, population, size):
    popFitness = []
    finalPop = []
    totalFitness = 0
    for speci in population:
        specFit = fitness(short, longo, speci)
        popFitness.append(specFit + totalFitness)
        totalFitness += specFit
    
        #not finished
    while len(finalPop) < size:
        gen = random.randint(0,totalFitness)
        found = False
        cur = 0
        while found == False:
            #print(cur)

            if cur >= size:
                break
            if popFitness[cur] <= gen and population[cur] not in finalPop:
                finalPop.append(population[cur])
                found = True
            else:
                cur += 1


    return finalPop


def fitness(short, longo, binary):
    candidate = ""
    yam = 0
    for x in range(len(binary)):
        if binary[x] == "1":
            candidate += (short[x])

    place = 0
    match = 0
    matchNotFound = 0
    numOfOnes = len(candidate)
    #print("num of ones",numOfOnes)
    z = 0
    for yam in range(numOfOnes):
        z = place
        if matchNotFound == 0:
            while z < len(longo):
                if longo[z] == candidate[yam]:
                    if place <= z:
                        place = z + 1
                        match += 1
                    break
                elif z == len(longo) - 1 and longo[z] != candidate[yam]:
                    matchNotFound = 1
                    break
                z += 1
        else:
            break


    #print("Match: ", match)
    fitnessRating = match + (match * numOfOnes) - ((numOfOnes - match))
    if match == numOfOnes:
        fitnessRating *= 2
    if fitnessRating <= 0:
        fitnessRating = 1


    print("Candidate: ", candidate,"Fitness: ", fitnessRating)
    print("###################################################")    
    return fitnessRating


def ga(pool):
    pop = pool

    n = 1000
    rand = random.random() * n
    if rand < (n * 0.95):
        return crossover(pop)
    else:
        reproduce()
        return pool


def crossover(pool):
    for i in range(0, len(pool), 2):
        point = random.randint(0, 9)
        # print(point)

        parent1 = pool[i]
        parent2 = pool[i+1]

        sub1 = parent1[point:]
        parent1 = parent1[:point]
        sub2 = parent2[point:]
        parent2 = parent2[:point]
        # print(f"{parent1} : {sub1}")
        # print(f"{parent2} : {sub2}")
        parent1 += sub2
        parent2 += sub1

        pool[i] = parent1
        pool[i+1] = parent2

    return pool


def reproduce():
    return


def mutate():
    return


def printList(li):
    for i in li:
        print(i)


def filterPopulation(pool, short, longo):
    result = []
    decodedList = []
    filteredResult = []
    # remove duplicates
    [result.append(x) for x in pool if x not in result]
    # decode the binary strings in the list to "words"
    for x in result:
        decodedList.append(parseBinary(short, x))
    # grab the items that are sub sequences
    [filteredResult.append(x) for x in decodedList if isLcs(x, longo)]

    return filteredResult


# decode the binary string based on the origin word
def parseBinary(origin, binary):
    word = ""
    for i, c in enumerate(binary):
        if c == '1':
            word += origin[i]
    return word


# Determine whether or not str1 is a subsequence of str2
def isLcs(str1, str2):
    it = iter(str2)
    return all(c in it for c in str1)
    

def main():
    populationSize = 100
    short = "president"
    longo = "providence"
    # tester = "prsident"
    # fitness("president", "providence", "110011110") #priden
    # print("##########################################")
    # fitness("president", "providence", "110011111") #prident
    # print("##########################################")
    # testBin = "110111111"
    #fitness(short, longo, testBin)
    # fitness(short, longo, testBin)
    population = makeInitialPop(short, populationSize)
    print(len(population), "---Pop size")
    finalPop = roulette(short, longo, population,populationSize-10)
    print(len(finalPop), "---Final Pop size")
    # for x in finalPop:
    #     print(x)
    
    # for i, binary in enumerate(finalPop):
    #     parseBinary('president', binary)
        
    print('=============================')
    while True:
        candidates = []
        population = ga(population)
        print('=============================')
        candidates = filterPopulation(population, short, longo)
        printList(candidates)
        
        action = input("\npress enter to continue\nor\n'q' to quit\n")
        if (action == 'q'):
            break
    # print("##########################################")

    # fitness("president", "providence", "100000101") #pet
    # print("##########################################")
    # fitness("president", "providence", "001100001") #
    # print("##########################################")
    # fitness("sourapple", "googleappstore", "010010101") #
    # print("##########################################")
    # fitness("sourapple", "googleappstore", "111111111") #

if __name__ == '__main__':
  main()
