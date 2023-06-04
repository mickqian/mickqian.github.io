
相对顺序 + 值顺序： Monotonic Queue


### Fenwick tree

```c++
struct Fenwick {
    vector<int> arr;

    int N;

    Fenwick(int n) {
        N = n + 1;
        arr = vector<int>(N, 0);
    }

    void add(int i, int diff){  
		i += 1;  
		while (i < N) {  
			arr[i] += diff;  
			i += i & (-i);  
		}  
	}

	// query the prefix ( i excluded )
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
  SegmentTree(int n_) : n(n_) {
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

#### Lazy Segment Tree
```cpp
int tree[400000] = {}, lazy[400000] = {};  
  
int build(vector<int> &arr, int n, int a, int b){  
	if(a == b)  
		return tree[n] = arr[a];  
	return tree[n] = build(arr, 2 * n, a, (a + b) / 2) + build(arr, 2 * n + 1, (a + b) / 2 + 1, b);  
}  

// n : update cnt
// a, b: subtree range
// i, j : range to update
int update_tree(int n, int a, int b, int i, int j){  
	if(b < i || a > j) // outside  
		return lazy[n] ? b - a + 1 - tree[n] : tree[n];  
	if(lazy[n]) {  
		tree[n] = b - a + 1 - tree[n];  
		if(a != b) {  
			lazy[n * 2] = !lazy[n * 2];  
			lazy[n * 2 + 1] = !lazy[n * 2 + 1];  
		}  
	lazy[n] = 0;  
	}
	if(a >= i && b <= j) { // inside  
		if(a != b) {  
			lazy[n * 2] = !lazy[n * 2];  
			lazy[n * 2 + 1] = !lazy[n * 2 + 1];  
		}  
	return tree[n] = b - a + 1 - tree[n];  
	}  
	return tree[n] = update_tree(n * 2, a, (a + b) / 2, i, j) +  update_tree(n * 2 + 1, (a + b) / 2 + 1, b, i, j);  
}  
  
build(n1, 1, 0, sz - 1);  
update_tree(1, 0, sz - 1, q[1], q[2]);  
sum += (long long) tree[1] * q[1];  
```

MAXBIT?
https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/solutions/1390159/c-python-same-with-longest-increasing-subsequence-problem-clean-concise/?orderBy=most_votes



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


DS can be used to build connectivity of partial nodes.
Just think of it as a way to **query indepedent group nodes and size(via voting)**




## Bit Trie
effectively judge the:
1. order
2. difference of different digits,
with the new value and previously inserted values.
Which shows the usage of Trie: Situation of first different item on the **prefix** sequence

```cpp
struct Trie {
    Trie* t[2] = {};
    int cnt = 0;
    void insert(int n, int i = 1 << 14) {
        ++cnt;
        bool b = n & i;
        if (t[b] == nullptr)
            t[b] = new Trie();
        if (i > 0)
            t[b]->insert(n, i / 2);
    }
    // e.g. for an application
    int countLess(int n, int lim, int i = 1 << 14) {
        bool n_b = n & i, lim_b = lim & i, x = (n xor lim) & i;
        return (lim_b && t[n_b] != nullptr ? t[n_b]->cnt : 0) +
            (t[x] != nullptr ? t[x]->countLess(n, lim, i / 2) : 0);
    } 
};
```

```cpp
	int countPairs(vector<int>& A, int low, int high) {
        return test(A, high + 1) - test(A, low);
    }

    int test(vector<int>& A, int x) {
        unordered_map<int, int> count, count2;
        for (int a : A) count[a]--;
        int res = 0;
        while (x) {
            for (auto const& [k, v] : count) {
                count2[k >> 1] += v;
                if (x & 1)
                    if (count.find((x - 1) ^ k) != count.end())
                        res += v * count[(x - 1) ^ k];
            }
            swap(count, count2);
            count2.clear();
            x >>= 1;
        }
        return res / 2;
    }
```


  

## Monotonic Queue

*  
	* 
	* Attribute: there're no smaller elements after item in an increasing stack
	* 



A queue which:

* the attribute A of items is monotonic, and unique
* the attribute B of items is also monotonic

It neglects all items smaller than before, since they are useless.

Attribute:

* the item at the beginning is the max one in a range, if the begining one gets poped when the window left
* the adjacent items are the next smaller/bigger one to each other
* while pushing new item, the new value is the next bigger one to the value being pushed
* the insert item will repeated incounter only and all the previous bigger element

Can be used to solve questions like

* sliding window with max/min values: the index of the max value is always kept at the beginning. If there is some bigger items with bigger index, the smaller in-between items are useless, because they will not be max values before the bigger items are removed, when they will be removed before.
* next index with bigger value: after removing smaller value in the end, the new value is the next-bigger value of the last value in queue
* finding the next smaller/bigger element of each: [Subarray With Elements Greater Than Varying Threshold](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/solutions/2259557/monostack/?orderBy=most_votes)
*


*  
	* Largest histogram
	* Increasing Queue, pop and calc
	* Attribute: Later-Smaller value are useless, they can't make rectangle larger than prev
	* 

*  
	* Min Length of Subarray with Sum at Least K
	* Keep index of increasing prefix Sum
	* Attribute:  In an increasing deque, prev-large indexes are discarded, which is useless in this case, since larger prefix sum will bring smaller subarray sum
	* 对于普通 MQ, 弹出A\[i\] <= V, 可以得到离 V 最近的 A\[i\] <= V（第一个弹出的）
	* 对于改进 MQ, 弹出 A\[i\] + K <= V, 可以得到离 V 最近的 A\[i\] + K <= V（第一个弹出的）
	* [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solutions/143726/c-java-python-o-n-using-deque/)
