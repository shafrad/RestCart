from flask import Flask, jsonify, json, request, abort

from app import data

from collections import Counter


app = Flask(__name__)

@app.route("/list")
def hello():
    
    #print(request.method)
    return jsonify(data)
    #return render_template('templates/data/datas.html',
    #                       datas=datas, title="Descriptions")

@app.route('/list/<int:list_id>', methods=['GET'])
def helloid(list_id):
    
    id = [id for id in data if id['id'] == list_id]
    if len(id) == 0:
        abort(404)
    return jsonify({'id': id[0]})

@app.route('/add', methods=['POST'])
def addData():
    
    # menambahkan data Todo
    #newTodo = request.json
    #print (request.method)
    if not request.json or not 'description' in request.json:
        abort(400)
    if not request.json or not 'price' in request.json:
        abort(400)
    if not request.json or not 'category' in request.json:
        abort(400)
    if not request.json or not 'qty' in request.json:
        abort(400)
    if not request.json or not 'totalPrice' in request.json:
        abort(400)
    #if item in data:
    newTodo = {
        'id': data[-1]['id'] + 1,
        'description': request.json.get('description', ""),
        'price': request.json.get('price', ""),
        'category': request.json.get('category', ""),
        #if item in data:
        'qty': data[-1]['qty'] + 1,
        #request.json.get('qty', ""),
        'totalPrice': data[-1]['totalPrice'] + data[0]['price']
        #request.json.get('totalPrice', "")
    }
    data.append(newTodo)
    return jsonify({'newTodo': newTodo}), 201

@app.route('/edit/<int:list_id>', methods=['PUT'])
def editData(list_id):
    
    id = [id for id in data if id['id'] == list_id]
    if len(id) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not str:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not str:
        abort(400)
    if 'totalPrice' in request.json and type(request.json['totalPrice']) is not str:
        abort(400)
    id[0]['description'] = request.json.get('description', id[0]['description'])
    id[0]['price'] = request.json.get('price', id[0]['price'])
    id[0]['category'] = request.json.get('category', id[0]['category'])
    id[0]['totalPrice'] = request.json.get('totalPrice', id[0]['totalPrice'])
    return jsonify({'id': id[0]})

@app.route('/delete/<int:list_id>', methods=['DELETE'])
def deleteData(list_id):
    id = [id for id in data if id['id'] == list_id]
    if len(id) == 0:
        abort(404)
    data.remove(id[0])
    return jsonify({'result': True})