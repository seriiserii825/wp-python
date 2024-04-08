import json
import os


def getWpPosts():
    json_posts = os.popen("wp post-type list --publicly_queryable=1 --fields=name --format=json").read()
    data = json.loads(json_posts)
    posts = []
    for post in data:
        post_name = post['name']
        posts.append(post_name)
    return posts

