# 유클리드 호제법을 이용한 두 수의 최대공약수를 구하는 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
lst = list(map(int,input().split()))

# 하나의 수를 정해 이와 다른 수들과의 차이를 리스트 dif에 저장한다. 
dif = [i-lst[0] for i in lst if i != lst[0]]
D = dif[0]

# 각 차이들의 최대공약수를 구한다.
for i in range(1,len(dif)):
    D = gcd(D,dif[i])

# 차이의 기준을 임의의 수로 정했기에 음수가 될 수 있음을 고려한다.
print(abs(D))
