from flask import Flask, request, render_template
import subprocess
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# 存储程序输出的全局变量
program_output = ""

# 定义一个函数，用于实时推送结果到前端
def send_result(result, event):
    socketio.emit(event, result, namespace='/results')

def r2n(x):
    (x)
    return '正在处理......'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None  # 用于存储函数的输出
    model_result = None
    model_result1 = None
    if request.method == 'GET':
        # 处理GET请求的代码
        return render_template('index.html', result=None)
    
    if request.method == 'POST':
        data_from_form = request.form.get('input_field_name')  # 获取表单输入的数据
        # 在这里执行你的Python代码，使用data_from_form作为输入数据
        if request.form.get('转换'):
            try:
                result = r2n(data_from_form)
                send_result(result, 'update_result1')  # 实时推送结果给前端
            except Exception as e:
                result = f"未输入地址"

        if request.form.get('算法执行'):
            try:
                # 要执行的Python脚本文件
                script_to_execute = 'VNet3d.py'

                # 使用subprocess运行另一个Python脚本
                subprocess.run(['python', script_to_execute])
                model_result = '执行完成'
                send_result(model_result, 'update_result2')  # 实时推送结果给前端
            except Exception as e:
                model_result = f"An error occurred: {str(e)}"

        if request.form.get('数据分析'):
            try:
                # 要执行的Python脚本文件
                script_to_execute = 'ConnectSQL.py'

                # 使用subprocess运行另一个Python脚本
                subprocess.run(['python', script_to_execute])
                model_result1 = '分析完成'
                send_result(model_result1, 'update_result3')  # 实时推送结果给前端
            except Exception as e:
                model_result1 = f"An error occurred: {str(e)}"


    # 渲染HTML页面，并将函数的输出(result)传递给页面
    return render_template('index.html', result1=result, result2=model_result, result3=model_result1)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
