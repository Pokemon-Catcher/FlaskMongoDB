from app import app
from app import mongo
from flask import jsonify
from flask import request
from flask import abort

@app.route('/', methods=['GET'])
def get_db():
    return jsonify(mongo.db.collection_names()), 200

@app.route('/<collection>', methods=['GET'])
def get_something(collection):
    if not collection in mongo.db.collection_names():
        return "Collection is not found",404
    result = mongo.db[collection].find()
    docs = []
    for doc in result:
        docs.append(str(doc))
    return jsonify(docs), 200
    

@app.route('/<collection>/<id>', methods=['GET'])
def get_something_one(collection, id):
    if not collection in mongo.db.collection_names():
        return "Collection is not found",404
    result = mongo.db[collection].find({'_id':id})
    output=[]
    for r in result:
        output.append(str(r))
    if len(output)==0:
        return "Object is not found", 404
    return jsonify(output), 200 


  

@app.route('/<collection>', methods=['POST'])
def add_something(collection):
    mongo.db[collection].insert(request.json)
    return "Success", 201

@app.route('/<collection>/<id>', methods=['PUT'])
def put_something(collection, id):
    if not collection in mongo.db.list_collection_names():
        return "Collection is not found",404
    result = mongo.db[collection].find({'_id':id})
    output=[]
    for r in result:
        output.append(str(r))
    if len(output)>0:
        mongo.db[collection].update({'_id':id},request.json)
        return "Object has been put", 200 
    else:
        abort(404)

@app.route('/<collection>/<id>', methods=['DELETE'])
def delete_something(collection, id):
    if not collection in mongo.db.list_collection_names():
        return "Collection is not found",404
    result = mongo.db[collection].find({'_id':str(id)})
    output=[]
    for r in result:
        output.append(str(r))
    if len(output)>0:
        mongo.db[collection].remove({'_id':str(id)})
        return "Success", 200 
    else:
        abort(404)