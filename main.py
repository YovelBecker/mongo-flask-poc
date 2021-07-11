from flask import Flask, json, request, Response
from MongoDB import MongoAPI

app = Flask(__name__)

mongo_config = {
    "database": "test_db",
    "collection": "users"
}
mongo = MongoAPI(mongo_config)


@app.route('/')
def base():
    return Response(
        response=json.dumps({"Status": "UP"}),
        status=200,
        mimetype='application/json')


@app.route('/user', methods=['GET'])
def query():
    res = mongo.read()
    res_json = json.dumps(res)
    return Response(
        response=res_json,
        status=200,
        mimetype='application/json')

@app.route('/user', methods=['POST'])
def add():
    body = request.json
    print(body)
    res = mongo.write(body)
    res_json = json.dumps(res)
    return Response(
        response=res_json,
        status=200,
        mimetype='application/json')

@app.route('/user', methods=['PUT'])
def update():
    username = request.args['name']
    new_user = request.json
    res = mongo.update(username, new_user)
    res_json = json.dumps(res)
    return Response(
        response=res_json,
        status=200,
        mimetype='application/json')

@app.route('/user', methods=['DELETE'])
def remove():
    username = request.args['name']
    res = mongo.delete(username)
    res_json = json.dumps(res)
    return Response(
        response=res_json,
        status=200,
        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
