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
            #print(temp)
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
            if gen <= popFitness[cur]: #and population[cur] not in finalPop:
                #print("fitness at cur: ", popFitness[cur], " Random Gen:", gen)
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
    fitnessRating = 3*match + (match * numOfOnes) - (5*(numOfOnes - match))
    #fitnessRating = match + (match * numOfOnes) - (numOfOnes - match)*2
    if numOfOnes > match:
        fitnessRating = math.floor(fitnessRating* .25)
    if fitnessRating <= 0:
        fitnessRating = 1
    if isLcs(short,candidate):
        fitnessRating *= 3
    else:
        fitnessRating = math.floor(fitnessRating * .25)
    return fitnessRating


def ga(pool, k):
    pop = pool
    crossPop = []
    repoPop = []
    n = 1000
    t = 0

    for x in pool:
        rand = random.random() * n
        if rand < (n * 0.97):
            crossPop.append(x)
        else:
            crossPop.append(x)
            repoPop.append(x)
            #print("Reproducing")
    #print("crossPop len", len(crossPop), "len of repoPop", len(repoPop))

    # if len(crossPop)%2 != 0:
    #     t = len(repoPop) -1
    #     crossPop.append(repoPop[t])
    #     repoPop.pop()
    crossPop = crossover(crossPop, k)
    crossPop.extend(repoPop)

    #print("New Pop Len: ",len(crossPop))
    return crossPop


def crossover(pool, k):
    for i in range(0, len(pool), 2):
        point = random.randint(0, 9)

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

        if random.random() * k < 1 / k: #pm = 1/k
        #    print("Mutating")
            pool[i] = mutate(pool[i])
            pool[i+1] = mutate(pool[i+1])

    return pool

def mutate(bin):
    if bin != '':
        word = ""
        li = []
        li[:] = bin
        rand = random.randint(0, len(bin) - 1)
        if bin[rand] == '0':
            li[rand] = '1'
        elif bin[rand] == '1':
            li[rand] = '0'
        word.join(li)

        return word
    return bin

def printList(li):
    for i in li:
        print(i)

# filter out valid sub sequences
def filterPopulation(pool, short, longo):
    result = []
    decodedList = []
    filteredResult = []
    # remove duplicates
    [result.append(x) for x in pool]# if x not in result]
    # decode the binary strings in the list to "words"
    for x in result:
        decodedList.append(parseBinary(short, x))
    # grab the only items that are sub sequences
    [filteredResult.append(x) for x in decodedList]# if isLcs(x, longo)]

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
    populationSize = 120
    maxGens = 200

    # different trials commented out
    # short = "president"
    # longo = "providence"

    # short = "tcaatacgtaagggtactcgtagaagaaacacacgcggtagcgtctgagattggagtggggttgggagat" #70 chars
    # longo = "tttgtaagggagggtcgagaaatataaggcaaatagtagctggccataatcagagccataaattggtaaggaaagattttttt" #80 chars

    # short = "helpmepleasehelpyoung"
    # longo = "Help!IneedsomebodyHelp!NotjustanybodyHelp!YouknowIneedsomeoneHelp!(When)WhenIwasyounger(WhenIwasyoung)somuchyoungerthantodayIneverneedIneverneededanybody'shelpinanyway"

    # short = "thebigbluestorewasfilledwithbees"
    # longo = "somebodyoncetoldmetheworldwasgonnarollmeiaintthesharpesttoolintheshed"

    # short = "myStationaryfig"
    # longo = "blastatgppppmmmmioneryfunimag"

    short = "thebluelagoon"
    longo = "theodoreisgreenandbluebutnotmaroon"

    short = short.lower()
    longo = longo.lower()
    seq = ""
    generation = 0
    found = 0
    identical = 0
    k = len(short)

    population = makeInitialPop(short, populationSize)
    #print(len(population), "---Pop size")
    finalPop = roulette(short, longo, population,populationSize-10)
    # for x in finalPop:
    #     print(x,"\n")
    ##################################
    while True:
        candidates = []
        finalPop = roulette(short, longo,finalPop , (populationSize - 10))
        finalPop = ga(finalPop, k)
        candidates = filterPopulation(finalPop, short, longo)
        #print(" ----- size of pop:", len(candidates))
        ### uncomment to view each generations possible lcs
        #printList(candidates)
        identical += 1

        for x in candidates:
            if len(x) > len(seq):
                seq = x
                identical = 0
        if identical == 0:
            found = generation
        generation += 1


        # if the same lcs stays for more than 10 generations, end the program
        if generation > maxGens: #identical > 10:
            print("**************************")
            print(f"\nfittest: {seq}")
            print(f"found in G: {found}")
            print(f"current G: {generation}")
            print("**************************")
            break
##########################333
        ## uncomment for manual control
        # action = input("\npress enter to continue\nor\n'q' to quit\n")
        # if (action == 'q'):
        #     break


if __name__ == '__main__':
  main()
