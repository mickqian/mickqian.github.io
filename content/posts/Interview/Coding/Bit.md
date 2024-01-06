---
title : ''
summary : ''
tags : [""]
author : ["Mick"]
draft : true
---

## Bit Mask
* 
	* 
	* 

CLRS book


```cpp
// to check if there's adjacent 1's
mask&(mask>>1)
```

A ^ B = C
A ^ B ^ B = C ^ B
A = C ^ B


* 
	* 
	* i-th bit of mask records the even/odd of appearance of a particular digit, dp\[mask\] is the first occurance index of that mask
	* I thought of using bit as the xor result of all numbers, but that can only show the xors of even digits, which is helpless to find an awesome string. awesome -> xor is the central digit. But having the prefix xors, we are unable to find a i for j, 0121,2**1322**
	* But having the prefix each-digit-even-odd, we can find awesome substrings by those prefix results, that mask ^ dp\[mask ^ (1 << each digit)\]
	* [Find Logest Awesome Substring](https://leetcode.com/problems/find-longest-awesome-substring/)