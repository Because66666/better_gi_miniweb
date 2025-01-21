from flask import Flask, jsonify, request
import os
import json
from datetime import datetime

app = Flask(__name__)


post_path = r'.\post_load'
if not os.path.exists(post_path):
    os.mkdir(post_path)

def save_post(request_info):
    current_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename = f'{current_time}.txt'
    fullpath = os.path.join(post_path, filename)
    with open(fullpath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(request_info))

@app.route('/', methods=['POST'])
def main():
    request_info = {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'args': dict(request.args),
        'form': dict(request.form),
        'json': request.json if request.is_json else None,
        'data': request.get_data(as_text=True)  # 获取原始数据作为文本
    }

    save_post(request_info)
    return jsonify({'msg': 'OK'})


@app.route('/page', methods=['GET'])
def page():
    return jsonify({'msg': 'OK'})


if __name__ == '__main__':
    app.run(debug=True, port=222)
