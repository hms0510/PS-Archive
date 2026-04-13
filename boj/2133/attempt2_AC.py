N = int(input())
dp = [1,0,3,0] # dp 테이블 생성
for i in range(4,N+1):
    if i % 2 == 1:
        dp.append(0)
        continue
    cnt = dp[i-2]*3 # 고정적 패턴
    for j in range(4,i+1,2): # 짝수 예외 패턴 세기
        cnt += dp[i-j]*2
    dp.append(cnt)
   
print(dp[N])
