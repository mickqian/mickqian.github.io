
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


状态压缩：转移方程中若存在类似 dp[i] += dp[i - k]  的格式，考虑状态是否可压缩。最常用的状态压缩方式为求前缀和等


## One pass dp

* 
	* 
	* 


*  Hard
	*  \[0 ~ i chars\]\[j ~ end chars in the pattern\] = number of matches
	* From the contraints, we should fix with all the possibilities, which is not a big space
	*  Apply **Fixed Possibilities**, **store the states associated with that**
	* [Count Palindromic Subsequences](https://leetcode.com/problems/count-palindromic-subsequences/solutions/2851160/dp-vs-prefix-suffix/?orderBy=most_votes)



* 
	* \[first i groups\]\[mask of chosen value \] = numbers that can't be changed
	* **Inspiration**: using an index, and a mask marking the entire state affecting the next step, and iterate over all the possible mask is a regular operation
	* [Make the XOR of All Segments Equal to Zero](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/solutions/1097796/python-3-another-short-dp-7-lines-explained/?orderBy=most_votes)


* 
	* The final result is calculated in one-pass, storing the possible extreme sub-result, assuming taking special conditions all-the-way 
	* [Minimum Time to Remove All Cars Containing Illegal Goods]

* 
	* \[n-th song\]\[different songs cnt\] = number of playlists
	* storing the cnt of different songs is enough, for us to calculate the plans for next song, as the next-song choice is only constrained by that.
	* [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/description/)




## Memoization | Permutation


* 
	* 
	* 

* Classic
	* If possible to fit numbers into boxes
	* Try combinations of items on each boxes, box-size to numbers mask
	* [distribute repeated numbers](https://leetcode.com/problems/distribute-repeating-integers/solutions/935522/step-by-step-optimization-more-than-10-methods/?orderBy=most_votes)

* 
	* Subsequence sums
	* \[first i numbers\]\[choosing j numbers\] = possible sums as set, check if sum == j * average
	* Basically a NP problem, O($N^2 * m$), but we need only check the sums of less than n/2 numbers
	* [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/solutions/120667/c-solution-with-explanation-early-termination-updated-for-new-test-case/?orderBy=most_votes)


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
	* With vector<int> as used numbers key, and trying every type of num in each call
	 [Maximum Number of Groups Getting  Fresh Donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/solutions/1140644/c-0-ms-greedy-dp/?orderBy=most_votes)
