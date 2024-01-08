def generate_combinations(K, N):
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            print(i, j)

# 입력 받기
K, N = map(int, input().split())

generate_combinations(K, N)