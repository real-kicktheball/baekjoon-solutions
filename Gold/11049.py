import sys

def solve():
    # 입력을 빠르게 받기 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input:
        return
    
    N = int(input[0])
    matrix = []
    idx = 1
    for _ in range(N):
        matrix.append((int(input[idx]), int(input[idx+1])))
        idx += 2

    # DP 테이블 초기화
    dp = [[0] * N for _ in range(N)]

    # d: 구간의 길이 (1부터 N-1까지)
    for d in range(1, N):
        # i: 시작 지점
        for i in range(N - d):
            j = i + d # j: 끝 지점
            
            # 최댓값 설정 (2^31 - 1)
            dp[i][j] = 2147483647 
            
            # i와 j 사이를 k로 쪼개기
            # 이 부분이 가장 많이 실행되므로 최적화가 필요함
            curr_i_row = matrix[i][0]
            curr_j_col = matrix[j][1]
            
            for k in range(i, j):
                # 점화식: 왼쪽 비용 + 오른쪽 비용 + (왼쪽행 * 공통열 * 오른쪽열)
                cost = dp[i][k] + dp[k+1][j] + (curr_i_row * matrix[k][1] * curr_j_col)
                if cost < dp[i][j]:
                    dp[i][j] = cost

    print(dp[0][N-1])

solve()
