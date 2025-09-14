
# read the list from the url

filename = "test.txt"
leftList = []
rightList = []
with open(filename) as f:
    for line in f:
        values = line.strip().split(" ")

        leftList.append(int(values[0]))
        rightList.append(int(values[3]))

    leftList.sort()
    rightList.sort()

    score = 0
    for i in range(len(leftList)):
        score += abs(leftList[i] - rightList[i])

    print(score)




