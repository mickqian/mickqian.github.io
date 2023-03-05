
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
	* 
	* 

* 
	* 
	* 

