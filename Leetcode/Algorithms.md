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
	*  Maximum Subarray, find the subarray with the largest sum, and return its sum
	*  Just like sliding window, but in this case, the sum of the subarray is calculated. So when current subarray's sum is negative, instead of moving the start pointer forward until invalid, the remaining window is always empty, so we should set the start pointer to current end pointer
	*  Applies to all kinds of subarray, counting the max subarray value(could be occurence)


## Sliding Window
Valid, when the end pointer moves forward, the start pointer has to move forward to make the window valid again.

*  
	* Find minimum diffs
	* Calculate the sum, get the target, iterator num_cnt on one part of the half
	* [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/)


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