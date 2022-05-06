# C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts
# python -m pip install flask
# 환경변수 설정안했을때 python -m 스크립트 폴더에 들어갈 수 있게 해준다.

from flask import Flask, request, jsonify
import member_dao as dao

flask = Flask(__name__)


@flask.route("/my-member")
def list():

    return jsonify(dao.select_all())


@flask.route("/my-member/<id>")
def detail(id):

    return jsonify(dao.select_one(id=id))  # **data


@flask.route("/my-member/<id>", methods=['DELETE'])
def delete(id):
    return dao.delete_one(id=id)


@flask.route("/my-member/<id>", methods=['PUT'])
def update(id):
    # data = request.data # x-www-form-urlencoded
    data = request.get_json()  # application/json

    return dao.update_one(id=id, username=data["username"], password=data["password"])


@flask.route("/my-member", methods=['POST'])
def save():
    data = request.get_json()
    return dao.insert_one(username=data["username"], password=data["password"])


flask.run(
    host="0.0.0.0",  # 모두가 접근 가능
    port=5000,
    debug=True  # 이 부분이 설정되면 파일 저장시 서버 자동 리로드 된다.
)
