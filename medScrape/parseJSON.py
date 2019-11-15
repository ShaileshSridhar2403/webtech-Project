#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:16:27 2019

@author: shailesh
"""

import json
import random
import math

dList = json.loads(open('/home/shailesh/Documents/sem7/WT/project/medScrape/medList.json').read())

communityNames = list(set([d['communityName'] for d in dList]))
communityNames.sort()

l = []
for i in range(len(communityNames)):
	d = {}
	d['communityName']=communityNames[i]
	d['communityID'] = i+1
	l.append(d)

with open('communityName_communityID.json', 'w') as outfile:
    json.dump(l, outfile)





sampleDict = set([])
for i in range(100000):
	sampleDict.add((random.randint(1,101),random.randint(1,1026)))

sampleDict = [list(l) for l in sampleDict]

for l in sampleDict:
	l.append(math.floor((random.random()*3) + 1))
	
ratingList = []
for i in sampleDict:
	d={}
	d['UserID'] = l[0]
	d['communityID'] = l[1]
	d['rating'] = l[2]
	ratingList.append(d)


with open('ratingData.json', 'w') as outfile:
    json.dump(ratingList, outfile)


stringList = []
for char in 'abcdefghijklmnopqrstuvwxyz':
	for i in range(5):
		uString = char+str(i)
		stringList.append(uString)


UList = []
for i in range(1,101):
	d = {}
	d['UserID'] = i
	d['Username'] = stringList[i]
	UList.append(d)

UList[0]['Username'] = 'Krupesha D'


with open('userData.json', 'w') as outfile:
    json.dump(UList, outfile)
