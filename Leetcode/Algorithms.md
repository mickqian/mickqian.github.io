## Sweep Line

## Meet In the Middle

*  
	* Find minimum diffs
	* Calculate the sum, get the target, iterator num_cnt on one part of the half
	* [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/)


*  
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
	* Calculate the sum, get the target, iterator num_cnt on one part of the half
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
Rolling-hash to encode the seen string pattern in the set, check each hash value with the set
```c++
for (int i = 0; i < n; i++){
	hash = (hash * 26 + s[i] - s[i - k] * pow(26, p)) % mod;
}
```



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


## Z-function


## Re Rooting
DFS for once, use information from previous visit, to simulate differnt roots
* 
	*  Max Root Path Sum - Root
	*  ans\[i\] = max(subtree sum, parent and its other subtree sum) - v\[i\]
	* [Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/solutions/3052596/re-rooting-o-n-explained/?orderBy=most_votes)
