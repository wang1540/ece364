__author__ = 'ee364b09'

from pprint import pprint as pp

x='af aef d e sa f e'
y = x.split()
xx={}
t = 0

for i in y:
    xx[t] = y[t]
    t += 1
pp(xx)


hh = 1


del xx[hh]
del xx[hh + 1]

pp(xx)

mm =[]

for i in xx.keys():
    nn = [i, xx[i]]
    mm += [nn]

print(mm)

for ele in mm:
    if ele[0] >= hh:
        ele[0] = ele[0] - 2
        xx[ele[0]] = ele[1]
print(len(xx.keys()))
del xx[len(xx.keys()) - 1]
del xx[len(xx.keys()) - 2]
print(mm)
pp(xx)

