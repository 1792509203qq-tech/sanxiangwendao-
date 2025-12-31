#!/usr/bin/env python3
"""
增量更新索引脚本
"""
import os
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag_system.document_loader import DocumentLoader
from rag_system.embedding import EmbeddingModel
from rag_system.vector_store import VectorStore


def update_index():
    """增量更新索引"""
    print("开始更新索引...")
    
    # 初始化组件
    loader = DocumentLoader()
    embedding_model = EmbeddingModel()
    vector_store = VectorStore()
    
    # 这里可以添加增量更新逻辑
    # 例如：只处理最近修改的文件
    
    print("索引更新完成！")


if __name__ == "__main__":
    update_index()
