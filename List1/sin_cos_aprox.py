import math
import random

def sinApprox(k : int, angle : int) -> float:
    sinSeries = [(-1) ** i * (angle ** (2 * i + 1)) / math.factorial(2 * i + 1) for i in range(k)]
    return sum(sinSeries)

def cosApprox(k : int, angle : int) -> float:
    cosSeries = [(-1) ** i * (angle ** (2 * i)) / math.factorial(2 * i) for i in range(k)]
    return sum(cosSeries)

def maxList(randList : list) -> int:
    return max(randList)

def minList(randList : list) -> int:
    return min(randList)

def averageList(randList: list) -> float:
    return sum(randList) / len(randList)


"""def manualMaxList(randList: list) -> int:
    max = randList[0]
    for i in range(len(randList)):
        if randList[i] > max:
            max = randList[i]

    return max

def manualMinList(randList: list) -> int:
    min = randList[0]
    for i in range(len(randList)):
        if randList[i] < min:
            min = randList[i]

    return min

def manualAverage(randList: list) -> float:
    listSum = 0
    for i in range(len(randList)):
        listSum = listSum + randList[i]

    return listSum / len(randList)
"""

if __name__ == "__main__":
    print("Enter k")
    k = int(input())
    print("Enter angle")
    requestAngle = math.radians(int(input()))
    print("sin = ",  sinApprox(k, requestAngle))
    print("cos = ", cosApprox(k, requestAngle))

    print("\n\nRandom k values")
    for i in range(10):
        print("\nRandomization number ", i+1, "\nsin = ", sinApprox(random.randint(1, 10), requestAngle))
        print("Math sinus", math.sin(requestAngle))
        print("cos = ", cosApprox(random.randint(1,10), requestAngle))
        print("Math cosinus", math.cos(requestAngle))

    newRandList = [random.randint(1, 100) for i in range(10)]
    print("\nRandom list generated")
    print(newRandList)
    print("\nMax in list =  ", maxList(newRandList))
    print("Min in list =  ", minList(newRandList))
    print("Average of list =  ", averageList(newRandList))