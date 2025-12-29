numbers = [1,2,3,4]
num = []
for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                num.append(a*1000+b*100+c*10+d)
num.sort()
x = num[::-1]
print(x)