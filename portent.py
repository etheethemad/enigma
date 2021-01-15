import random

adjs = []
subjs = []

with open("data/portent/portent_adjs.txt",'r',errors='ignore') as f:
    adjs = f.read().split('\n')

with open("data/portent/portent_subjs.txt",'r',errors='ignore') as f:
    subjs = f.read().split('\n')

def gen(num=1):
    return [random.choice(adjs) + ' ' + random.choice(subjs) for i in range(num)]
