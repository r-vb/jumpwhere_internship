# checking method -using stack (checking, not generating)
def validparentheses(combination):
    stack =[]
    for paran in combination:
        if paran == '(':
            stack.append(paran)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
# checking method - without using stack just tracking diff
def validparentheses(combination):
    diff = 0
    for paran in combination:
        if paran == '(':
            diff +=1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0


# generating using backtracking
def generate(n):
    def rec(n,diff,comb,combs):
        if diff < 0:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n-1,diff+1,comb,combs)
            comb.pop()
            comb.append(')')
            rec(n-1,diff-1,comb,combs)
            comb.pop()
    combs = []
    rec(2*n,0, [], combs)
    return combs
# T(n) = 2^k * T(n-k)+(2^k -1) {substitution method}
# T(n) = O(n2^n)
# S: call stack size [n+1] + combs arr size [n*2^n] = O(n2^n) {upperbound}