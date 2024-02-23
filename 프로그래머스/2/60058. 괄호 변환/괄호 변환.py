def solution(str):  
    if len(str) == 0 or rightStr(str): # 1
        return str
    u,v= "", "",
    for i in range(2,len(str)+1): # 2  
        if balanceStr(str[:i]) :
            u, v = str[:i], str[i:]
            break;
    
    if rightStr(u) and balanceStr(u): # 3
        return u + solution(v)# 3-1
    else : # 4
        newStr = "(" # 4-1
        newStr += solution(v)# 4-2
        newStr += ')'# 4-3
        u = u[1:-1]#4-4
        u = "".join(['(' if c == ')' else ')' for c in u ]) # 4-4
        newStr += u
        return newStr

def balanceStr(str):
    cnt1, cnt2= 0, 0
    for i in str:
        if i == ')':
            cnt1 += 1
        else:
            cnt2 += 1
    return cnt1 == cnt2
    
def rightStr(str):
    stack = []
    for idx, c in enumerate(str):
        if c == '(':
            stack.append('(')
        else:
            if len(stack) == 0 :return False
            stack.pop()
    return True
    
        