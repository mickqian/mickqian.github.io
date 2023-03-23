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
	*  
	* Choose Combination, then calculate Permutation