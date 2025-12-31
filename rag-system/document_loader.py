"""
文档加载器
"""
import os
from typing import List, Dict
from pathlib import Path
import yaml
from rag_system.config import DOCS_DIR


class DocumentLoader:
    """文档加载器类"""
    
    def __init__(self, docs_dir: str = None):
        self.docs_dir = docs_dir or DOCS_DIR
    
    def load_markdown_file(self, file_path: str) -> Dict:
        """
        加载Markdown文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            文档字典，包含content、metadata等
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                "content": content,
                "file_path": file_path,
                "file_name": os.path.basename(file_path),
                "file_type": "markdown"
            }
        except Exception as e:
            raise Exception(f"加载文件失败: {str(e)}")
    
    def load_yaml_index(self, yaml_path: str) -> Dict:
        """
        加载YAML索引文件
        
        Args:
            yaml_path: YAML文件路径
            
        Returns:
            索引字典
        """
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                index_data = yaml.safe_load(f)
            return index_data
        except Exception as e:
            raise Exception(f"加载YAML索引失败: {str(e)}")
    
    def load_all_documents(self) -> List[Dict]:
        """
        加载所有文档
        
        Returns:
            文档列表
        """
        documents = []
        
        # 遍历docs_dir下的所有.md文件
        for root, dirs, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    doc = self.load_markdown_file(file_path)
                    documents.append(doc)
        
        return documents
