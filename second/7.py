m,t0,t1 = input('请输入水的质量,初始温度,最终温度,用空格隔开：').split()
Q = float(m)*(float(t1)-float(t0))*4184
print(Q,'J')