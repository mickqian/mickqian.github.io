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
        return res
