'''
ps - https://atcoder.jp/contests/dp/tasks/dp_r
'''

def solve():
    MOD = 10**9 + 7
    
    def matmul(A, B, n):
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C
    
    def matpow(mat, k, n):
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        base = [row[:] for row in mat]
        while k > 0:
            if k % 2 == 1:
                result = matmul(result, base, n)
            base = matmul(base, base, n)
            k //= 2
        return result
    
    n, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    result_mat = matpow(mat, k, n)
    
    total = 0
    for i in range(n):
        for j in range(n):
            total = (total + result_mat[i][j]) % MOD
    
    print(total)

solve()