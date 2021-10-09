import random
def d6(n=1):
    results = []
    result = 0
    for i in range(1,n):
        result = random.randint(1,6)
        results.append(result)
    return results

def dStar(d=2, n=1):
    results = []
    result = 0
    for i in range(1, n+1):
        result = random.randint(1, d)
        results.append(result)
    return results

def dStarMod(d=2, n=1):
    results = []
    result = 0
    for i in range(1, n+1):
        result = random.randint(1, d)+1
        results.append(result)
    return results


def dAverage(arr):
    sum = 0
    for i in arr:
        sum += i
    average = sum/len(arr)
    return average

# test = dStar(20,200)
# print(test)
# expect = dAverage(test)
# print(expect)