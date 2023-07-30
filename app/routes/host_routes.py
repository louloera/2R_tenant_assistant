from flask import Blueprint, jsonify, abort, make_response,request
from app import db 
from app.models.host import Host
from app.models.home import Home
from app.valid import validate_id, validate_entry
import datetime

host_bp = Blueprint ("host", __name__, url_prefix="/host")



@host_bp.route('', methods=['POST'])
# @cross_origin()
def create_host():
    request_body = request.get_json()
    valid_request = validate_entry(Host, request_body)
    

    new_host = Host.from_dict(valid_request)
    # new_host.initiation_date= datetime.datetime.utcnow()
    db.session.add(new_host)
    db.session.commit()
    return jsonify(new_host.to_dict()), 201



@host_bp.route('', methods=['GET'])
def get_hosts():

    hosts = Host.query.all()
    
    host_response = [host.to_dict() for host in hosts]
    return jsonify(host_response), 200


@host_bp.route('/<host_id>', methods=['GET'])
def get_host(host_id):

    host = validate_id(Host,host_id)
    
    host_response = host.to_dict()
    return jsonify(host_response), 200


@host_bp.route('/<host_id>', methods=['DELETE'])
def delete_host(host_id):
    host = validate_id(Host,host_id)
    
    host_username = host.username
    
    db.session.delete(host)
    db.session.commit()
    return {'details': f'Host {host_id} "{host_username}" successfully deleted'}, 200


@host_bp.route('/<host_id>/homes', methods=['POST'])
# @cross_origin()
def post_home_to_specific_host(host_id):
    
    host =validate_id(Host, host_id)
    request_body = request.get_json()
    
    valid_request = validate_entry(Home, request_body)
    new_home = Home.from_dict(valid_request)
    new_home.host_id = host_id
    
    db.session.add(new_home)
    db.session.commit()

    return (new_home.to_dict()), 200