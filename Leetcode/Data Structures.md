
相对顺序 + 值顺序： Monotonic Queue


### Fenwick tree

```c++
struct BIT {
    vector<int> arr;

    int N;

    BIT(int n) {
        N = n + 1;
        arr = vector<int>(N, 0);
    }

    void add(int i) {
        i += 1;
        while (i < N) {
            arr[i] += 1;
            i += i & (-i);
        }
    }

    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += arr[i];
            i = i & (i - 1);
        }
        return sum;
    }
};
```



### Segment Tree

```cpp
class SegmentTree {
 public:
  int n;
  vector<int> tree;
  MaxSegmentTree(int n_) : n(n_) {
    int size = (int)(ceil(log2(n)));
    size = (2 * pow(2, size)) - 1;
    tree = vector<int>(size);
  }
  
  int max_value() { return tree[0]; }

  int query(int l, int r) { return query_util(0, l, r, 0, n - 1); }

  int query_util(int i, int qL, int qR, int l, int r) {
    if (l >= qL && r <= qR) return tree[i];
    if (l > qR || r < qL) return INT_MIN;

    int m = (l + r) / 2;
    return max(query_util(2 * i + 1, qL, qR, l, m), query_util(2 * i + 2, qL, qR, m + 1, r));
  }

  void update(int i, int val) { update_util(0, 0, n - 1, i, val); }
  void update_util(int i, int l, int r, int pos, int val) {
    if (pos < l || pos > r) return;
    if (l == r) {
      tree[i] = max(val, tree[i]);
      return;
    }

    int m = (l + r) / 2;
    update_util(2 * i + 1, l, m, pos, val);
    update_util(2 * i + 2, m + 1, r, pos, val);
    tree[i] = max(tree[2 * i + 1], tree[2 * i + 2]);
  }
};
```

### Trie

```c++
class TrieNode {
public:
    TrieNode* child[26];
    int count;
    
    TrieNode* insert(int c){
        if (child[c] == nullptr){
            child[c] = new TrieNode();
        }
        return child[c];
    }
};

void build(const string &word) {
	auto ptr = root;
    for (char ch: word) {
       int idx = ch - 'a';
	   ptr = ptr->insert(idx);
       ptr->count++;
    }
}
```


### Disjoint Set(aka Union-Find)

```c++
class UnionFind {
private:
    vector<int> parent, rank;

public:
    UnionFind(int size) {
        parent.resize(size);
        rank.resize(size, 0);
        // initially, parent i points to i itself
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void union_set(int x, int y) {
        int xset = find(x), yset = find(y);
        if (xset == yset) {
            return;
        } else if (rank[xset] < rank[yset]) {
            parent[xset] = yset;
        } else if (rank[xset] > rank[yset]) {
            parent[yset] = xset;
        } else {
            parent[yset] = xset;
            rank[xset]++;
        }
    }
};
```

