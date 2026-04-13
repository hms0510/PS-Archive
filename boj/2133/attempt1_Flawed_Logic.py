N = int(input())
lst = [0,0,3,0,8]
for i in range(5,31):
    if i % 2 == 1:
        lst.append(0)
        continue
    lst.append((lst[i-2]+3) + (lst[i-4]+2)) # dp[i-2]로부터 발생하는 패턴 + 예외 패턴
    
print(lst[N])
