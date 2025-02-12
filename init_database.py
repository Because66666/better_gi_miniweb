from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bettergi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post_data(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    event = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.Text, nullable=True)
    screenshot = db.Column(db.Text, nullable=True, default=None)
    create_time = db.Column(db.DateTime, default=datetime.now)
    message = db.Column(db.Text)


def init_db():
    with app.app_context():
        print("Initializing database...")
        db.create_all()
        print("Database initialized.")

def write_json_to_db():
    import os
    import json
    if not os.path.exists('./post_load'):
        return
    with app.app_context():
        for filename in os.listdir('./post_load'):
            file = os.path.join('./post_load', filename)
            with open(file, 'r', encoding='utf-8') as e:
                dict_list = json.loads(e.read())['json']
            possible_fields = ['action', 'conclusion', 'task', 'screenshot']
            record = Post_data(event=dict_list['event'])
            for field in possible_fields:
                setattr(record, field, dict_list.get(field))  # 如果字段不存在则默认为 None
            db.session.add(record)
            db.session.commit()

if __name__ == '__main__':
    init_db()
    write_json_to_db()
