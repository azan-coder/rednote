# 小红书内容生成器

一个基于 AI 的小红书内容生成工具，可以生成标题和封面图片。

## 功能特点

- 🎯 生成小红书风格的标题
- 💡 简洁的用户界面
- 🚀 快速响应

## 技术栈

- 后端：Python + Flask
- 前端：HTML + CSS + JavaScript
- AI API：Silicon Flow

## 安装说明

1. 安装依赖：

pip install flask requests

2. 配置 API 密钥：
- 获取 Silicon Flow API 密钥
- 在 `app.py` 中设置 API_KEY

3. 运行应用：

python app.py

4. 访问网址：

http://127.0.0.1:5000

## 目录结构

rednote/
├── app.py # Flask 应用主文件
├── AI_title_generator.py # 标题生成器核心代码
├── requirements.txt # 项目依赖
├── vercel.json # Vercel 配置
├── .env.example # 环境变量示例
├── .gitignore # Git 忽略文件
├── static/ # 静态文件目录
│ └── style.css
└── templates/ # 模板目录
└── index.html



## 使用说明

### 生成标题
1. 在输入框中输入关键词（如：减肥、穿搭、美食）
2. 点击"生成标题"按钮
3. 等待几秒钟，系统会生成多个标题供选择


## 注意事项

- 确保 API 密钥正确设置
- 生成的内容仅供参考，建议进行适当修改

## 版本历史

- v1.0.0 (2025-02-07)
  - 实现基础标题生成功能

## 维护者

- [azan]