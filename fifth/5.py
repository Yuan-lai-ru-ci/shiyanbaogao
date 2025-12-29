num = [1,2,3,4,5,6,7,8,9,0]
number = []
for a in num:
    for b in num:
        for c in num:
            if (b + c) % 10 == a:
                if 1000> a*100+b*10+c > 100:
                    number.append(a*100+b*10+c)
            else:
                continue
print(number)