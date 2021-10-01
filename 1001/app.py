from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/article', methods=['POST'])
def save_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'comment': comment_receive
    }
    db.article.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '작성 완료'})


@app.route('/article', methods=['GET'])
def get_post():
    articles = list(db.article.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': articles})
    return {"result": "success"}


@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)