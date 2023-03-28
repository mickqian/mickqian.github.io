* finding factors
```cpp
```


## Multinomial Coefficient
permutation of N1, N2... Nn numbers, with Sum(Ni) = M:
$M! / N1! * N2! * ... * Nn!$

## Modular Multiplicative Inverse
$(A / B) \% mod = A * ( B ^ -1 ) \% mod = A * (b \^ (mod -2))$

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
