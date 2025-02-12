# brute force technique
def cantraverse(gas, cost, start):
    n =len(gas)
    remaining =0
    i=start
    started=False
    while i!=start or not started:
        started =True
        remaining += gas[i]-cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True
def gasstation(gas,cost):
    for i in range(len(gas)):
        if cantraverse(gas, cost, i):
            return i
    return -1
# T: O(n^2)
# S: O(1)

# using candidate method
def gasstation(gas,cost):
    remaining=0
    candidate=0
    for i in range(len(gas)):
        remaining+= gas[i]-cost[i]
        if remaining < 0:
            candidate=i+1
            remaining=0
    prevRemaining=sum(gas[:remaining])-sum(cost[:candidate])
    if candidate==len(gas) or remaining+ prevRemaining < 0:
        return -1
# T: O(n)
# S: O(1)