
* 
	* Goal:
	* Key point:
	* 


* 
	* 
	* 


* **Classic** 
	* Find patterns of the solutions of the problem
	* There are two patterns which meets the requirements: (1). two circled person, and two arms. (2). an entire circle
	* [Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/1660944/c-dfs-with-illustration/?orderBy=most_votes)


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
	* Record the starting and endings of intervals with an array(arr\[s\]++, arr\[e\]--). Iterate over value, adding the value of arr, sum of that will be **number of intervals convering that value**.
	* [Number of Flowers in Full Bloom]

* Hard
	* Finding the K-th biggest sum from an array
	* Starts with maximum value, get the next-smaller values by (1). removing/adding the smallest positive/biggest negative value (2). removing previous selecition, move to next s/b value
	* [Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array/solutions/2457384/priority-queue-c/?orderBy=most_votes)

* Hard
	* Find number of subsequences with max and min fixed
	* Three-pointer sliding window, number in window is within range, considering the valid range ending with i while iterating, which is $min(prevMin, prevMax) - prevBad$
	* [Count Subarrays with fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation/?orderBy=most_votes)

* 
	* Gudge if there's element appears odd times
	* xor
	* Seems like other kinds of appearing pattern can't be decided in O(N) easily
	* [Find Longest Awesome Substring](https://leetcode.com/problems/find-longest-awesome-substring/)

  
* Hard, Classics
	* Ways to fill rectange with square
	* Again, finding patterns help. The special case can be formed by 4 normal rectangular, and 1 rectangular in the middle
	* [Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/solutions/414260/8ms-memorized-backtrack-solution-without-special-case/?orderBy=most_votes)


* 
	* Find Number of different GCDs
	* A number N can be a GCD, if and only if the gcd of all numbers divisible by N, is N itself. If g(N) = N already, it will holds later
	* [Number of Different Subsequences GCDs](https://leetcode.com/problems/number-of-different-subsequences-gcds/description/)


* 
	* Reverse pairs
	* A number N can be a GCD, if and only if the gcd of all numbers divisible by N, is N itself. If g(N) = N already, it will holds later
	* [Number of Pairs Satisfying Inequality](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/solutions/2646606/python-reverse-pairs/?orderBy=most_votes)



* 
	* If exists path with max edge length
	* If exists, the paths consists of shorter edge <-> exist shorter edge make the path <-> exist shorter edge connects the point <-> All shorter edge connects the point
	* [https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/submissions/917168157/](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/submissions/917168157/)


* 
	* If exists path with max edge length
	* If exists, the paths consists of shorter edge <-> exist shorter edge make the path <-> exist shorter edge connects the point <-> All shorter edge connects the point
	* [https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/submissions/917168157/](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/submissions/917168157/)

* Classic
	* Two-approach
	* Maintain two data structure, to make the update/query more efficient
	* [Design a Text Editor](https://leetcode.com/problems/design-a-text-editor/description/)

* 
	*  Calculate 2d prefix, to judge if a rectangular contains something
	* The last 2d prefix sum is tricky, since to make a cell stamped, that cell is not the only place to place the top-left of the stamp.The top-left can be placed anywhere within (x - w, y - h) ~ (x,y)
	* [Stamping The Grid](https://leetcode.com/problems/stamping-the-grid/description/)

* 
	* Minimum number to pick up, with sum >= k
	* Greedy, calculate max sum with i numbers picking up, always picking up the maximum number within reach
	* [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/submissions/917314858/)


* 
	* Finding min(A[i], A[j]) * ( j - i ) - sum(A[i:j])
	* sum(h\[front\] - h\[middle\]), when h[i] > h[front],  a new boundary starts, since the prev boundaray(h[front]) is lower
	* [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

* 
	* DFS in disguise, actually top-sort
	* each color A can not exist in B, while surrounding B at the same time. Use DFS to visit A, mark A as invalid after searching, if exists B, while visiting B, A will be in B's covering with invalid mark
	* Essential part: A surrounds B => A > B, B surrounds A => B > A, mark A = B + 1 when A surrounds B, then when visiting B, later-found A shoud have smaller value, which conflicts with A = B + 1
	* [Strange Printer 2](https://leetcode.com/problems/strange-printer-ii/submissions/920702448/)


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


* 
	* find path
	* 1XXXXXXX -> ... -> 11000000 -> 1000000 -> ... -> 0
	* [Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/solutions/877741/c-solution-with-explanation/?orderBy=most_votes)

* 
	* Maximum value(Or Sum) of intervals
	* (1). Priority Queue on value, line sweep, put start and end separatedly. 
	* (2). Segment Tree
	* [Skyline](https://leetcode.com/problems/the-skyline-problem/solutions/61273/c-69ms-19-lines-o-nlogn-clean-solution-with-comments/)[]()
	* [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/solutions/137941/java-treemap-solution-inspired-by-skyline-and-meeting-room/?orderBy=most_votes) Sort on interval pair {x1,  +y1}  ~ {x2, -y2}, with map<height, count>, for each interval, scan through the map to get the valid y_range with x_covered. The essential part is to, set {y, 1} when y becomes valid, and {y, - 1} when invalid, adding that counter when pass through, check the sign of the counter
	* [Falling Squares](https://leetcode.com/problems/falling-squares/solutions/108764/easy-and-concise-python-solution-97/?orderBy=most_votes) 

* 
	* Maximum times of multiple subtraction
	* Very intuitive: a battery can no be taken more than answer hours 
	* [Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/solutions/1693347/heap-vs-binary-search/?orderBy=most_votes )


* 
	* Normalize, means indexing different numbers with unique id
	* You can move a char to anywhere, if you can swap adjacent chars in a string

* 
	* Minimum number to pick up, with sum >= k
	* Greedy, calculate max sum with i numbers picking up, always picking up the maximum number within reach
	* [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/submissions/917314858/)

* 
	* Minimum prefix\[A\[i\]\] +  B\[i\]
	* Fixing the first i index, the answer is k(prefix\[i\] is also fixed) + B\[i\], so the minimum B should be selected last
	* I nearly think of this solution, but skip that thought after taking the un-certainty of the prefix  into consider. However, if we only focused at last position, the prefix is always fix
	* Maybe only focus on one part, the remaining parts will be handled
	* [Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/description/)


* 
	* Shortest interval convering query points
	* Regular solution: sort query and intervals, while iterating queries, update all available(covering) intervals( by pushing intervals which start <= q, and popping those end <= q), retrive the smallest. Like a sliding window
	* Intuitive solution: check each interval from short to long, check if it covers some queries
	* [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/solutions/?orderBy=most_votes)



* 
	* Sequence ending with number
	* dp\[ending character\] = sum(all dp) + new sequence with single new character
	* [Number of Unique Good Subsequences](https://leetcode.com/problems/number-of-unique-good-subsequences/)


* 
	* Convex Function 
	* Binary Search for the bottom
	* [Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/solutions/2734091/dp-vs-w-median-vs-binary-search/?orderBy=most_votes)

* 
	* Ways to make fixed-length array with product
	* (1). Prime factorization (2). Stars and bars (3). Distinguishable stars
	```cpp
    for (auto p : primes) {
            int r = 0;
            while (k % p == 0) {
                ++r;
                k /= p;
		    }     
    }
```
	* The Ways to put **r** factors into **N** numbers, is $Comb(N+r, r)$
	* [Count Ways to Make Array With Product](https://leetcode.com/problems/count-ways-to-make-array-with-product)


	* Count digits
	* Set\<prefix integers\>, use permutation to calculate possibilities with prefix given
	* [Count Special Integers](https://leetcode.com/problems/count-special-integers/solutions/2425271/java-python-math/?orderBy=most_votes)




![[Pasted image 20230325113448.png]]