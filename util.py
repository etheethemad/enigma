import random, re

def roll(num, sides):
    return [random.randint(1,sides) for i in range(num)]

def isdigit(x):
    x = re.sub("^-", "", x) 
    return str.isdigit(x)
