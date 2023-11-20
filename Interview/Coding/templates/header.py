
class BitTrie:
    def __init__(self):
        self.children = [None, None]

    def insert(self, key, l=19):
        node = self
        for i in range(l, -1, -1):
            bit = (key >> i) & 1
            if not node.children[bit]:
                node.children[bit] = BitTrie()
            node = node.children[bit]

    def remove(self, n, l=19):
        if l < 0:
            return True
        bit = (n & (1 << l)) > 0
        if self.children[bit] and self.children[bit].remove(n, l - 1):
            self.children[bit] = None

        return not self.children[bit] and not self.children[1]

    def max_xor(self, key, l=19):
        if l < 0:
            return 0
        bit = (key & (1 << l)) > 0
        # choose the bit with highest xor result
        if self.children[1 - bit]:
            return (1 << l) + self.children[1 - bit].max_xor(key, l - 1)
        # choose second choice
        return self.children[bit].max_xor(key, l - 1)


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sortedcontainers.SortedSet(nums)

        trie = BitTrie()
        last = 0
        ans = 0

        # trie.insert(3)
        # trie.max_xor(3)

        for i in range(len(nums)):
            while last < len(nums) and nums[last] - nums[i] <= nums[i]:
                trie.insert(nums[last])
                last += 1
            ans = max(ans, trie.max_xor(nums[i]))
            trie.remove(nums[i])
        return ans


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


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.max = 0
        self.left = self.right = None
        self.lazy = 0

class LazySegmentTree:
    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def __init__(self, arr, merge=lambda x, y: x + y, basef=lambda x: x, basev=0):
        """Build the segmentation tree."""
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = n = len(arr)
        self.tree = [0] * (4 * n)
        # `1` for pending updates
        self.lazy = [0] * (4 * n)
        self.len = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                self.tree[node] = arr[start]
            else:
                mid = (start + end) // 2
                build(node * 2 + 1, start, mid)
                build(node * 2 + 2, mid + 1, end)
                self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

        build(0, 0, n - 1)

    def update_util(self, node, start, end, q_start, q_end, val=0) -> None:
        """Update segment tree when value in [q_start, q_end] is flipped."""
        self.prop_lazy(node, start, end)
        if start > end or start > q_end or end < q_start:
            return

        if start >= q_start and end <= q_end:
            self.tree[node] = self.len[node] - self.tree[node]
            if start != end:
                self.lazy[node * 2 + 1] ^= 1
                self.lazy[node * 2 + 2] ^= 1
            return

        mid = (start + end) // 2
        self.update_util(node * 2 + 1, start, mid, q_start, q_end, val)
        self.update_util(node * 2 + 2, mid + 1, end, q_start, q_end, val)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]


    def update_range(self, l, r, val=1):
        self.update_util(0, 0, self.n - 1, l, r, val)

    # handle lazy propagations
    def prop_lazy(self, node, start, end):
        # if the parent node has the notation to flip, then we update all summation of children nodes.
        if self.lazy[node] != 0:
            self.tree[node] = self.len[node] - self.tree[node]
            if start != end:  # not a leaf node
                self.lazy[self.left_child(node)] ^= 1
                self.lazy[self.right_child(node)] ^= 1
            self.lazy[node] = 0

    def query_util(self, node, start, end, l, r):
        if start > end or start > r or end < l:
            return 0

        self.prop_lazy(node, start, end)

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        p1 = self.query_util(node * 2 + 1, start, mid, l, r)
        p2 = self.query_util(node * 2 + 2, mid + 1, end, l, r)
        return p1 + p2

    def query_range(self, l, r):
        return self.query_util(0, 0, self.n - 1, l, r)


# Binary Lifting

# parent: parent of each node
# level: level of each node, root as 0
def preprocess(parent, n):
    log = math.ceil(math.log2(n))
    dp = [[-1 for _ in range(log)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = parent[i]

    for j in range(1, log):
        for i in range(1, n + 1):
            if dp[i][j - 1] != -1:
                dp[i][j] = dp[dp[i][j - 1]][j - 1]
    return dp


def find_lca(u, v, dp, parent):
    if level[u] < level[v]:
        u, v = v, u

    log = len(dp[0])

    for i in range(log - 1, -1, -1):
        if (level[u] - (1 << i)) >= level[v]:
            u = dp[u][i]

    if u == v:
        return v

    for i in range(log - 1, -1, -1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]

    return parent[u]

