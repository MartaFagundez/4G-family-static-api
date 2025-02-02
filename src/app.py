"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    return jsonify(response_body), 200


@app.route("/member", methods=["POST"])
def add_new_member():
    body = request.get_json(silent=True)

    if body is None:
        return jsonify({"msg": "Debes enviar los datos en el body"}), 400
    if 'first_name' not in body:
        return jsonify({"msg": "El campo first_name es obligatorio"}), 400
    if 'age' not in body:
        return jsonify({"msg": "El campo age es obligatorio"}), 400
    if 'lucky_numbers' not in body:
        return jsonify({"msg": "El campo lucky_numbers es obligatorio"}), 400
    
    new_member = body
    return jsonify(jackson_family.add_member(new_member)), 200


@app.route("/member/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = jackson_family.get_member(member_id)

    if member is None:
        return jsonify({"msg": "No se encontró un miembro con el id ingresado"}), 404
    
    return jsonify(member), 200


@app.route("/member/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None: 
        return jsonify({"msg": "No se encontró un miembro con el id ingresado"}), 404
    
    jackson_family.delete_member(member_id)
    
    return jsonify({"done": True}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
