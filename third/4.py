aList = [9,9,8.5,10,7,8,8,9,8]
bList = sorted(aList)
cList = bList[1:10]
n = 0
for i in range(8):
    n = aList[i+1] + n
print(n/8)