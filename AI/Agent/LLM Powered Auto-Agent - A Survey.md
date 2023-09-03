

> 本文的讨论主要以 *不对 LM 结构和参数进行改造* 为前提，因此对于涉及模型改造的方法会一笔带过


With the fast progress of LM, **agents with LM as controller** has extended the ability of LM, from generating text/stories/reports/essay, to solving comprehensive real-world problems


## Glossary 词汇表



## Introduction 背景介绍

### What is an LM-Powered Agent ? 

> Autonomous Agent(自主代理) 是能够感知环境、在现实世界中执行自主、有目的的行动的系统

针对 Autonomous Agent 的研究可以追溯到 上世纪 90年代。早期的研究只停留于理论阶段，直到最近十年才开始出现基于机器人/自动驾驶的初级 Auto-Agent 实验

最近半年（2023/4 ~ now） Auto-Agent 的[一些实验项目](https://github.com/e2b-dev/awesome-ai-agents)(Auto-GPT, BabyAGI, etc) 突然获得了极大的关注度，最主要的原因是 ChatGPT 等大语言模型能力的迅速提升，使 **将LM作为核心控制器的 Agent** 的能力也随之大幅提高，从而使一些更复杂问题的解决成为可能。一般也称这种能力为 Weak AGI

其中最具有代表性的一些项目有：
* [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT):  基于 External Commands 和 Vector Database 实现的 LM Auto-Agent，更侧重于使用各种外部功能实现更 General 的目标
* [HuggingGPT](https://huggingface.co/spaces/microsoft/HuggingGPT): 更强大的外部工具：多模态、领域专业的AI工具，聚焦于 解决多模态任务
* [chemcrow](https://github.com/ur-whitelab/chemcrow-public)： 侧重于使用化学工具，解决 推理密集型 的化学任务
### How does it work 它是怎么工作的？
以 Auto-GPT 官方提供的 [Demo](https://github.com/Significant-Gravitas/Auto-GPT#-demo-april-16th-2023-) 为例：

**用户提供的任务**：
“介绍 AutoGPT 项目，输出到 autogpt.txt"

**Auto-GPT 的处理**：
将任务分为几个子任务：
1. 使用 Google search API 搜索关键字：“AutoGPT"
2. 针对搜索结果进行分析/归纳
3. 从结果中找到 AutoGPT 的 Github 地址，访问改网址并对项目进行分析，得到总结
4. 调用工具: *Write to File*，将文本保存到名为 autogpt.txt 的文件中


## Agent Overview

![[Pasted image 20230807103751.png | Overview of Agent]]

通常来说，一个以 LM 作为核心的自动代理（至少）具有以下组件：

### 1. Planning 规划

规划模块以具体意图作为原始输入，并结合具体情况（Tools，外部环境等）组成 Prompt，作为 LM 的完整输入。这一步的核心目标：

* 指示 LM 针对指定任务，对任务进行合理分解(Decomposition)，制定可行计划(Sub-plan, Sub-goal)。”可行“的定义是： 可以用于 API 调用，并可以在某个环境下执行
* 指示 LM 对于过去的行为进行 反思(Self-Reflection) 和 反省(Self-Criticism)，减少未来发生类似错误的几率

### 2.  Memory 记忆

由于 LM context window 有限且珍贵，无法容纳所有信息，因此需要维护外部记忆（Memory），以降低幻觉 (Extrinsic) 产生的概率，提升 Agent 的稳定性和输出质量
Memory 按照作用时间，可以分为两类：
* Short-term Memory: 短期记忆，In-Context Learning，直接参与模型生成
* Long-term Memory: 在 Agent 活动期间产生的所有有效信息，都可以被人为保留，并在需要时取出，从而模拟人脑 回忆(recall) 的功能。最终目的是参与到 Short-term Memory

注意所有记忆都需要主动维护，本质上”记忆“的设计还是因为目前模型的 context 限制

### 3. Tool Use 工具使用 ( External Abilities )

LM 本身只能以文本作为输入和输出。如果把输出文字作为调用工具的 指令/代码，就可以使  LM 具有调用外部工具的能力，从而解决更实际的 real-world problems

这些工具的能力包括但不限于：
* 信息检索：web search, vector db search, document search
* 代码执行：code interpreter
* 数学运算能力：calculator
* 文件操作能力：read file, write file, modify file
* misc: calendar...

## Planning

### Task Decomposition 任务分解

Task Decomposition 的目标是把输入任务分解成子任务(Subgoal)

当前实现 Task Decomposition 的方式主要有两类：
1. 使用现成的 Prompt Techniques: Cot, ToT, ReAct 等，指示模型进行”逐步思考“，将大任务分解成中间子任务，从而增加模型处理复杂任务的能力
2. 另一类比较特别的方式：**借助外部规划器**， 使用规划领域的特定语言(PDDL) ，再将结果转为自然语言


由于模型在 Planning 阶段常常会出现偏离主任务/陷入循环等情况，执行过程中应该允许用户介入，进行一些规划方向的调整


### Self-Reflection 自我反省

人类从错误的尝试积累经验，降低后续继续犯错的可能性。这很重要--想象没有标准答案的考试

反省过程对 Agent 处理容易出错的任务也很关键，它允许 Agent 通过纠正错误/完善计划，使能力得到迭代提升

#### ReAct

**ReAct** 除了能让 LM 对 task 进行 decomposition，也含有反省的本质：基于过去行动的结果，对下一步动作进行规划和调整。

ReAct 的模板大致格式为：
```
Thought: ... 
Action: ... 
Observation: ... 
... (Repeated many times)
```

LM 基于此格式进行输出，并以此为输入进行下一步规划

[实验表明](https://arxiv.org/abs/2210.03629) **ReAct** 能显著提升 LM 在 知识密集型任务和决策任务上的表现
#### Reflexicon

**Reflexion** 是一个 基于 ReAct 进行改进的 推理框架。它的创新是：
* 奖励模型：设计了三种生成反馈的方式：
	* 简单二元环境反馈：人工反馈，单元测试 等
	* 预定义的启发式函数：是否得到3次以上重复输出，是否超过30步未能成功
	* Self-Evalution: 基于 LM 的评估，基于 LM 编写的单元测试
  最终，这些反馈都会转换为自然语言的格式，加入 Long-term memory 中
  本质上是一种 强化学习（Reinforcement Learning)
* 具备动态记忆：最终失败的任务在执行期间的记忆有可能是低质量的，因此每次任务重启时，记忆应该被有选择地 **更新**

![[Pasted image 20230811154131.png]]


#### Chain of Hindsight 后验链
* 明确呈现过去的输入-反馈来改进模型的输出，使用 SFT
* 添加正则项避免过拟合
#### Algorithm Distillation 算法蒸馏

![[Pasted image 20230811165235.png]]
* 对比知识蒸馏，算法蒸馏面向 Agent 的决策
* **离线**训练数据的生成：训练 N 个独立的单任务 RL 算法，收集其学习历史作为训练数据，训练一个 序列模型（GPT, RNN, LSTM 等），基于这个序列模型生成动作序列
* 基于 Offline 数据的  Offline Policy Distillation，使用 agent 预测离线数据中的动作，实现策略蒸馏


#### Brief Summary 小结
* 现有 Self-Reflection 方法除了使用 in-context learning, RL 也是一个重要的手段
* Reward 的获取是难点


## Memory
内存（记忆）可以被定义为 信息的获取(acquire)，存储，稍后获取(retrieval) 过程
从这个定义出发，agents 中的记忆模块需要利用好 agents 运行期间产生的信息



> 此处的讨论以不对 LM 本身进行任何改造为前提，因此忽略 Knowledge Enhanced Pretrained Models/Dynamic Memory Networks 等通过知识对模型本身进行增强的方法


### Long-term Memory
长期记忆是 agents 需要关注的部分，因为它负责把合适的信息转为 context，作为输入向 LM 提供

#### RAG

**Retrieval-Augmented Generation (RAG)** 是指从模型外部获取相关数据，并使用这些数据增强模板的上下文，以改善模型的输出，提升 Agent 面对 知识密集型（ knowledge-intensive) 和开放域问答( Open-Domain Question Answering ) 任务的性能

##### 结构
RAG 结构由两部分组成：
* 参数模型：预训练的语言模型
* 非参数记忆：外部知识索引

仅依靠有限的参数部分，大语言模型不足以解决 开放域的 长尾知识，而且知识容易过时

RAG 是目前 Agents 框架中 Long-term Memory 的主流应用形式

![[Pasted image 20230810143456.png | Check out this amazing picture.]]
##### 步骤
1. 构建文档索引：使用 DPR encoders 或其他任意 Embedding 模型, E(passge) - passage 
2. Retrieve: 在推理前，将问题转换为 embedding(E(q))，从倒排索引（向量数据库）中找出与之相似度最高的 k 个文档
3. Inference: 拼接输入问题和检索到的文档，作为完整context
	* 在这一阶段，根据 文档 在生成过程中的参与度，也有两种方式：
		* RAG-Sequence: 对于检索到的 k 个文档，每个文档都和原始输入拼接起来进行一次生成，得到 k 个输出，语言模型对于每个输出序列也会有一个 概率（）。对这 k 个概率进行归一化，选择概率最高的输出序列作为最终输出
		 * RAG-Token: 对于检索到的 k 个文档，同样拼接得到 k 个 context。模型对每个 context 都对下一个 token 产生一个概率分布。从中选出最大的概率对应的token，将其作为下一个 token。得到新token后，重新进行文档检索，如此递归生成所有回答
		 
##### 细节
* 关于 Retrieve，有一些常见变化：
	* What to: Chunk/Token/Self-Defined Unit
	* How to: Input/Intermediate/Output
	* When to: Once/Every N tokens
 What/How/When 都会影响输出效果
 ![[Pasted image 20230815144452.png]]
* 一些实验表明，混合检索（hybrid retrivel)：传统搜索（包括关键字检索） + 基于 embedding 的检索的效果会优于 纯 embedding 搜索
	* 纯 embedding 搜索在 名称/短语/缩写/ID 等情况下效果不佳
* 几种常见的相似度算法有：
	* LSH：局部敏感哈希
	* ANNOY：最近邻投影树，
 分布划分为簇，然后在簇内细化量化，缩小搜索范围
* Metric:
	* cosine
	* 欧几里得距离(L2 Norm)
	* Hamming 距离
	* 点积


### Others
* 以上 RAG 方式能工作的前提都是，对于 query(用户指定的问题），能够找到与其相似的 Passage。这些索引的创建需要时间。如果没有这种 query-passage 的相关性信息，HyDE 提供了另外一种解决方式：
	1. 用户给定 query 和 instruction
	2. **LM 生成假设文档**
	3. Encoder 将假设文档嵌入到隐空间，得到 embedding vector
	4. 使用 embedding vector 和 文档的 embedding 计算内积相似度，找出最相似的文档
 这种方式不需要创建 query-passage，只需要 passage_embedding-passage
 * **Internal Retrieval** 是在缺乏外部知识的情况下，引导 LM 生成有关问题的知识，然后利用这些知识指示 LM 进一步回答
 


> 一点延申想法：
> 这种对人类记忆工作机制的模拟仍然相对粗糙，本质上仍然类似下面会提到的 Tool 使用


> 然而， 来自 OpenAI 的 Jack Rae 和  ilya Sutskever 提出过 Compression for AGI (压缩即智慧)的想法。其基本观念是，对数据的压缩率 与 智能 呈现正相关关系。因此，如果 Agent 对数据的压缩能力越强，它就越为智能，也能完成更困难复杂的任务。
> 从这个角度出发，如果我们要让 LM Powered Agent 处理更复杂的能力，就需要在数据的压缩方面-即记忆的存储和获取-进行更多更细致的设计，让 agent 记住更多信息，更精准地 retrieve 信息


## Tool Use

工具的使用，帮助人类和 LM 完成超出自身能力范围的工作
以简单加法计算为例，LM 的泛化能力有限，很难生成训练数据未覆盖的加法算式结果，所以需要外部工具-计算器-的能力介入
而 Agent 的工作，就是把 LM 的输出路由到最适合的专家模块（路由目标也可以由LM自己决定），并调用专家模块，获取返回数据，决定下一步动作

常见的 LM with Tool 框架：
* ChatGPT Plugins：允许开发人员定制工具 API， 供LM调用
* HuggingGPT: 更强大的外部工具：多模态、domain-specific 的AI工具，聚焦于 解决多模态任务
	![[Pasted image 20230804153636.png]]

### Brief Summary
* 对于可能引入外部信息的工具，需要考虑将其生成的数据合并至 Long-term Memory 中
* 对于可能引入 **大量** 外部信息的工具，由于 context 的限制，需要考虑 Retrieve 的流程，对于信息进行有效提炼


## Case Study

### Auto-GPT

AutoGPT 已经引起了很多关注，它是人类对于 AGI 的一次早期尝试
为了更清晰地解释其原理，以下列出了 Auto-GPT 最重要的 Prompt 部分（[branch stable](ce86a5e6978e19ff11cdfd765f6d402f81885fb3)), 
```
You are {agent_name}, {agent_role}
Your goals are: {user-provided agent_goals}

GOALS:
1. {{user-provided goal 1}} 
2. {{user-provided goal 2}} 
3. ...


Constraints: 
1. ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files. 
2. If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember. 
3. No user assistance 
4. Exclusively use the commands listed in double quotes e.g. "command name" 

Commands: 
1. Google Search: "google", args: "input": "<search>" 
2. Browse Website: "browse_website", args: "url": "<url>", "question": "<what_you_want_to_find_on_website>" 
7. Clone Repository: "clone_repository", args: "repository_url": "<url>", "clone_path": "<directory>" 
8. Write to file: "write_to_file", args: "file": "<file>", "text": "<text>" 
9. Read file: "read_file", args: "file": "<file>" 
10. Append to file: "append_to_file", args: "file": "<file>", "text": "<text>" 11. Delete file: "delete_file", args: "file": "<file>" 
11. Search Files: "search_files", args: "directory": "<directory>" 
12. Analyze Code: "analyze_code", args: "code": "<full_code_string>" 
14. Write Tests: "write_tests", args: "code": "<full_code_string>", "focus": "<list_of_focus_areas>" 
15. Execute Python File: "execute_python_file", args: "file": "<file>" 
16. Generate Image: "generate_image", args: "prompt": "<prompt>" 
17. Send Tweet: "send_tweet", args: "text": "<text>" 
18. Do Nothing: "do_nothing", args: 
19. Task Complete (Shutdown): "task_complete", args: "reason": "<reason>"
20. Toolformer Complete (Shutdown): "task_complete", args: "reason": "<reason>"


Resources:
1. Internet access for searches and information gathering.
2. Long Term memory management.
3. File output.

Performance Evaluation:
1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
2. Constructively self-criticize your big-picture behavior constantly.
3. Reflect on past decisions and strategies to refine your approach.
4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps

Respond with only valid JSON conforming to the following schema: 
{  
  "$schema": "http://json-schema.org/draft-07/schema#",  
  "type": "object",  
  "properties": {  
    "thoughts": {  
      "type": "object",  
      "properties": {  
        "text": {  
          "type": "string",  
          "description": "thoughts"  
        },  
        "reasoning": {  
          "type": "string"  
        },  
        "plan": {  
          "type": "string",  
          "description": "- short bulleted\\n- list that conveys\\n- long-term plan"  
        },  
        "criticism": {  
          "type": "string",  
          "description": "constructive self-criticism"  
        },  
        "speak": {  
          "type": "string",  
          "description": "thoughts summary to say to user"  
        }  
      },  
      "required": [  
        "text",  
        "reasoning",  
        "plan",  
        "criticism",  
        "speak"  
      ],  
      "additionalProperties": false  
    },  
    "command": {  
      "type": "Append to file",  
      "properties": {  
        "name": {  
          "type": "string"  
        },  
        "args": {  
          "type": "object"  
        }  
      },  
      "required": [  
        "name",  
        "args"  
      ],  
      "additionalProperties": false  
    }  
  },  
  "required": [  
    "thoughts",  
    "command"  
  ],  
  "additionalProperties": false  
}

Determine exactly one command to use, and respond using the JSON schema specified previously
```
除了常规部分外，AutoGPT 新增了 Constraints 和 Performance Evaluation 部分



### GPT-Engineer
通过自然语言指定的任务生成代码库
* 类似 CoT, GPT-Engineer 被指示先从小组件开始构建，最终构建完整项目
* 允许在开始前，针对不明确的部分进行提问，要求人类澄清
```
You will read instructions and not carry them out, only seek to clarify them.
Specifically you will first summarise a list of super short bullets of areas that need clarification.
Then you will pick one clarifying question, and wait for an answer from the user.
We are writing {{a Super Mario game in python. MVC components split in separate files. Keyboard control.}}

Summary of areas that need clarification:
	1. Specifics of the Super Mario game (e.g. level design, characters, gameplay mechanics)
	2. Details about the MVC components (e.g. which components are in each file)
	3. Keyboard control implementation (e.g. which keys to use, how to handle input)

```



## Challenges & Drawbacks

以上展示的 Agent 有一些常见的限制：

* token 消耗：每次调用都需要 系统 prompt，长度为 1k+
* long term plannning and plan decomposition: 
	* 当涉及一些较为复杂的任务时，在不对该领域知识有较为深入的了解的情况下进行任务规划和分解是很困难的，LM 常常会陷入自循环，或偏离主要方向的困境中
* 错误处理和反思：
	* 相对人类的反复学习/试错/总结过程，LM 在应对未知错误时的反思能力较差
* Absense of common sense:  任何超出 LM 能力范围的任务，哪怕与 LM 本身具有的能力重叠程度较大，Agent 也会走一套繁琐耗时的流程来进行学习
* Memory Recall: 
	* 相较于大脑的复杂结构（复杂网络，图），向量数据库的信息存储方式（树，哈希等简单索引）和检索能力（树搜索，hash，内积相似度计算等方式）都过于简单，导致记忆功能的精度不足。而类比记忆对类人智能的重要性，长期记忆功能的羸弱也限制了 Agent 的能力

Agent 产品化过程中有一些阻碍：
1. 


## IDE  内的应用

在 IDE 领域，针对以上三个部分，可以通过一些调整来使 Agent 更擅长处理 IDE 的 任务：
* Planning: 
	* 对于具有一定经验的开发者，会有属于自己的 workflow。可以考虑将这些 workflow 以 shots 的形式提供给 LM，使其在规划阶段能够参考这些 best practices，从而增强 Planning 能力
	* 需要将 IDE 内部功能进行整理，以工具/tool function 的方式提供给 LM
	* 奖励的设置：Intrinsic reward(奖励新奇性)
* Memory:
	 * 由于现代 IDE 的功能繁多，在使用过程中的记忆来源也较为复杂。每一次在 IDE 内部的操作都可能涉及很多长期记忆，因此长期记忆需要额外设计
* Tool:
	*  我们设想一下一个具有一定经验的软件开发者需要具备的基础知识：
		* Coding: 一种或多种语言的 需求开发，单元测试
		* Document: 编写技术文档
		* Debug: 针对异常/缺陷，结合运行情况进行 debug
	* 针对以上基础知识需求，除了实现与功能相关性较高的工具，还可以将这些领域知识以 Fine-Tune 的方式注入到模型内部

## Improvements

1. LM Powered Auto-Agent 所做的事情是  [Cognitive Architecture](https://cogarch.ict.usc.edu/) 的相关研究 的子集。相对他们的研究，LM Agent 在以下方面有挖掘空间：
	* 奖励机制：当效果符合预期时进行正反馈，当效果不符合预期时进行惩罚和反思
	* 学习进化：持续提升 LM 能力
		* 记忆中的数据大多与领域相关，可以考虑将其作为训练数据，对 LM 进行 fine-tune
2. 参考 [Toolformer](https://github.com/lucidrains/toolformer-pytorch),  Agent 作为具有一定能力的主体，可以自行创造工具，以更好地应对领域相关的不常见需求（例如 IDE 内部的工作流）
	* Toolformer 中尚未实现的 **链式工具调用** 和 **交互式工具构建** 也是两个值得探索的方向
1. Human as Tool: Agent 利用 tool 的能力有限，可以考虑人类介入的方式，把人类作为一种 Tool 使用，在 agent 遇到无法解决的领域问题时向人类寻求帮助
2. MultiAgent: 如果单个 Agent 被赋予太多任务(Context 中包含太多内容)，那么整体质量会显著下降。有必要把复杂任务细分给每个独立的 Agent Role，多个 Agent 协同合作（Environment Detector Agent)
3. ~~Retrieval Enhanced Transformer~~
## References

1. [LM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
2. [Compression for AGI](https://www.youtube.com/watch?v=dO4TPJkeaaU)
3. [Scratchpads](https://arxiv.org/pdf/2112.00114.pdf)
4. [LM-patterns](https://eugeneyan.com/writing/LM-patterns/#retrieval-augmented-generation-to-add-knowledge)
5. [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://arxiv.org/abs/2212.10496)
6. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
7. [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
8. [Augmented Language Models: a Survey](https://arxiv.org/abs/2302.07842)
9. [Retrieval-based Language Models and Applications](https://acl2023-retrieval-lm.github.io)
10. [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
11. [Exploration Strategies in Deep Reinforcement Learning](https://lilianweng.github.io/posts/2020-06-07-exploration-drl/)
