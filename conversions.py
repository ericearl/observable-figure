#! /usr/bin/env python3

import json
from pandas import read_csv 

df = read_csv('final30.csv')

final = []
for i in range(df.shape[0]):
    td = {}
    td['a'] = int(df['node1'][i])
    td['b'] = int(df['node2'][i])
    td['fc'] = float(df['fc'][i])
    td['cca'] = float(df['cca'][i])
    final.append(td)

print(json.dumps(final, indent=4))

thing = list(set([td['a'] for td in final] + [td['b'] for td in final]))

stuff = [[0 for count in range(len(thing))] for i in range(len(thing))]
for e in final:
    for i, node1 in enumerate(thing):
        if node1 == e['a']:
            break
    for j, node2 in enumerate(thing):
        if node2 == e['b']:
            break
    stuff[i][j] = e['cca']

print('"' + '", "'.join([str(t) for t in thing]) + '"')

for line in stuff:
    print(line,',')

yep = stuff.copy()
for line in yep:
    print(line,',')

stuff = [[0 for count in range(len(thing))] for i in range(len(thing))]
for e in final:
    for i, node1 in enumerate(thing):
        if node1 == e['a']:
            break
    for j, node2 in enumerate(thing):
        if node2 == e['b']:
            break
    stuff[i][j] = e['cca']
    stuff[j][i] = e['cca']

for line in stuff:
    print(line,',')

yep = stuff.copy()
for i, line in enumerate(yep):
    for j, elem in enumerate(line):
        if elem != 0:
            yep[i][j] = 1

for line in yep:
    print(line,',')
