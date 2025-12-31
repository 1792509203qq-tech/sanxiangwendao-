#!/usr/bin/env python3
"""
构建完整索引脚本
"""
import os
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag_system.document_loader import DocumentLoader
from rag_system.embedding import EmbeddingModel
from rag_system.vector_store import VectorStore


def build_index():
    """构建完整索引"""
    print("开始构建索引...")
    
    # 初始化组件
    loader = DocumentLoader()
    embedding_model = EmbeddingModel()
    vector_store = VectorStore()
    
    # 加载所有文档
    print("加载文档...")
    documents = loader.load_all_documents()
    print(f"共加载 {len(documents)} 个文档")
    
    # 生成向量
    print("生成向量...")
    texts = [doc["content"] for doc in documents]
    embeddings = embedding_model.embed(texts)
    
    # 添加到向量数据库
    print("添加到向量数据库...")
    vector_store.add_documents(documents, embeddings)
    
    print("索引构建完成！")


if __name__ == "__main__":
    build_index()
