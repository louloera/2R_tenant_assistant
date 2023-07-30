from flask import Blueprint, jsonify, abort, make_response,request
from app import db 
from app.models.home import Home
from app.valid import validate_id, validate_entry


home_bp = Blueprint ("home", __name__, url_prefix="/home")


@home_bp.route('/<home_id>', methods=['GET'])
def get_home(home_id):
    home = validate_id(Home,home_id)
    home_response = home.to_dict()
    return jsonify(home_response), 200


@home_bp.route('', methods=['GET'])
def get_homes():
    homes = Home.query.all()
    home_response = [home.to_dict() for home in homes]
    return jsonify(home_response), 200


@home_bp.route('/<home_id>', methods=['DELETE'])
def delete_host(home_id):
    home = validate_id(Home,home_id)
    home_name = home.name
    db.session.delete(home)
    db.session.commit()
    return {'details': f'Home {home_id} "{home_name}" successfully deleted'}, 200