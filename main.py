def checker(per):
    i=len(per)-1
    for j in range(i):
        if( i-j == abs(per[i]-per[j])):
            return False
    return True

def solver(per, n, ans=False):
    global x
    if(len(per)==n):
        return per
     
    for i in range(n):
        if i not in per:
            per.append(i)
            
            if(checker(per)):
                ans=solver(per,n)
                if(ans):
                    return ans

            per.pop()
    return ans

print("Enter n: ")
k=int(input())
print(solver([],k))
