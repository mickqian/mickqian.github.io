
### DFS & BFS

* dfs: 验证连通性
* bfs: 可以携带一些当前节点的状态，常用于求加权最短路径

#### Difference

1. dfs 和 bfs 在时间复杂度上，由于 dfs 会保存一份context变量，而 bfs 会为每个状态保存一份变量，因此时间复杂度上不一致
2. To reduce search space:
   1.  memorization could be:
      1.  of visited paths(i to j) and associated values
      2.  of new states and associated(minimum or maximum) values
   2. On bfs, the prioritized value is always increasing, so it should be **exactly** what the problem what, and returns as soon as it meets the requirement.
   3. On dfs, return earlier when the current cnt has passed previous extreme value
   4. when don't know exact solutions, try greedy & (BFS|DFS)
3. dfs + memorization roughly equals to bfs?
   1. dfs needs to enumerate all possibilities, and use cache to shorten search space
   2. bfs gives best solutions naturally


### 0-1 BFS
[0-1 BFS](https://cp-algorithms.com/graph/01_bfs.html)
Djikstra without priority queue: [Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/solutions/2086235/0-1-bfs-c/?orderBy=most_votes)
1. Push unvisited neighbour with cost, to end of the queue
2. Push unvisited neighbour with cost, to beginning of the queue
So that the neighbor with lower cost will be visited first, and the cost of first visited is the minimum cost

## Optimization In BFS 
1. Store the visited path
2. Store \[visited notes\]\[ending node\]



* 
	* If a position is surrounded by wall of points
	* There are two patterns which meets the requirements: (1). two circled person, and two arms. (2). an entire circle
	* [Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/1660944/c-dfs-with-illustration/?orderBy=most_votes)

* 
	* Graphic search, move in 4 directions
	```cpp
	 double ans = DBL_MAX;
        vector<double> p(2, 0);
        double step = 100, eps = 1e-6;
        // dir = 1
        while (step > eps) {
            bool found = false;
            for (auto &dir : dirs) {
                vector<double> next = {p[0] + step * dir[0], p[1] + step * dir[1]};
                double d = all(A, next);
                if (d < ans) {
                    ans = d;
                    p = next;
                    found = true;
                    break;
                }
            }
            if (!found) step /= 2;
        }
	```
	* [Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/1660944/c-dfs-with-illustration/?orderBy=most_votes)

