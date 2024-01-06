
---
title : ''
summary : 'Summary of this thesis'
tags : [""]
author : ["Mick"]
draft : true
---


Autonomous Agent framework
# AutoGPT
记忆 + 工具

核心: Prompt Loop:

1. 组装 Command Prompt， 传入
2. 得到 Next Step Command
3. 执行 Command
4. 得到 Result，作为 Command Prompt 的元素之一
5. 重复 1

## Command Prompt

### Demand
* Name
* Role
* Goal
* Commands
* Performance Evaluation: 作为提醒
	1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities. 
	2. . Constructively self-criticize your big-picture behavior constantly. 
	3. Reflect on past decisions and strategies to refine your approach. 
	4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.
* Format Regulation: Json

### History: 短期
Chat history


### Memory：长期
backed by vector database



  


## Characteristic
* Data-aware
* Agentic: interact with environment

## Concepts/Prompting techniques
* **Cot** to generate **intermediate** reasoning steps
	* 大语言模型的推理（reasoning）是一种涌现行为，具体指: 只有在引入CoT之后，超过1000亿参数的大模型才能解锁reasoning能力。
* **ReAct**: generate **reasoning** traces + task-specific **actions**


## Emergence ?
* In-Context learning
* long-term memory : fine tune or vector database?

### Demerits:
1. token 开销：history + 迭代次数
2. 不确定，不可控： 提出不切实际的方案，列如选择自己训练模型而不是 ICT
3. 对于复杂任务：陷入循环
4. 固化知识的能力弱

### Commands:
1. git clone, terminal execute(分析依赖，自动安装)
2. 自动根据错误进行修复



# HuggingGPT
ml 社区



# Semantic GPT

# Sparkle of AGI