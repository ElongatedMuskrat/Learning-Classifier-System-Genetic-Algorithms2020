import math
import random

def makeInitialPop(short, populationSize):
    population = []
    temp = ""
    for x in range(populationSize):
        temp = ""
        for index in range(len(short)):
            gen = random.randint(0,1)
            temp += str(gen)
        if temp not in population:
            population.append(temp)
            print(temp)
        else:
            print("Woah no posers brah. You gotta be unique to join our crew!")
    return population

def roulette(short, longo, population):
    popFitness = []
    totalFitness = 0
    for speci in population:
        specFit = fitness(short, longo, speci)
        popFitness.append(specFit)
        totalFitness += specFit
        #not finished

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


    print("Match: ", match)
    fitnessRating = match + (match * numOfOnes) - ((numOfOnes - match))
    if match == numOfOnes:
        fitnessRating *= 2
    if fitnessRating <= 0:
        fitnessRating = 1
    print("Candidate: ", candidate,"Fitness: ", fitnessRating)
    print("###################################################")
def main():
    populationSize = 500
    short = "president"
    longo = "providence"
    # tester = "prsident"
    # fitness("president", "providence", "110011110") #priden
    # print("##########################################")
    # fitness("president", "providence", "110011111") #prident
    # print("##########################################")
    # testBin = "110111111"
    #fitness(short, longo, testBin)
    # population = makeInitialPop(short, populationSize)
    # for x in population:
    #    fitness(short, longo, x)

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
