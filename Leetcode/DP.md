
Divide problems into sub problems:

#### Top down(memoization)

* **recursive** function call, store results

* **apply** cache to **potential** duplicate calculation

* Accords to the natural logic of the original problem description

Choosed when there is some useless states, or no actual index concepts


#### Bottom up(Tabulation)

* **iterative** on the indices of sub problems

* **base** on the pre-calculated results

* choose and simplify the states, which will affect the results
   * state: Two finger's position, or even the previous character(https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)
   * only the previous uncovered tiles, even not of carpetLen, since all of the former states can contribute to the previous one [Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/)


Rough process:

1. Iterate over the indices of the state, may be 2D even 3D
2. Take all possible (optimal) actions on the current state
3. build the relation from results of current state and the state after the action is taken.
    * the relation may be derived from the natural thinking, and do a little math can contribute to ?
        * In the [Edit Distance](https://leetcode.com/problems/edit-distance/solutions/25846/c-o-n-space-dp/?orderBy=most_votes) case, the current state's best result comes from 3 actions, and **think about from prev state, apply 3 actions will lead to which future state's best results**. After the thinking is done,  think backwards, build the reverse relation, by taking the future state as current state, and look for the 3 pre-action, and which one from the pre-state is the best results.
        * 

#### forwarding

recursive iterative loop, moving forward at each index based on prev results




1. d[i] = d[j] + k： 
   1. 使用 top_down 或 单次迭代可完成
   2. top_down 可以忽略一些不必要的值
2. d[i] = d[j] + d[i - j] : 双循环


## One pass dp

* 
	* 
	* 


* 
	* The final result is calculated in one-pass, storing the possible extreme sub-result, assuming taking special conditions all-the-way 
	* [Minimum Time to Remove All Cars Containing Illegal Goods]

* 
	* \[n-th song\]\[different songs cnt\] = number of playlists
	* storing the cnt of different songs is enough, for us to calculate the plans for next song, as the next-song choice is only constrained by that.
	* [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/description/)


* 
		*  Optimize, by compressing the common state(length, value, etc) and **try on that possible state**
	* [Selling Pieces of Wood](https://leetcode.com/problems/selling-pieces-of-wood/description/)


* 
	*  $dp[n] = min(max(A[i], B[i])$, A\[i\] increase, B\[i\] decrease
	* Binary Search to find the i to make each part equal
	* [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/solutions/159055/java-dp-solution-from-o-kn-2-to-o-knlogn/?orderBy=most_votes)
	* Also, [tabulation](https://leetcode.com/problems/super-egg-drop/solutions/159508/easy-to-understand/?orderBy=most_votes) seems intuitive here 

* Classic
	* Minimum Intervals covering the range
	* \[position\] = minimum num of intervals to cover 0~ position
	* [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/)


* 
	* Valid permutations with relative order between consecutives
	* (1). Top-down: choosing every ID as the biggest, the remaining numbers can be chosed randomly, C(n, k)
	* (2). Bottom-up: Next State should care about the unused digits, and the number of ways to choose next digits. Since the relative order of the previous digit in the unused digit is the only state we care about, the next digit can choose from every previous dp, from the previous relative index. dp\[i\]\[k\] = dp\[i - 1\]\[k + 1: n - 1\]
	* It is tricky, but the remaining permutation can be viewed as permutation of random different digits, actually we don't care about the exact values. **For each possibility where the index of last digit  is the same, the next-permutation is also the same**
	* [Valid Permutations for DI Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence/solutions/?orderBy=most_votes)





## Memoization 


* Classic
	* If possible to fit numbers into boxes
	* Try combinations of items on each boxes, box-size to numbers mask
	* [distribute repeated numbers](https://leetcode.com/problems/distribute-repeating-integers/solutions/935522/step-by-step-optimization-more-than-10-methods/?orderBy=most_votes)


*  Classic
	* BitMasking to perform DFS
	* \[courses taken\]\[courses last semester\] = minimum days
		the courses of last semester should be stored, since it affects the courses available next semester.
		```cpp
		  for(int i = 0; i < (1 << n); i += 1){
            int ex = 0;
            // get the possible next semesters courses
            for(int j = 0; j < n; j += 1) if((i & pre[j]) == pre[j]) ex |= 1 << j;
            // get the unlearnt next semester courses
            ex &= ~i;
            // next semester, learn courses from ex
            for(int s = ex; s; s = (s - 1) & ex) if(__builtin_popcount(s) <= k){
                dp[i | s] = min(dp[i | s], dp[i] + 1);
            }
        }
		```


	* [Parallel Coursues2](https://leetcode.com/problems/parallel-courses-ii/)

* 
	* Recursively choose each item, top-down
	* iterate over each choice, recursive call
	* [Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/solutions/108318/c-java-python-dp-memoization-with-optimization-29-ms-c/?orderBy=most_votes)


* 
	* Ways to choose numbers(duplication), no order
	* With vector\<int\> as used numbers key, and trying every type of num in each call
	 [Maximum Number of Groups Getting  Fresh Donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/solutions/1140644/c-0-ms-greedy-dp/?orderBy=most_votes)

Divide problems into sub problems:

#### Top down(memoization)

* **recursive** function call, store results

* **apply** cache to **potential** duplicate calculation

* Accords to the natural logic of the original problem description

Choosed when there is some useless states, or no actual index concepts


#### Bottom up(Tabulation)

* **iterative** on the indices of sub problems

* **base** on the pre-calculated results

* choose and simplify the states, which will affect the results
   * state: Two finger's position, or even the previous character(https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)
   * only the previous uncovered tiles, even not of carpetLen, since all of the former states can contribute to the previous one [Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/)


Rough process:

1. Iterate over the indices of the state, may be 2D even 3D
2. Take all possible (optimal) actions on the current state
3. build the relation from results of current state and the state after the action is taken.
    * the relation may be derived from the natural thinking, and do a little math can contribute to ?
        * In the [Edit Distance](https://leetcode.com/problems/edit-distance/solutions/25846/c-o-n-space-dp/?orderBy=most_votes) case, the current state's best result comes from 3 actions, and **think about from prev state, apply 3 actions will lead to which future state's best results**. After the thinking is done,  think backwards, build the reverse relation, by taking the future state as current state, and look for the 3 pre-action, and which one from the pre-state is the best results.
        * 

#### forwarding

recursive iterative loop, moving forward at each index based on prev results




1. d[i] = d[j] + k： 
   1. 使用 top_down 或 单次迭代可完成
   2. top_down 可以忽略一些不必要的值
2. d[i] = d[j] + d[i - j] : 双循环


## One pass dp

* 
	* 
	* 


* 
	* The final result is calculated in one-pass, storing the possible extreme sub-result, assuming taking special conditions all-the-way 
	* [Minimum Time to Remove All Cars Containing Illegal Goods]

* 
	* \[n-th song\]\[different songs cnt\] = number of playlists
	* storing the cnt of different songs is enough, for us to calculate the plans for next song, as the next-song choice is only constrained by that.
	* [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/description/)


* 
	* \[first i-hats]\[assigned people] = ways
	* [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)


* 
	*  Optimize, by compressing the common state(length, value, etc) and **try on that possible state**
	* [Selling Pieces of Wood](https://leetcode.com/problems/selling-pieces-of-wood/description/)


* 
	*  $dp[n] = min(max(A[i], B[i])$, A\[i\] increase, B\[i\] decrease
	* Binary Search to find the i to make each part equal
	* [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/solutions/159055/java-dp-solution-from-o-kn-2-to-o-knlogn/?orderBy=most_votes)
	* Also, [tabulation](https://leetcode.com/problems/super-egg-drop/solutions/159508/easy-to-understand/?orderBy=most_votes) seems intuitive here 

* Classic
	* Minimum Intervals covering the range
	* \[position\] = minimum num of intervals to cover 0~ position
	* [Minimum Number of Taps to Open to Water a Garhttps://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/den](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/)


* Classic
	* Merge intervals
	* Minimum Cost to Merge Stones: $[i][j] = min([i][mid] + [mid + 1][j]) + range\_sum[i][j]$. The range sum is for, after merge sub-range, the number is replaced by sub_range
	* Burst Ballon:  Iterate on the **last** ballon to pop
	* Zuma:  More like a dfs search with memo, not strictly dp?
	* String Compression: 
		1.  Try to make the first i character the same, keep the max_occurence chars as the group, \[first i character\]\[move\] = min length
		2. \[first i chars\]\[prev char\]\[prev char cnt\]\[remain moves\] = min len
	* Strange Printer: 





## Memoization 


* Classic
	* If possible to fit numbers into boxes
	* Try combinations of items on each boxes, box-size to numbers mask
	* [distribute repeated numbers](https://leetcode.com/problems/distribute-repeating-integers/solutions/935522/step-by-step-optimization-more-than-10-methods/?orderBy=most_votes)

* 
	* Recursively choose each item, top-down
	* iterate over each choice, recursive call
	* [Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/solutions/108318/c-java-python-dp-memoization-with-optimization-29-ms-c/?orderBy=most_votes)


* 
	* Ways to choose numbers(duplication), no order
	* With vector\<int\> as used numbers key, and trying every type of num in each call
	 [Maximum Number of Groups Getting  Fresh Donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/solutions/1140644/c-0-ms-greedy-dp/?orderBy=most_votes)
