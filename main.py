import base64
from io import BytesIO
from flask import Flask, jsonify, request, render_template, send_file
from init_database import Post_data,app,db



# webhook发送的json转为字典可能存在的键
# 此外event字段一定存在，不再考虑
possible_fields = ['result', 'timestamp', 'message', 'screenshot']


def save_data(dict_list: dict):
    record = Post_data(event=dict_list['event'])
    for field in possible_fields:
        setattr(record, field, dict_list.get(field))  # 如果字段不存在则默认为 None
    db.session.add(record)
    db.session.commit()


@app.route('/', methods=['POST'])
def main():
    # 从bettergi的webhook接收数据
    try:
        save_data(request.json)
    except Exception as e:
        print(e)
        return jsonify({'msg': 'error'})
    return jsonify({'msg': 'OK'})


@app.route('/', methods=['GET'])
def page():
    # 网页展示端，外部展示可能需要配置内网穿透。注意风险。
    posts = Post_data.query.order_by(Post_data.create_time.desc()).limit(10).all()
    if posts:
        min_id = min(post.id for post in posts)  # 找到这批记录中最小的id
    else:
        min_id = 0
    return render_template('base.html', data=posts, last_id=min_id)


@app.route('/image/<image_id>')
def serve_image(image_id):
    # 从数据库中查询图片
    FilterData = Post_data.query.get(image_id)
    if FilterData is None:
        return 'Image not found', 404
    image_data = FilterData.screenshot
    # 解码Base64字符串为二进制数据
    binary_data = base64.b64decode(image_data)
    # 创建BytesIO对象并将二进制数据写入其中
    img_io = BytesIO(binary_data)
    # 返回图片数据作为响应
    return send_file(img_io, mimetype='image/png')


@app.after_request
def add_header(response):
    # 如果你只想对GET请求生效，可以加个判断
    if request.method == 'GET':
        response.cache_control.public = True
        response.cache_control.max_age = 86400  # 缓存1天
    return response


if __name__ == '__main__':
    app.run(debug=True, port=222)
