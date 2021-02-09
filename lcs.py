
def fitness(short, longo, binary):
    candidate = ""
    for x in range(len(binary)):
        if binary[x] == "1":
            candidate += (short[x])
    #print("Candidate: ", candidate)
    place = 0
    match = 0
    numOfOnes = len(candidate)
    z = 0
    for y in range(numOfOnes):
        z = place
        while z < len(longo):
            if longo[z] == candidate[y]:
                if place <= z:
                    place = z + 1
                    match += 1
                break
            z += 1


    print("longo: ", longo)
    print("Match: ", match)
    fitnessRating = match + (match * numOfOnes) - (numOfOnes - match)
    print("Fitness: ", fitnessRating)
def main():


  print("##########################################")
  fitness("president", "providence", "110011110") #priden
  print("##########################################")
  fitness("president", "providence", "100000101") #pet
  print("##########################################")
  fitness("president", "providence", "001100001") #
  print("##########################################")
  fitness("sourapple", "googleappstore", "010010101") #
  print("##########################################")
  fitness("sourapple", "googleappstore", "111111111") #

if __name__ == '__main__':
  main()
