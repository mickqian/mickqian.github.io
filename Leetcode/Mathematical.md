* finding factors
```cpp
```


## Multinomial
permutation of N1, N2... Nn numbers, with Sum(Ni) = M:
$M! / N1! * N2! * ... * Nn!$

## Modular Multiplicative Inverse
$(A / B) % mod = A * ( B ^ -1 ) % mod = A * (b ^ (mod -2))$

```c++
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

