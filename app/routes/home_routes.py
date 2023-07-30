from flask import Blueprint, jsonify, abort, make_response,request
from app import db 
from app.models.home import Home


home_bp = Blueprint ("home", __name__, url_prefix="/home")

# @home_bp.route('', methods=['POST'])
# # @cross_origin()
# def create_board():
#     request_body = request.get_json()
#     valid_request = valid.validate_entry(Board, request_body)

#     new_board = Board.from_dict(valid_request)
    
#     db.session.add(new_board)
#     db.session.commit()
#     return jsonify(new_board.to_dict()), 201