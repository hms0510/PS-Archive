MOD = 1000000000

N = int(input())
# dp 테이블 생성
dp = [[0 for _ in range(10)] for _ in range(N+1)]

# 0으로 시작하는 경우 제외하고 초기화
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        # 뒷자리가 0으로 끝나는 경우 1 뒤에 0이 붙는 경우만 존재
        if j == 0:
            dp[i][j] = dp[i-1][1] % MOD
        # 뒷자리가 9으로 끝나는 경우 8 뒤에 0이 붙는 경우만 존재
        elif j == 9:
            dp[i][j] = dp[i-1][8] % MOD
        # 위의 두 경우가 아니라면 뒤에 1 더 작은 수, 1 더 큰 수 모두 붙을 수 있음
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD
            
# 최종 출력에도 모듈러스 연산하기
print(sum(dp[N]) % MOD)
