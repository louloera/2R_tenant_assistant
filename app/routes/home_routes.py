from flask import Blueprint, jsonify, abort, make_response,request
from app import db 
from app.models.home import Home
from app.models.trash import Trash
from app.models.towel import Towel
from app.models.item import Item
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


################### TRASH ############################

@home_bp.route('/<home_id>/trash', methods=['POST'])
# @cross_origin()
def post_trash_to_specific_home(home_id):
    home =validate_id(Home, home_id)
    request_body = request.get_json()
    valid_request = validate_entry(Trash, request_body)
    new_trash = Trash.from_dict(valid_request)
    new_trash.home_id = home_id
    db.session.add(new_trash)
    db.session.commit()
    return (new_trash.to_dict()), 200

@home_bp.route('/<home_id>/trash', methods=['GET'])
def get_trash(home_id):
    home = validate_id(Home,home_id)
    trashes =Trash.query.filter(Trash.home_id==home_id)
    for trash in trashes:
        trash_response = trash.to_dict()
    return jsonify(trash_response), 200

@home_bp.route('/<home_id>/trash', methods=['DELETE'])
def delete_trash(home_id):
    home = validate_id(Home,home_id)
    trashes =Trash.query.filter(Trash.home_id==home_id)
    for trash in trashes:
        the_trash = trash.to_dict()
        the_trash = validate_id(Trash, str(the_trash['trash_id']))
    db.session.delete(the_trash)
    db.session.commit()
    return {'details': f'Trash {the_trash.id} successfully deleted'}, 200


################### TOWELS ############################

@home_bp.route('/<home_id>/towels', methods=['POST'])
# @cross_origin()
def post_towels_to_specific_home(home_id):
    home =validate_id(Home, home_id)
    request_body = request.get_json()
    valid_request = validate_entry(Towel, request_body)
    new_towel = Towel.from_dict(valid_request)
    new_towel.home_id = home_id
    db.session.add(new_towel)
    db.session.commit()
    return (new_towel.to_dict()), 200

@home_bp.route('/<home_id>/towels', methods=['GET'])
def get_towel(home_id):
    home = validate_id(Home,home_id)
    towels =Towel.query.filter(Towel.home_id==home_id)
    if towels: 
        for towel in towels:
            towel_response = towel.to_dict()
    else: 
        towel_response= (f'No Towels for {home_id}')
    return jsonify(towel_response), 200

@home_bp.route('/<home_id>/towels', methods=['DELETE'])
def delete_towels(home_id):
    home = validate_id(Home,home_id)
    towels =Towel.query.filter(Towel.home_id==home_id)
    for towel in towels:
        the_towel = towel.to_dict()
        the_towel = validate_id(Towel, str(the_towel['towel_id']))
    db.session.delete(the_towel)
    db.session.commit()
    return {'details': f'Towel {the_towel.id} successfully deleted'}, 200

################### ITEMS ############################

@home_bp.route('/<home_id>/items', methods=['POST'])
# @cross_origin()
def post_items_to_specific_home(home_id):
    home =validate_id(Home, home_id)
    request_body = request.get_json()
    valid_request = validate_entry(Item, request_body)
    new_item = Item.from_dict(valid_request)
    new_item.home_id = home_id
    db.session.add(new_item)
    db.session.commit()
    return (new_item.to_dict()), 200

@home_bp.route('/<home_id>/items', methods=['GET'])
def get_item(home_id):
    home = validate_id(Home,home_id)
    items =Item.query.filter(Item.home_id==home_id)
    if items: 
        for item in items:
            item_response = item.to_dict()
    else: 
        item_response= (f'No Items for {home_id}')
    return jsonify(item_response), 200

@home_bp.route('/<home_id>/items', methods=['DELETE'])
def delete_items(home_id):
    home = validate_id(Home,home_id)
    items =Item.query.filter(Item.home_id==home_id)
    for item in items:
        the_item = item.to_dict()
        the_item = validate_id(Item, str(the_item['item_id']))
    db.session.delete(the_item)
    db.session.commit()
    return {'details': f'Item {the_item.id} successfully deleted'}, 200

