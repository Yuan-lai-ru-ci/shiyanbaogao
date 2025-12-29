import math
a,b,c = input('请输入三边:').split()
p = (float(a)+float(b)+float(c))/2
if float(a) > 0 and float(b) > 0 and float(c) > 0:    
    if float(a)+float(b)>float(c) and float(a)+float(c)>float(b) and float(b)+float(c)>float(a):
        print('这三边可以构成三角形')
        print('三角形的周长为:',float(a)+float(b)+float(c))
        print('三角形的面积为:',math.sqrt(p*(p-float(a))*(p-float(b))*(p-float(c))))
    else:
        print('这三边不能构成三角形')