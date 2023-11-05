class DisjointSet:
    def __init__(self, elements):
        self.parent = {i: i for i in elements}
        self.rank = {i: 0 for i in elements}

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_x] = parent_y
                if self.rank[parent_x] == self.rank[parent_y]:
                    self.rank[parent_y] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n, self.n * 2):
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 0:
            self.tree[i // 2] = self.tree[i] + self.tree[i ^ 1]
            i //= 2

    def query(self, i, j):
        i += self.n
        j += self.n
        res = 0
        while i < j:
            if i & 1:
                res += self.tree[i]
                i += 1
            if j & 1:
                j -= 1
                res += self.tree[j]
            i //= 2
            j //= 2
import math

# parent: parents of each node e.g. [0, 1, 1, 1, 2, 2, 3]
def preprocess(n, parent):
    # Initialize the dp table.
    dp = [[-1 for _ in range(int(math.log2(n)) + 1)]
            for _ in range(n+1)]
 
    # Parent of every node i is parent[i]
    for i in range(1, n+1):
        dp[i][0] = parent[i]
 
    # Fill dp[] using values in dp[][]
    for i in range(1, n+1):
        for j in range(1, int(math.log2(n)) + 1):
            if dp[i][j-1] != -1:
                dp[i][j] = dp[dp[i][j-1]][j-1]
 
    return dp

def binary_lifting(n, dp, u, k):
    # Logarithm base 2 of n
    log = int(math.log2(n))

    # Check if the node u has a k-th parent.
    if k > (1 << log):
        return -1

    # Calculate the k-th parent for node u
    for i in range(log, -1, -1):
        if (k & (1 << i)) > 0:
            u = dp[u][i]

    return u

# dp: [i-th node][j] = 2^j-ancestor
# depth: depth of each node
def lca(n, dp, u, v, depth):
    log = int(math.log2(n))

    # If v is situated on a higher level than u, then swap them
    if depth[v] < depth[u]:
        u, v = v, u

    # Compute the difference of levels
    diff = depth[v] - depth[u]

    # Lift v up to the same level as u
    for i in range(log, -1, -1):
        if (diff & (1 << i)) > 0:
            v = dp[v][i]

    # If u and v are at the same position, then they are the lca
    if u == v:
        return u

    # Lift u and v up simultaneously
    for i in range(log, -1, -1):
        if dp[u][i] != -1 and dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]

    return dp[u][0]


# Preprocess the parent array
dp = preprocess(n, parent)

# Find the 2nd ancestor for node 5
print(binary_lifting(n, dp, 5, 2))  # Output: 1

# Find the 3rd ancestor for node 5
print(binary_lifting(n, dp, 5, 3))  # Output: -1

        
        return res
