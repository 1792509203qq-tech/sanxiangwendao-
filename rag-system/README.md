# RAG System

RAG（Retrieval-Augmented Generation）系统实现，用于知识库的智能问答。

## 功能

- 文档加载和索引
- 向量存储和检索
- 混合检索（向量检索 + 关键词检索）
- RAG链实现

## 使用示例

```python
from rag_system.rag_chain import RAGChain

# 初始化RAG链
rag = RAGChain()

# 查询
result = rag.generate_response("什么是认知内共生理论？")
print(result["answer"])
```
