image -> txt

transformer 应用于 CV 领域
patch : 16 * 16
图片 -> n * n 个 patch

特殊的 positional encoding:
![[Pasted image 20230618151346.png]]
对patch按顺序进行编号，将编号通过查表


转换为 embedding，sum

extra learnable token
