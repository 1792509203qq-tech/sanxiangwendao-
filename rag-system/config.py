"""
RAG系统配置文件
"""
import os
from typing import Dict, Any

# 基础配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "01-dao")

# Embedding配置
EMBEDDING_MODEL = "text-embedding-3-small"  # 或 "text-embedding-3-large"
EMBEDDING_DIMENSION = 1536  # text-embedding-3-small的维度

# 向量数据库配置
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_db")
VECTOR_DB_COLLECTION = "sanxiangwendao"

# 检索配置
TOP_K = 5  # 默认检索top-k个文档块
SIMILARITY_THRESHOLD = 0.7  # 相似度阈值

# RAG配置
RAG_CONFIG: Dict[str, Any] = {
    "chunk_size": 1000,  # 文档块大小
    "chunk_overlap": 200,  # 文档块重叠
    "enable_rerank": True,  # 是否启用重排序
    "rerank_top_k": 3,  # 重排序后的top-k
}

# LLM配置
LLM_MODEL = "gpt-4o-mini"  # 或 "gpt-4o"
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 2000
