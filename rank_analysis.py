import operator
import numpy as np
from matplotlib import pyplot as plt

def get_rank(filerank):
	rank = []
	objs = {}
	with open(filerank, 'r') as f:
		for line in f:
			line = line.split(',')
			item = (line[1],float(line[2]))
			rank.append(item)
			objs[line[1]] = item
	return (rank,objs)

def get_trust(filename):
	trust = []
	with open(filename, 'r') as f:
		for line in f:
			trust.append(line.split()[0])
	return trust

def percentage_split(seq, percentages):
	print(sum(percentages))
	assert abs(sum(percentages) - 1.0) < 0.000001
	prv = 0
	size = len(seq)
	cum_percentage = 0
	for p in percentages:
		cum_percentage += p
		nxt = int(cum_percentage * size)
		yield seq[prv:nxt]
		prv = nxt

def get_bins_analysis(bins1,bins2):
	for index, b1 in enumerate(bins1):
		b2 = bins2[index]
		print('Bin ' + str(index+1) + ': ' + str((len(set(b1) & set(b2)))/len(merged)))
# ************************************************************


poe_rank, poe = get_rank('files/poe_rank.txt')
poe_trust = get_trust('files/poe_confiaveis.txt')
csgo_rank, csgo = get_rank('files/csgo_rank.txt')
csgo_trust = get_trust('files/csgo_confiaveis.txt')

dict1 = {}
dict2 = {}
for t in poe_trust: dict1[t] = poe_rank.index(poe[t])
for t in csgo_trust: dict2[t] = csgo_rank.index(csgo[t])

sorted1 = sorted(dict1.items(), key=operator.itemgetter(1))
sorted2 = sorted(dict2.items(), key=operator.itemgetter(1))

print("where are the poe trust?")
for i in sorted1: print(i)
print("where are the csgo trust?")
for i in sorted2: print(i)

k1 = list(poe.keys())
merged = []
for k in k1:
	if(k in csgo.keys()): merged.append(k)

print('users intersec: ', len(merged))
dist = []

# for u in merged:
# 	p1 = (poe_rank.index(poe[u]))/float(len(csgo))
# 	p2 = (csgo_rank.index(csgo[u]))/float(len(csgo))
# 	dist.append(abs(p1-p2))

# print(np.mean(dist))
# print(np.std(dist))

bins1 = list(percentage_split([x[0] for x in poe_rank],[0.4,0.3,0.2,0.1]))
bins2 = list(percentage_split([x[0] for x in csgo_rank],[0.4,0.3,0.2,0.1]))
get_bins_analysis(bins1,bins2)
