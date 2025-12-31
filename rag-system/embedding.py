"""
Embedding模型封装
"""
from typing import List
import openai
from rag_system.config import EMBEDDING_MODEL, EMBEDDING_DIMENSION


class EmbeddingModel:
    """Embedding模型封装类"""
    
    def __init__(self, model_name: str = None):
        self.model_name = model_name or EMBEDDING_MODEL
        self.dimension = EMBEDDING_DIMENSION
    
    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        将文本列表转换为向量列表
        
        Args:
            texts: 文本列表
            
        Returns:
            向量列表
        """
        try:
            response = openai.embeddings.create(
                model=self.model_name,
                input=texts
            )
            return [item.embedding for item in response.data]
        except Exception as e:
            raise Exception(f"Embedding失败: {str(e)}")
    
    def embed_query(self, query: str) -> List[float]:
        """
        将查询文本转换为向量
        
        Args:
            query: 查询文本
            
        Returns:
            向量
        """
        embeddings = self.embed([query])
        return embeddings[0] if embeddings else []
