import random 
def result(s) :
    value = random.choice(s)
    return value

a = input().split()
print(result(a))