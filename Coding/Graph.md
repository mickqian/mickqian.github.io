  

*  
	* Find cycles(Aka **Tarjan's Bridge-Finding Algorithm**)
	* DFS, with dfn(time order) & low(lowest reachable time ordered from current root).
		$dfn(n) < low(v)$-> uv is a bridge. If a node with rank in-between, a cycle starts from that. Pick unvisited nodes to next round
	* [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/)



*  
	* Max 4 neighbors sum
	* To construct a valid sequence, start by selecting the middle part and extend it, with each node's top 3 neighbors(a's neighbor + a + b + the max remaining neighbour)
	* [Maximum Score of a Node Sequence](https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2261280/python-arranging-primes-intro-to-combinatorics/?orderBy=most_votes)