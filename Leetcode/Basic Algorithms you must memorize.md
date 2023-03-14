

## Consider Aspects

Every thing appears on the problems, Number of steps/Complete Gardens/cost, even the possibilities of given edges

And choose the one with minimum possibilites:

1. if the range of number is limited, but there might be many of them, why not use map/set/bitset to track the occurence of them ?
2. Always consider if iterate over the aspects if possible

 

### Monotonic Queue

A queue which:

* the attribute A of items is monotonic, and unique
* the attribute B of items is also monotonic

It neglects all items smaller than before, since they are useless.

Attribute:

* the item at the beginning is the max one in a range, if the begining one gets poped when the window left
* the adjacent items are the next smaller/bigger one to each other
* while pushing new item, the new value is the next bigger one to the value being pushed

Can be used to solve questions like

* sliding window with max/min values: the index of the max value is always kept at the beginning. If there is some bigger items with bigger index, the smaller in-between items are useless, because they will not be max values before the bigger items are removed, when they will be removed before.
* next index with bigger value: after removing smaller value in the end, the new value is the next-bigger value of the last value in queue
* LIS: the queue maintains the items of increasing items, in order

### Parametric Search

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo+hi)//2
            tot, cnt = 0, 1
            for num in nums:
                if tot+num<=mid: 
                    tot += num
                else:
                    tot = num
                    cnt += 1
            if cnt>m: lo = mid+1
            else: hi = mid
```



### Binary Search

find i such that :

* if low < i, f(low) = true,
* if high > i, f(high) = false

if i is in a certain range, we can narrow the range depending on the return value of the f()

Used when the compare is cheap, that is whether the middle value e.g:

1. the values in a sorted array
2. the maximum avaible i, where there exists a k

```rust
  		//  0 <= left <= left + size = right <= self.len()
		let mut size = self.len();
        let mut left = 0;
        let mut right = size;
        while left < right {
            let mid = left + size / 2;
            let cmp = cmp([mid], v);

            if cmp == Less {
                left = mid + 1;
            } else if cmp == Greater {
                right = mid;
            } else {
                return Ok(mid);
            }

            size = right - left;
        }

        Err(left)
```

### Kadane Algorithm(Maximum subarray problem)

[Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

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




### A star(Heuristic)

pursuit: **finds the shortest path from a specified source to a specified goal**

1. Roughly speaking, A* is a BFS with customized priority for selecting a node to expand; the priority is to select the lowest f()=heuristic()+cost()
2. A heuristic function is admissible if: it's always a lower bound of the actual cost from current state to target state (in this example, manhatten distance is admissible)
3. An important theorem: If heuristic function is admissible, then A* is guaranteed to find the optimal path



$$ f(n) = g(n) + h(n) $$, where:

* f(n): priority of n
* g(n): distance from start to n
* h(n): distance from n to target

```pseudocode
function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.prepend(current)
    return total_path

function A_Star(start, goal, h)
    openSet := {start}

    // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    // to n currently known.
    cameFrom := an empty map

    // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore := map with default value of Infinity
    gScore[start] := 0

    fScore := map with default value of Infinity
    fScore[start] := h(start)

    while openSet is not empty
        // This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        current := the node in openSet having the lowest f(n) value
        if current = target
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
            // d(current,neighbor) is the weight of the edge from current to neighbor
            // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore := gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := tentative_gScore + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)

    // Open set is empty but goal was never reached
    return failure
```



### Floyd-Warshall Algorithm

```c++
for (auto& e : edges) 
            dist[e[0]][e[1]] = dist[e[1]][e[0]] = 1;
        
for (int k = 0; k < n; k++)
    for (int i = 0; i < n; i++)
       for (int j = 0; j < n; j++)
           dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
```


### Traveling Salesman

 directed graph shortest path of Hamilton path




### Sequence

#### LCS


```python
def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]: # 如果相等，则加入现有的公共子串
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度
```

### LCP

### LIS

可用于所有 Ord,  if  $Ord[i, j] \& Ord[j, k]$, then  $$Ord[i, k] $$


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
     }```



### KMP


### Divisors

```c++
int gcd(int a, int b) {
   if (a < b) {
       return gcd(b, a);
   }
   if (a % b == 0) {
       return b;
   }
   return gcd(b, a % b);
}
```

