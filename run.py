import re
from main import app
import os
import subprocess
file_cache = 'client.txt'
first = True
if os.path.exists(file_cache):
    first = False
if first:
    print('检测到第一次运行。正在配置环境。')
    # 使用 subprocess.run 执行命令
    command = re.split(' ','pip install -r r.txt')
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print('正在初始化数据库。')
    command = re.split(' ','python python init_database.py')
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    with open('client.txt','w') as e:
        e.write('finished.')
    print('正在尝试启动服务。')
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('0.0.0.0', 222), app)
    version = "0.40"
    m = f"""
    BetterGI 前端展示页（适用于bettergi {version} 版本）
    =================
    在 http://127.0.0.1:222/ 以查看。
    =================
    """
    print(m)
    print('服务已启动。')
    server.serve_forever()
else:
    print('正在尝试启动服务。')
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('0.0.0.0', 222), app)
    version = "0.40"
    m = f"""
    BetterGI 前端展示页（适用于bettergi {version} 版本）
    =================
    在 http://127.0.0.1:222/ 以查看。
    =================
    """
    print(m)
    print('服务已启动。')
    server.serve_forever()