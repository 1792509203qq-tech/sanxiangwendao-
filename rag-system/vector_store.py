"""
向量数据库封装
"""
from typing import List, Dict, Optional
import chromadb
from chromadb.config import Settings
from rag_system.config import VECTOR_DB_PATH, VECTOR_DB_COLLECTION, EMBEDDING_DIMENSION


class VectorStore:
    """向量数据库封装类"""
    
    def __init__(self, db_path: str = None, collection_name: str = None):
        self.db_path = db_path or VECTOR_DB_PATH
        self.collection_name = collection_name or VECTOR_DB_COLLECTION
        
        # 初始化ChromaDB客户端
        self.client = chromadb.PersistentClient(
            path=self.db_path,
            settings=Settings(anonymized_telemetry=False)
        )
        
        # 获取或创建集合
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )
    
    def add_documents(self, documents: List[Dict], embeddings: List[List[float]]):
        """
        添加文档到向量数据库
        
        Args:
            documents: 文档列表，每个文档包含content、metadata等
            embeddings: 文档对应的向量列表
        """
        ids = [f"doc_{i}" for i in range(len(documents))]
        texts = [doc["content"] for doc in documents]
        metadatas = [
            {
                "file_path": doc.get("file_path", ""),
                "file_name": doc.get("file_name", ""),
                "file_type": doc.get("file_type", "markdown")
            }
            for doc in documents
        ]
        
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )
    
    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Dict]:
        """
        搜索相似文档
        
        Args:
            query_embedding: 查询向量
            top_k: 返回top-k个结果
            
        Returns:
            相似文档列表
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        # 格式化结果
        documents = []
        if results['ids'] and len(results['ids']) > 0:
            for i in range(len(results['ids'][0])):
                documents.append({
                    "content": results['documents'][0][i],
                    "metadata": results['metadatas'][0][i],
                    "distance": results['distances'][0][i] if 'distances' in results else None
                })
        
        return documents
    
    def delete_collection(self):
        """删除集合"""
        self.client.delete_collection(name=self.collection_name)
