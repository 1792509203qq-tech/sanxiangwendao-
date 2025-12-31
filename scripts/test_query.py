#!/usr/bin/env python3
"""
测试查询脚本
"""
import os
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag_system.rag_chain import RAGChain


def test_query():
    """测试查询"""
    print("初始化RAG链...")
    rag = RAGChain()
    
    # 测试查询
    query = "什么是认知内共生理论？"
    print(f"查询: {query}")
    
    result = rag.generate_response(query)
    print(f"回答: {result['answer']}")
    print(f"来源: {result['sources']}")


if __name__ == "__main__":
    test_query()
