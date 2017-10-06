oneToTwenty = list(range(1,21))
for value in oneToTwenty:
    print(value)


oneToMil = list(range(1,1000001))
for value in oneToMil:
    print(value)

print(min(oneToMil))
print(max(oneToMil))
print(sum(oneToMil))

print(range(1, 20, 2))
thirtyList = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for value in thirtyList:
    print(value)

cubesListOne = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
for value in cubesListOne:
    print(value)

cubesList = []
for value in range(1,11):
    cubesList.append(value**3)
for value in cubesList:
    print(value)
