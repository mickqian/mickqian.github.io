

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

