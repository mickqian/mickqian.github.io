## 凸优化
找出使凸函数值最小的x，为全局最优值
局部最优解一定是全局最优解

## 方法
* 梯度下降
* 牛顿法
* 拟牛顿法



## 傅立叶变换 Fourier Transformation
* $x[n]$: 信号
* $X[k]$: 频率为 k 的震荡函数的级数（cos, sin）

缺点：
1. 不能刻画时间域上信号的局部特性
2. 对突变和非平稳信号的效果不好，没有时频分析


Gibbs效应：



## FS Fourier Series
$$

\begin{align} f(t)&=\frac{a_{0}}{2}+\sum_{n=1}^{\infty}{[a_{n}cos(n\omega t)+b_{n}sin(n\omega t)]}  \tag{1}  \\

&a_{n}=\frac{2}{T}\int_{t_{0}}^{t_{0}+T}f(t)cos(n\omega t)dt \tag{2} \\ 
 
&b_{n}=\frac{2}{T}\int_{t_{0}}^{t_{0}+T}f(t)sin(n\omega t)dt \tag{3}\\ \end{align}
$$

### DFT
$X[k]=\sum_{n=0}^{N-1}e^{-j\frac{2\pi}{N}{nk}}x[n]$ 

#### IDFT

#### FFT Fast Fourier Transform 快速傅立叶变换
将 DFT 矩阵分解成稀疏因子的乘积来快速计算
是 DFT 算法

$X(K)=\sum_{r=0}^{\frac{N}{2}-1}x(2r)W_{\frac{N}{2}}^{rk}+W_N^r\sum_{r=0}^{\frac{N}{2}-1}x(2r+1)W_{\frac{N}{2}}^{rk}$

[推导过程](https://blog.csdn.net/enjoy_pascal/article/details/81478582)

#### 欧拉公式
$e^{i\theta}=cos\theta+i\cdot sin\theta$


### STFT 短时傅立叶变换
加窗傅立叶变换 -> 局部性
![[Pasted image 20230512231535.png]]
窗太小 -> 频率分辨率差
窗太大 -> 时间分辨率差


海森堡不确定性：我们不能同时获取一个粒子的动量和位置，我们也不能同时获取信号绝对精准的时刻和频率




## 小波变换 Wavelet transform

![[Pasted image 20230513125020.png]]


干脆直接把傅里叶变换的基给换了，将无限长的三角函数基换成了有限长的会衰减的小波基

傅里叶变换，变量只有w，而小波变换则有尺度a和平移量b，尺度对应于频率，平移量对应于时间


基的正交性：充分条件，内积为1
基具有完备性即可
基的表示有唯一性

时频分析

![[Pasted image 20230512231658.png]]

$\tau$: 移量
$a$: 横向尺度，对应频率（反比）
t 时刻，频率为 a 的正弦波的振幅

步骤：
1. 小波 w(t) 和 f(t)的 *开始部分* 作内积，计算系数C
2. 向右平移小波，重复1
3. 扩展小波，重复1，2
4. 不断扩展，重复1，2，3


#### CWT 连续小波变换
![[Pasted image 20230513124232.png]]

#### DWT 离散小波变换
离散的参数a,b，以降低运算量

1. RWT 冗余小波变换
	* a: 指数扩张
	* b: $b = nb_{0}a_{0}^{m}$
2. MRA: 尺度和位置都按照2的幂选取，所以更高效准确


解决局部性
解决时频分析

#### 多分辨分析 MultiResolution Analysis

#### Filter Bank 滤波组
对信号进行小波分解，得到低频部分和高频部分
下2采样，分为两半， $O(Nlog_{2}{N})$




#### 父小波 母小波
任何小波变换的基函数，其实就是对母小波和父小波缩放和平移的集合

![[Pasted image 20230513113606.png]]

#### Sampling
upsampling: 时间序列从低频到高频（每月到每天）重新采样
downsampling: 时间序列从高频重新采样到低频（每周一次到每月一次）

频谱： frequency-amplitude 的二维平面
上采样：过采样/信号插值，频谱压缩
下采样：欠采样/信号抽取，频谱扩展

### References:
[小波变换（wavelet transform）的通俗解释](https://www.cnblogs.com/jfdwd/p/9249850.html)



## 马尔可夫过程