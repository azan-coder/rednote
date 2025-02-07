from flask import Flask, render_template, request, jsonify
from AI_title_generator import create_title_generator
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 添加调试信息
print("当前工作目录:", os.getcwd())
print("模板目录:", app.template_folder)
print("静态文件目录:", app.static_folder)

# 从环境变量获取API密钥
API_KEY = os.getenv('SILICON_API_KEY')
if not API_KEY:
    raise ValueError("未设置 SILICON_API_KEY 环境变量")

# 添加错误处理
try:
    generator = create_title_generator("siliconflow", api_key=API_KEY)
except Exception as e:
    print(f"初始化生成器失败: {str(e)}")
    raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_titles():
    try:
        keywords = request.json.get('keywords', '')
        if not keywords:
            return jsonify({'error': '请输入关键词'}), 400
        
        # 添加长度限制
        if len(keywords) > 100:
            return jsonify({'error': '关键词太长'}), 400
            
        titles = generator.generate(keywords)
        return jsonify({'titles': titles})
    except Exception as e:
        print(f"生成标题失败: {str(e)}")  # 添加日志
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
