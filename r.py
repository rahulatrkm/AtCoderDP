'''
ps - https://atcoder.jp/contests/dp/tasks/dp_r
Matrix Exponentiation: A^K gives walks of length K
'''

def matmul(A, B, n, mod):
    """Multiply two n×n matrices modulo mod"""
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def matpow(mat, k, n, mod):
    """Compute mat^k using fast exponentiation"""
    # Initialize result as identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [row[:] for row in mat]  # Copy matrix
    
    while k > 0:
        if k % 2 == 1:
            result = matmul(result, base, n, mod)
        base = matmul(base, base, n, mod)
        k //= 2
    
    return result

def helper(mat, n, k):
    mod = 10**9 + 7
    
    # Compute mat^k
    result_mat = matpow(mat, k, n, mod)
    
    # Sum all entries in the result matrix
    total = 0
    for i in range(n):
        for j in range(n):
            total = (total + result_mat[i][j]) % mod
    
    return total

n, k = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

print(helper(mat, n, k))

