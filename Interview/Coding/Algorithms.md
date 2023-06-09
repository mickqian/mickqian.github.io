## Sweep Line

## Meet In the Middle
To find the shortest dist to target num, we have possibilities from 2 parts. 
Fix choice on each possibility on the first one, Binary Search (T - P(A)) in P(B)

*  
	* Find minimum diffs
	* Calculate the sum, get the target, iterator num_cnt on one part of the half
	* [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/)


*  
	* 
	* 


## Kadane's Algorithm

* 
	* Maximum Subarray, find the subarray with the largest sum, and return its sum
	* Just like sliding window, but in this case, the sum of the subarray is calculated. So when current subarray's sum is negative, instead of moving the start pointer forward until invalid(positive), the remaining window(start:mid) is always positive, so mid:end is always negative, so we should set the start pointer to current end pointer
	*  Applies to all kinds of subarray, counting the max subarray value(could be occurence)
	* [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

```c++
int max_subarray(vector<int>& numbers){
    // Find the largest sum of any contiguous subarray.
    int best_sum = 0
    int current_sum = 0
    for (auto x : numbers){
        current_sum = max(0, current_sum + x);
        best_sum = max(best_sum, current_sum);
    }
    return best_sum;
}
```


## Sliding Window
To find range that meets requirement
Valid, when :
1. after a valid window, the end pointer needs to move forward to accept new elements
2. when the end pointer moves forward, the start pointer has to move forward to make the window valid again.
*  
	* Find minimum diffs
	* Calculate the sum, store map\<num_count, set\<sum\>\> for 2 parts, iterate num_cnt on one part of the half

```cpp
long long countSubarrays(vector<int>& nums, long long k) {
    long long sum = 0, res = 0;
    for (int i = 0, j = 0; i < nums.size(); ++i) {
        sum += nums[i];
        while (sum * (i - j + 1) >= k)
            sum -= nums[j++];
        res += i - j + 1;
    }
    return res;
}
```

## Merge Sort

merge process naturally fetch every two items from two sorted sub-arrays, and **each** item get to combined each item from the right at least once.

```c++
int i = 0, mid = ( i + n ) / 2, j = mid;

while (i < mid && j < n){
		// each i in 0~mid have at least one combination to mid~n - 1
	if (nums[i++] < nums[j++]){
		temp[cnt++] = nums[i++];
	} else {
		temp[cnt++] = nums[j++];
	}
}
```

Utilize the attribute that, in a `merge(lo, mid, hi)`, the lo:mid-1 and mid:hi is already **ordered**.
Each element gets to compare with to-the-right number's range at least one time

## Boyer-Morre majority Vote
for elements appear at least n / k times, maintain k candidates:
```c++
for (auto& num : nums){
	for (auto& [can, cnt]: candidates){
		if (--cnt == 0){
			can = num, cnt = 0;
		}
	}
}
```


## KMP aka Prefix Suffix Subarray
Generate the table

```c++
	// kmp: [the index of the matching string] = [the index in the pattern string]
	vector<int> kmp(s.size());
    for (auto j = 0, i = 1; i < kmp.size(); ++i) {
        if (s[i] == s[j])
            kmp[i] = ++j;
        else if (j > 0) {
            j = kmp[j - 1];
            // recursive step back, to get the max matching len with the prefix
            --i;
        }
    }
```
use the table as a tool, to determine if an another string contains a pattern
```c++
     while (n_ep > 0 && ch != s[i]){
	     // calculate the max matching len of the character
         common_prefix_len = kmp[i - 1];
	 }
```


## Rabin-Karp
To check existence of **exactly equal** substrings
Time Complexity: O(len)
Rolling-hash to encode the string pattern in the set, check each hash value within the set
Rolling-hash can reduce the compare time from O(N) to O(1) ( if the hash can be computed in O(1))

```c++
for (int i = 0; i < n; i++){
	hash = (hash * 26 + s[i] - s[i - k] * pow(26, p)) % mod;
}
```

*  
	* Find the longest duplicate substring
	* Binary Search + Rabin-Karp will do
	* [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/solutions/?orderBy=most_votes)

*  
	* Check if a string pattern occurs repeatedly
	* Binary Search + Rabin-Karp will find the longest identical strings
	* Need binary search to fix the length first, and rolling-hash is perfect for finding hash for fixed length(just append the char at the end)
	* [Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath/solutions/1314826/rolling-hash-vs-suffix-automation/?orderBy=most_votes)




## Reservior Sampling

chance of placing cur item into reservior is $reservior\_cnt/item\_index$

```c++
(* S has items to sample, R will contain the result *)
ReservoirSample(S[1..n], R[1..k])
  // fill the reservoir array
  for i := 1 to k
      R[i] := S[i]

  // replace elements with gradually decreasing probability
  for i := k+1 to n
    // (* randomInteger(a, b) generates a uniform integer from the inclusive range {a, ..., b} *)
    j := randomInteger(1, i)
    if j <= k
        R[j] := S[i]
```


## Sieve

```c++
for (int i = 0; i <= mx; i++) sieve[i] = i;
	for (int i = 2; i <= mx; i++) {
        if (sieve[i] != i) {
             continue
        }
        for (int j = i * i; j <= mx; j += i) {
            if (sieve[j] > i) {
                sieve[j] = i;
            }
        }
    }
}
```




## Binomial Coefficients
Stars and Bars: placing m bars in n numbers = choosing n locations from m = number of partition array of n into m **subarray**

Forming an array of size n, with m consecutive unique numbers = placing m bars as transition in n numbers

```c++
	// pascal's triangle
	for (int s = 1; s <= m; ++s) // nCr (comb)  
	    for (int r = 0; r <= n ; ++r){
	        comb[s][r] = r == 0 ? 1 : (comb[s - 1][r - 1] + comb[s - 1][r]) % mod; }
```

[Count the Number of Ideal Arrays](https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2265366/sieve-of-eratosthenes-o-maxvalue/?orderBy=most_votes)


## Permutation


`std::next_permutation`

## LIS

1. dp1:

   * 状态：以 a[i] 结尾的 LIS

   * 转移： dp[i] = arr[i] > arr[j] ? arr[j + 1]

   * 复杂度：O(N^2)

2. dp2: 

   * 状态：a[i] 之前的，长度为 i + 1，末尾元素最小的 的 LIS
   * 转移：
     
     * 每次将 a[i] 插入序列即可
* 复杂度：O(NlogN)
  
 ```c++
     int main()
     {
         int n;
         vector<int> dp(n, INT_MAX);
         int pos=0;    // 记录dp当前最后一位的下标
         dp[0]=nums[0];
         for(int i=1; i<n; i++)
         {
            if(nums[i]>=dp[pos])
                // 组成更长的子序列
                dp[++pos]=nums[i];
            else
                // 当前值更小，替换子序列串
			    dp[lower_bound(dp,dp+pos+1,nums[i])-dp]=nums[i];
         }
         return pos;
     }
   ```



## Suffix Array
Sort all suffix substrings by starting index
Usage: 
* compare substrings
* 

```c++

// Structure to store information of a suffix
struct suffix
{
	int index;
	char *suff;
};

// A comparison function used by sort() to compare two suffixes
int cmp(struct suffix a, struct suffix b)
{
	return strcmp(a.suff, b.suff) < 0? 1 : 0;
}

// This is the main function that takes a string 'txt' of size n as an
// argument, builds and return the suffix array for the given string
int *buildSuffixArray(char *txt, int n)
{
	// A structure to store suffixes and their indexes
	struct suffix suffixes[n];

	// Store suffixes and their indexes in an array of structures.
	// The structure is needed to sort the suffixes alphabetically
	// and maintain their old indexes while sorting
	for (int i = 0; i < n; i++)
	{
		suffixes[i].index = i;
		suffixes[i].suff = (txt+i);
	}

	// Sort the suffixes using the comparison function
	// defined above.
	sort(suffixes, suffixes+n, cmp);

	// Store indexes of all sorted suffixes in the suffix array
	int *suffixArr = new int[n];
	for (int i = 0; i < n; i++)
		suffixArr[i] = suffixes[i].index;

	// Return the suffix array
	return suffixArr;
}
```



## Z-function
  $z[i]$  is the length of the longest string that is, at the same time, a prefix of   $s$  and a prefix of the suffix of   $s$  starting at i
```cpp
vector<int> z(string &s) {
    vector<int> z(s.size());
    int l = 0, r = 1;
    for (int i = 1; i < s.size(); ++i) {
        z[i] = i > r ? 0 : min(r - i, z[i - l]);
        while (i + z[i] < s.size() && s[z[i]] == s[z[i] + i])
            ++z[i];
       if (z[i] + i > r) {
           l = i;
           r = z[i] + i;
        }
    }
    return z;
}
```


## Re Rooting

It says so on the post:
> 1.  Arbitrary root the tree, lets take `node 0` for explanation.
> 2.  Solve the given problem as if it was rooted at `node 0`.
> 3.  Similarily solve the problem for all nodes

But I think it's still very vague.

DFS for once, use information from previous visit, to simulate different roots
* 
	*  Max Root Path Sum - Root
	*  ans\[i\] = max(subtree sum, parent and its other subtree sum) - v\[i\]
	* [Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/solutions/3052596/re-rooting-o-n-explained/?orderBy=most_votes)

* 
	*  Possible roots, given at least k of the parent-children query is correct( what the heck is this problem? )
	*  Follow the steps, (1). assume 0 as the root, (2). calculate correct guess (3). DFS. While visiting a new child, correct guess changes atmost 1, updating corrent gusses and update final answer
	* [Count Number of Possible Root Nodes](https://leetcode.com/problems/count-number-of-possible-root-nodes/solutions/3256065/re-rooting-o-n-explained/?orderBy=most_votes)

## Eulerian Path
-   A graph has an Eulerian Path if and only if
    1.  we have `out[i] == in[i]` for each node `i`. Or
    2.  we have `out[i] == in[i]` for all nodes `i` except **exactly two** nodes `x` and `y`, with `out[x] = in[x] + 1`, `out[y] = in[y] - 1`, where x being the head, y being the tail


## Hamilton Path


## De Brujin


## Investors

#### Intention
\[cost, threadshold\] pair, return the:
(1). minimum start up, in some order, or
(2). minimum start up, in any order
#### Intuition
turn to a new story:
> If you want to invest on a project `[x,y]`, you must have `y` money. Once finished, you gain `y-x` money. So, which project you should invest first to build up a good capital for the next investments?

Cause a task's gonna be done anyway. Anytime it got done, we want to borrow money(from the startup money), and the done the deal. The profit is t - c. To do more investment, take the most profitable transaction first

Do the task with largrest profits(y - x) first

[Minimum Initial Energy to Finish Tasks](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/)

## Graham scan


## Knapsack

### Multi-knapsack
NP-complete
Most of the multi knapsack problems is solved by **pruning**
* 
	*  Max Root Path Sum - Root
	*  ans\[i\] = max(subtree sum, parent and its other subtree sum) - v\[i\]
	* [Find Minimum Time to Finish All Jobs](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/solutions/1009768/c-0ms-use-greedy-to-prune/?orderBy=most_votes)

* 
	* Two Subarray with same average
	* dp\[length]\[s+A\[i]] = true is the sum exists for length 
	* dp\[sum] = bitmask of subaray with length as i 
	* [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/solutions/120667/c-solution-with-explanation-early-termination-updated-for-new-test-case/?orderBy=most_votes)

### 0-1 Knapsack
pick a candidate, or not

https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns#Merging-Intervalshttp://


## Game(of thrones)
Most straighforward method: enumerate each possible move on each player

### Combinatory Game Theory
First you need understand the N position and P postion from Combinatorial Game Theory.  
P-Position is previous player win, N-Position is next player (current player) win.  

A position is a N-Position as long as **one of** its following positions is P-Position, i.e. if current player take this move, in next turn he as the previous player is guaranteed to win.  

A position is a P-Position only if **all** its following positions are N-Position, i.e. no matter how current player move, the previous player is guaranteed to win in next turn.
```c++
bool winnerSquareGame(int n) {
        will =vector<int>(n + 1, -1);
        if (will[n] != -1) {
            return will[n];
        }

        bool win = false;
        int maxSF = findMaxSquareFoot(n);
        if (maxSF * maxSF == n) {
            win = true;
        } else {
            for (int i = 1; i <= maxSF; i++) {
                int nextMove = i * i;
                if (!winnerSquareGame(n - nextMove)) {
                    // Bob will loose
                    win = true;
                    break;
                }
            }
        }
        will[n] = win ? 1: 0;
        return win;
}

int findMaxSquareFoot(int n) {
    return ::floor(::sqrt(n));
}
```

## Random Pick
Reduce the probability by random-pick several times is acceptable
One-time miss being p, 5 time miss will be p^5, which will be very small


## Tarjan's Algorithm
Find the cycle(with edges) of a given graph
```cpp
 int time = 1;
 void dfs(int curr, int prev) {
		// disc: the first time curr is visited
		// low: the first time cycle of curr is visited
        disc[curr] = low[curr] = time++;
        for (int next : adj[curr]) {
            if (disc[next] == 0) {
	            // unvisited next
                dfs(next, curr);
                low[curr] = min(low[curr], low[next]);
            } else if (next != prev)
                low[curr] = min(low[curr], disc[next]);
            if (low[next] > disc[curr]) {
	            // next has been visited, with low[next] marked as length of that  cycle
                ans.push_back({curr, next});
            }
        }
    }
```

### Appendix: Find Cycles
```cpp
int bfs(int n,vector<int> adj[]){
        int ans = INT_MAX;
        for (int i = 0; i < n; i++) {
            vector<int> dist(n,(1e9));
            vector<int> parents(n, -1);
            dist[i] = 0;
            queue<int> q = {i};
            while (!q.empty()) {
                int x = q.front();
                q.pop();
                for (int c : adj[x]) {
                    if (dist[c] == (int)(1e9)) {
                        dist[c] = 1 + dist[x];
                        par[c] = x;
                        q.push(c);
                }
                else if (parents[x] != c && parents[c] != x)
                    ans = min(ans, dist[x] + dist[c] + 1);
                }
            }
        }
        if (ans == INT_MAX)
            return -1;
        else
            return ans;
}
```



## Traveling Salesman

 directed graph shortest path of Hamilton path
 each node is visited once

* 
	*  
	* precalculate the overlapped length as weight of the path
	* I wonder if a = "abc",  b = "xyabc", then ab = 3, then the dfs won't work. But that's wrong, since in this case, the ba sequence will yield the correct answer
	* [Find The Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/solutions/194932/travelling-salesman-problem/?orderBy=most_votes)



## Topological sort
```c++
vector<int> top_sort(int k, vector<vector<int>> &conditions) {
        vector<int> order(k, -1);
        vector<int> sorted;
        vector<int> q;
        vector<vector<int>> adj(k);
        vector<int> in(k);
        for (auto &condition: conditions) {
            adj[condition[0] - 1].push_back(condition[1] - 1);
            in[condition[1] - 1]++;
        }

        for (auto i = 0; i < k; i++) {
            if (in[i] == 0) {
                q.push_back(i);
            }
        }

        while (!q.empty()) {
            // q: current unvisited list
             vector<int> q1;
             for (auto i: q) {
                 sorted.push_back(i + 1);
                 for (auto& j: adj[i])
                     if (--in[j] == 0)
                         q1.push_back(j);
             }
             swap(q, q1);
         }

         if (sorted.size() != k)
             return {};
        return sorted;

    }
```


## Manacher's Algorithm
Longest Palindrome Substring

```c++
vector<int> d1(n), d2(n);
for (int i = 0; i < n; i++) {
  d1[i] = 1;
  while (0 <= i - d1[i] && i + d1[i] < n && s[i - d1[i]] == s[i + d1[i]]) {
    d1[i]++;
  }

  d2[i] = 0;
  while (0 <= i - d2[i] - 1 && i + d2[i] < n &&
        s[i - d2[i] - 1] == s[i + d2[i]]) {
    d2[i]++;
  }
}
```

## Bellman-Ford
Single-source shortest paths

```java
public boolean SSSP(int s, Edge[] edges) {
        //初始化
        for (int i = 0; i < n; i++) {
            dis[i] = i == s ? 0 : INF;
        }
        //每一轮的顶点，对所有的edges做松弛
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < e; j++) {
                if (dis[edges[j].v] > dis[edges[j].u] + edges[j].w) {//relax操作
                    dis[edges[j].v] = dis[edges[j].u] + edges[j].w;
                    pre[edges[j].v] = edges[j].u;
                }
            }
        }
        boolean f = false;
        for (auto& e: edges) {
            if (dis[e.v] > dis[e.u] + e.w) {
                f = true;
                break;
            }
        }
        return f;
    }
```



```c++
int SPFA(int s) {
	queue<int> q;
	bool inq[maxn] = {false};
	for(int i = 1; i <= N; i++) dis[i] = 2147483647;
	dis[s] = 0;
	q.push(s); inq[s] = true;
	while(!q.empty()) {
		int x = q.front(); q.pop();
		inq[x] = false;
		for(int i = front[x]; i !=0 ; i = e[i].next) {
			int k = e[i].v;
			if(dis[k] > dis[x] + e[i].w) {
				dis[k] = dis[x] + e[i].w;
				if(!inq[k]) {
					inq[k] = true;
					q.push(k);
				}
			}
		}
	}
	for(int i =  1; i <= N; i++) std::cout << dis[i] << ' ';
	std::cout << std::endl;
	return 0;
}
```