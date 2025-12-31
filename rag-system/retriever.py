"""
混合检索器
"""
from typing import List, Dict
from rag_system.vector_store import VectorStore
from rag_system.embedding import EmbeddingModel
from rag_system.config import TOP_K, SIMILARITY_THRESHOLD


class Retriever:
    """混合检索器类"""
    
    def __init__(self, vector_store: VectorStore = None, embedding_model: EmbeddingModel = None):
        self.vector_store = vector_store or VectorStore()
        self.embedding_model = embedding_model or EmbeddingModel()
    
    def retrieve(self, query: str, top_k: int = None) -> List[Dict]:
        """
        检索相关文档
        
        Args:
            query: 查询文本
            top_k: 返回top-k个结果
            
        Returns:
            相关文档列表
        """
        top_k = top_k or TOP_K
        
        # 1. 将查询转换为向量
        query_embedding = self.embedding_model.embed_query(query)
        
        # 2. 向量检索
        results = self.vector_store.search(query_embedding, top_k=top_k)
        
        # 3. 过滤低相似度结果
        filtered_results = [
            r for r in results
            if r.get("distance") is None or (1 - r["distance"]) >= SIMILARITY_THRESHOLD
        ]
        
        return filtered_results
