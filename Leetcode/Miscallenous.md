
* 
	* Goal:
	* Key point:
	* 


* 
	* 
	* 


* 
	* Find the required pattern for the result
	* [Transform to Chessborad](https://leetcode.com/problems/transform-to-chessboard/solutions/114847/c-java-python-solution-with-explanation/)

* 
	* N = x + (x + 1)...(x + n) = n * x + (n - 1) * n / 2
	* Counting odd factors
	* [Consecutive Numbers Sum](https://leetcode.com/problems/consecutive-numbers-sum/solutions/128947/java-c-python-fastest-count-odd-factors-o-logn/?orderBy=most_votes)

* 
	* Special Operation: Each time pushing a new element,  try merging with the last one in the stack. Two way merge
	* [Replace Non-Coprime Numbers in Array](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)

* 
	* Find number of intervals covering a value
	* Meeting Roomes Template: Given some intervals and an array of value, returns the number of intervals covering that value
	* Record the starting and endings of intervals with an array(arr[s]++, arr[e]--). Iterate over value, adding the value of arr, sum of that will be number of intervals convering that value.
	* [Number of Flowers in Full Bloom]

* Hard
	* Finding the K-th biggest sum from an array
	* Starts with maximum value, get the next-smaller values by (1). removing/adding the smallest positive/biggest negative value (2). removing previous selecition, move to next s/b value
	* [Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array/solutions/2457384/priority-queue-c/?orderBy=most_votes)


## Strategy
* 
	* Goal:
	* Strategy:
	* 


* 
	* 
	* 

* Hard
	* Find the least starting value
	* The **time** we have the least money is, aftering finishing the last lossing-money cost, but not gaining the cashback yet (1). make sure we get through before, needs prev_loss + this_cost (2). make sure get the money to start next transaction
	* [Minimum Money Required Before Transactions](https://leetcode.com/problems/minimum-money-required-before-transactions/solutions/2588034/java-c-python-easy-and-coincise/?orderBy=most_votes)