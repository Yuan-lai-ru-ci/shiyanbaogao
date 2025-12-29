footballSet = {'xiaoming','xiaowang','xiaoliu','xiaoma'}
basketballSet = {'xiaoli','xiaobizaizi','xiaoaikun','xiaoliu'}
num = len(footballSet.union(basketballSet))
print('共' + str(num) + '人')
com = footballSet.intersection(basketballSet)
print('共' + str(len(com)) + '人加入了足球和篮球')
print('共' + str(num-len(com)) + '人只加入了其中一个')
