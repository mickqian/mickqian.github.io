
---
title : ''
summary : 'Summary of this thesis'
tags : [""]
author : ["Mick"]
draft : true
---


metric: 
* perplexity
* downstream accuracy

### 准备步骤

* vector store, index:  embedded vector -> index 的倒排索引
	* 为了控制取出文档的大小和精准性，需要做文本切分
		* split by char
		* MarkdownHeader
		* HTMLHeaderText
		* Program Analysis to extract the semantics
* retrieval: (可能涉及 rerank)
	* metric: nDCG@3/ lexical search score + semantic search score
	* 算法：convex combination > **RRF**(Hybrid search, 只考虑排序位置，忽略排序中数据对应的分数) > bm25 > knn
	* convex combination: 两个不同检索方式得到的召回数据，分数范围不一致，因此需要统一的分数评价体系
		* scaling: standard, min_max
* LLM:
	* 方式： concatenation / post-fusion： 生成多个回答，选一个 / concat + PF： 最可靠
		* K 轮 问答 * (1 次 K 篇 文档）
* retrieval: optional

## **pipeline**

1. 给定输入x
	1. 可能有 pre process:  口语化过滤，生成多个 queries
2. 以 x 为输入，对知识库检索，得到候选 topk Zi
3. 拼接x，Z * i (s)，得到输入序列
4. 送入encoder，得到输出(s)
	1. 如果得到多个输出，送入answer pool 进行排序


## How to retrieve

### Retriever train

训练 retriever，损失函数可以为 选中期望目标 的概率


## When to retrieve

* once
* every n token
* every token
* me


1. 分割为等长的窗口，分别retrieve 并拼接，提高效果



## What to retrieve
 * tokends
 * entities or 
 * 语义 paragraphs(markdown headings)



## How to use?


作用于 LLM 的：
* input layer: 拼接为对 LLM 的输入
* intermediate layers: Retrieval-encoder 能够对取出的 neighbours 进行编码，并送回transformer, help to generate
* output layer: 每次生成单个token后， 结合 LLM 和 knn 的概率，对索引进行质量排序



## Conclusion

* database 和 模型越大，效果越好
* 频繁的检索效果更好，但性能差