import os
from flask_blog.models import User, Post
import json
from flask_blog import db

# print('current working directory: ', os.getcwd())

with open('test_files/demo_posts.json') as json_posts:
    data = json.load(json_posts)
    for i in data:
        post = Post(title=i['title'], content=i['content'], user_id=i['user_id'])
        print(post)
        db.session.add(post)
        db.session.commit()