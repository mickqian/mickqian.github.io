//
// Created by 钱诚亮 on 2023/2/14.
//

#ifndef LEETCODEIDEAS_HEADER_H
#define LEETCODEIDEAS_HEADER_H
using namespace std;

class TreeNode{
public:
	TreeNode *left, *right;
	
	int val;
	
	TreeNode() : val(0), left(nullptr), right(nullptr){}
	
	TreeNode(int x) : val(x), left(nullptr), right(nullptr){}
	
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right){}
	
};

class DisjointSet{
public:
	vector<long> parents, rank;
	
	DisjointSet(int n){
		rank.resize(n);
		parents.resize(n);
		for (int i = 0; i < n; i++) {
			parents[i] = i;
		}
	}
	
	long find(long i){
		auto p = parents[i];
		if(i == p) {
			return i;
		}
		auto r = find(p);
		
		return parents[p] = r;
	}
	
	void join(long a, long b){
		auto aSet = find(a), bSet = find(b);
		if(aSet == bSet) {
			return;
		}
		else {
			parents[bSet] = aSet;

		}
	}
};


vector<int> sieve(int n){
	vector<int> p(n + 1);
	for (int i = 1; i <= n; i++) {
		p[i] = i;
	}
	
	for (int i = 2; i <= n; i++) {
		if(p[i] != i) {
			continue;
		}
		
		for (long long j = (long long)i * (long long) i; j <= n; j += i) {
			p[j] = i;
		}
	}
	
	return p;
}


class SegmentTree{

public:

vector<int> tree;
	SegmentTree(int n){
	    tree.resize(n)

	}

void build(vector<int>& nums, int node, int start, int end) {
    if (start == end) {
        tree[node] = nums[start];
    } else {
        int mid = (start + end) / 2;
        build(nums, 2 * node, start, mid);
        build(nums, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}

void update(int node, int start, int end, int idx, int val) {
    if (start == end) {
        tree[node] = val;
    } else {
        int mid = (start + end) / 2;
        if (start <= idx && idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}

int query(int node, int start, int end, int l, int r) {
    if (r < start || end < l) {
        return 0;
    }
    if (l <= start && end <= r) {
        return tree[node];
    }
    int mid = (start + end) / 2;
    int p1 = query(2 * node, start, mid, l, r);
    int p2 = query(2 * node + 1, mid + 1, end, l, r);
    return p1 + p2;
}

}




#endif //LEETCODEIDEAS_HEADER_H
