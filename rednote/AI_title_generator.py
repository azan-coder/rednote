import os
import requests
from abc import ABC, abstractmethod
from typing import List

class TitleGenerator(ABC):
    """标题生成器的抽象基类"""
    @abstractmethod
    def generate(self, keywords: str) -> List[str]:
        pass

class SiliconFlowTitleGenerator(TitleGenerator):
    """使用Silicon Flow的标题生成器"""
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('SILICON_API_KEY')
        self.base_url = "https://api.siliconflow.cn/v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    def generate(self, keywords: str) -> List[str]:
        data = {
            "model": "Qwen/Qwen2.5-7B-Instruct",  # Silicon Flow的模型
            "messages": [{
                "role": "user",
                "content": f"请生成5个包含'{keywords}'的小红书爆款标题，要求：\n"
                          f"1. 每个标题都要包含emoji\n"
                          f"2. 标题要吸引人点击\n"
                          f"3. 每行输出一个标题\n"
                          f"4. 不要包含序号"
            }]
        }
        
        response = self.session.post(f"{self.base_url}/chat/completions", json=data)
        if response.status_code == 200:
            result = response.json()
            titles = result['choices'][0]['message']['content'].strip().split('\n')
            return titles
        else:
            raise Exception(f"API调用失败：{response.text}")

def create_title_generator(provider: str = "siliconflow", **kwargs) -> TitleGenerator:
    """工厂函数：创建标题生成器实例"""
    generators = {
        "siliconflow": SiliconFlowTitleGenerator,
    }
    
    if provider not in generators:
        raise ValueError(f"不支持的AI提供商: {provider}")
    
    return generators[provider](**kwargs) 