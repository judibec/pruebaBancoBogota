import itertools


def challengeOne(s, testList):
    newList = []
    for i in testList:
        flag = True
        tempData = []
        for j in i:
            if int(j) < s:
                tempData.append(j)
            elif int(j) >= s:
                flag = False
        if flag:
            newList.append(i)
        else:
            for k in tempData:
                newList.append(k)

    newList = newList[::-1]
    return newList


def challengeTwo(s, testList):
    newList = []
    # sabiendo que el maximo numero S es 9 el valor maximo que puede entrar en la lista es 81
    counter = [0] * 82
    for i in range(len(testList)):
        if int(testList[i]) ** 2 < s ** 2:
            newList += [int(testList[i]) ** 2]
    for n in newList:
        counter[n] += 1

    resList = []
    for i in range(82):
        resList.extend([i] * counter[i])
    return resList


def challengeThree(testList):
    cont = 1
    sums = set()
    for i in range(1, len(testList) + 1):
        for comb in itertools.combinations(testList, i):
            s = sum(comb)
            sums.add(s)
    newList = list(sums)
    for i in range(len(newList)):
        if newList[i] == cont:
            cont += 1
        else:
            break
    return cont

