"""
RAG链实现
"""
from typing import Dict, List
import openai
from rag_system.query_processor import QueryProcessor
from rag_system.config import LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS


class RAGChain:
    """RAG链类"""
    
    def __init__(self, query_processor: QueryProcessor = None):
        self.query_processor = query_processor or QueryProcessor()
    
    def generate_response(self, query: str, top_k: int = None) -> Dict:
        """
        生成回答
        
        Args:
            query: 查询文本
            top_k: 检索top-k个文档
            
        Returns:
            回答字典，包含answer、sources等
        """
        # 1. 检索相关文档
        query_result = self.query_processor.process_query(query, top_k=top_k)
        relevant_docs = query_result["relevant_docs"]
        
        # 2. 构建上下文
        context = "\n\n".join([
            f"文档: {doc['metadata']['file_name']}\n内容: {doc['content']}"
            for doc in relevant_docs
        ])
        
        # 3. 构建提示词
        prompt = f"""基于以下文档内容回答问题：

{context}

问题：{query}

请基于上述文档内容回答问题，如果文档中没有相关信息，请说明。"""
        
        # 4. 调用LLM生成回答
        try:
            response = openai.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {"role": "system", "content": "你是一个知识库助手，基于提供的文档内容回答问题。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=LLM_TEMPERATURE,
                max_tokens=LLM_MAX_TOKENS
            )
            
            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "sources": [doc['metadata'] for doc in relevant_docs],
                "query": query
            }
        except Exception as e:
            raise Exception(f"生成回答失败: {str(e)}")
