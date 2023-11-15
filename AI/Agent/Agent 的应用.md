
### Key Introduction points

* Multi-Agent Architecture
	* SOP: Standard Operating Procedural
	* multi, to maximum the model ability
* In IDE: full aware of the intention, automation & autonomous
	* Sensory Engine: collect user actions in every way
	* Intention: guess the potential intention of the user( debug, jump to sources, build/run/deploy, profile)
	* Workflow/Chain: Routine automation
		* COI: framework in Rust/TS/WASM to support effectively setup LLM workflow with code or DSL
	* POCs: git msg summarize/auto bugfixing/creating project directory/fix bug and show in a diff editor
	* RAG
		* 基于更多信息/减少幻觉/提升生产力和内容质量
		* knowledge: chunked codebase
		* search: hybrid(lexical, semantical)
		* 

## IDE

## 文件树

1. 外部数据库 或 模型参数中 保存有流行项目 文件夹的配置
2. 返回后，将配置解析为 in-memory tree
3. 递归调用 sandbox 的 terminal， 执行 mkdir/ touch 等指令，完成项目的创建