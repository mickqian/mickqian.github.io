* finding factors
```cpp
```


## Multinomial Coefficient
permutation of N1, N2... Nn numbers, with $Sum(N_{i}) = M$:
$M! / N_{1}! * N_{2}! * ... * N_{n}!$

a / x % mod == a * inv_mod % mod

找出 inv_mod
```python
class Factorial:  
    def __init__(self, N, mod) -> None:  
        N += 1  
        self.mod = mod  
        self.f = [1 for _ in range(N)]  
        self.g = [1 for _ in range(N)]  
        for i in range(1, N):  
            self.f[i] = self.f[i - 1] * i % self.mod  
        // 费马小定理： a * a^(mod - 2) == 1 (% mod)
        // 所以 a^(mod - 2) 是 a 的模拟
        // 所以 K * a == K * a^(mod - 2) (% mod)
        
		
        self.g[-1] = pow(self.f[-1], mod - 2, mod) 
        // calcuate mod inverse for all 阶乘
        for i in range(N - 2, -1, -1):  
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod  
  
    def fac(self, n):  
        return self.f[n]  
  
    def fac_inv(self, n):  
        return self.g[n]  
  
    def combi(self, n, m):  
        if n < m or m < 0 or n < 0: return 0  
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod  
  
    def permu(self, n, m):  
        if n < m or m < 0 or n < 0: return 0  
        return self.f[n] * self.g[n - m] % self.mod  
  
    def catalan(self, n):  
        return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.mod  
    def inv(self, n):  
        return self.f[n - 1] * self.g[n] % self.mod


# 求 数组的 permuation 数量（每个子集有n个元素）, 原先需要阶乘相除
# 每个被除的阶乘，可以处理为 * 阶乘 对 MOD 的模逆
facts = []
for num in nums:
	# ans /= num!
	# 换成
	ans *= mod_inv(num)
```
## Modular Multiplicative Inverse
$(A / B) \% mod = A * ( B ^ {-1} ) \% mod = A * (b ^ (mod -2))$

```cpp
	// the order of a sequence in all its permutation
	for (int i = sz - 1; i >= 0; --i)
    {
	    // only count sequence lower than i ~ sz here
	    // xxxxcxxxxx
        cnt[s[i] - 'a'] += 1;
        // fix the first number as lower
        // calculate the permutation of the remaining part
        auto prems = accumulate(begin(cnt), begin(cnt) + s[i] - 'a', 0l) * ft[sz - i - 1] % mod;
        for (int n : cnt)
            prems = prems * im[n] % mod;
        res = (res + prems) % mod;
	 }
```


## Permutations

### Choose different balls with total cnt fixed

```c++
  // split through each kind of balls
  for (int j = 0; j <= A[i]; ++j) { // try different splits at the `i`-th element, i.e. a[i] + b[i] = A[i]
            a[i] = j;
            b[i] = A[i] - j;
            ans += dfs(A, a, b, i + 1, sa + a[i], sb + b[i]);
  }
```


* 
	* a * b % k == 0 <=> gcd(a, k) * gcd(b, k) % k == 0
	* Choose Combination, then calculate Permutation


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
