"""
查询处理器
"""
from typing import List, Dict
from rag_system.retriever import Retriever


class QueryProcessor:
    """查询处理器类"""
    
    def __init__(self, retriever: Retriever = None):
        self.retriever = retriever or Retriever()
    
    def process_query(self, query: str, top_k: int = None) -> Dict:
        """
        处理查询
        
        Args:
            query: 查询文本
            top_k: 返回top-k个结果
            
        Returns:
            处理结果，包含相关文档和查询信息
        """
        # 检索相关文档
        relevant_docs = self.retriever.retrieve(query, top_k=top_k)
        
        return {
            "query": query,
            "relevant_docs": relevant_docs,
            "doc_count": len(relevant_docs)
        }
