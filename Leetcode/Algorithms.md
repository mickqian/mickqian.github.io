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
	*  Maximum Subarray, find the subarray with the largest sum, and return its sum
	*  Just like sliding window, but in this case, the sum of the subarray is calculated. So when current subarray's sum is negative, instead of moving the start pointer forward until invalid, the remaining window is always empty, so we should set the start pointer to current end pointer
	*  Applies to all kinds of subarray, counting the max subarray value(could be occurence)

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


## Sliding Window
To find range that meets requirement
Valid, when :
1. after a valid window, the end pointer needs to move forward to accept new elements
2. when the end pointer moves forward, the start pointer has to move forward to make the window valid again.

*  
	* Find minimum diffs
	* Calculate the sum, store map\<count, set\<sum\>\> for 2 parts, iterate num_cnt on one part of the half
	* [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/)

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

## Merge Sorts

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


## Boyer-Morre majority Vote
for elements appear at least n / k times, maintain k candidates:
```c++
for (auto& num : nums){
	for (auto& [can,cnt]: candidates){
		if (cnt == 0){
			can = num, cnt = 0;
		}
	}
}

// check if the candidate appears at leask k times
```


## KMP
Generate the table

```c++
	// kmp: [the index of the matching string] = [the index in the pattern string]
	vector<int> kmp(evil.size());
    for (auto j = 0, i = 1; i < kmp.size(); ++i) {
        if (evil[i] == evil[j])
            kmp[i] = ++j;
        else if (j > 0) {
            j = kmp[j - 1];
            // recursive step back, to get the max matching len
            --i;
        }
    }
```
use the table as a tool, to determine if a string contains a pattern
```c++
      while (n_ep > 0 && ch != evil[n_ep]){
	     // calculate the max matching len of the character
         n_ep = kmp[n_ep - 1];
	 }
```


## Rabin-Karp
To check existence of  **exactly equal** substrings
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
	* Binary Search + Rabin-Karp will do
	* Need binary search to fix the length first, and rolling-hash is perfect for finding hash for fixed length(just append the char at the end)
	* [Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath/solutions/1314826/rolling-hash-vs-suffix-automation/?orderBy=most_votes)




## Reservior Sampling

chance of placing cur item into reservior is $reservior_cnt/item_index$

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

* 
	*  Permutation of index
	*  Recusive with bitmask, finding the next ununsed index
	* [Minimum XOR SUM Of Two Arrays](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/solutions/1238641/bit-mask/?orderBy=most_votes)


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


## Re Rooting

It says so on the post:
> 1.  Arbitrary root the tree, lets take `node 0` for explanation.
> 2.  Solve the given problem as if it was rooted at `node 0`.
> 3.  Similarily solve the problem for all nodes

But I think it's still very vague.

DFS for once, use information from previous visit, to simulate differnt roots
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

