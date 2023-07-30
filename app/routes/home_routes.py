from flask import Blueprint, jsonify, abort, make_response,request
from app import db 
from app.models.home import Home
from app.models.trash import Trash
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


@home_bp.route('/<home_id>/trash', methods=['POST'])
# @cross_origin()
def post_trash_to_specific_home(home_id):
    
    trash =validate_id(Trash, home_id)
    request_body = request.get_json()
    
    valid_request = validate_entry(Trash, request_body)
    new_trash = Trash.from_dict(valid_request)
    new_trash.home_id = home_id
    
    db.session.add(new_trash)
    db.session.commit()

    return (new_trash.to_dict()), 200

@home_bp.route('/<home_id>/trash', methods=['GET'])
def get_trah(home_id):

    trash = validate_id(Trash,home_id)
    home_response = trash.to_dict()
    return jsonify(home_response), 200

@home_bp.route('/<home_id>/trash', methods=['DELETE'])
def delete_trash(home_id):
    home = validate_id(Home,home_id)
    trash_id = home.name
    db.session.delete(home)
    db.session.commit()
    return {'details': f'Home {home_id} "{home_name}" successfully deleted'}, 200

