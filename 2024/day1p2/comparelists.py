from collections import defaultdict
# read the list from the url

filename = "test.txt"
leftList = []
d = defaultdict(int)
with open(filename) as f:
    for line in f:
        values = line.strip().split(" ")

        
        leftList.append(int(values[0]))
        rightValue = int(values[3])
        d[rightValue] += 1

    score = 0
    for i in range(len(leftList)):
        score += abs(leftList[i] * d[leftList[i]])

    print(score)




