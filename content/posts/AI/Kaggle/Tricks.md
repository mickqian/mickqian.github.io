
---
title : ''
summary : 'Summary of this thesis'
tags : [""]
author : ["Mick"]
draft : true
---


Normalize
Apply one-hot encoding to categorical column

1. Outliers 甄别和去除
2. 补全 Missings
3. 增添 Features
4. 观察，选择和结果相关性较高的feature(for training)
	* object
	* category
		* the categorical titles to ordinal 
		* ![[Pasted image 20230623112408.png]]
	* numeric
		* Age -> AgeBand
		* Fare -> Fare Ordinal

```python
train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False)
```

