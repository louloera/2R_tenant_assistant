
# @home_bp.route('/<home_id>', methods=['DELETE'])
# def delete_host(home_id):
#     home = validate_id(Home,home_id)
#     home_name = home.name
#     db.session.delete(home)
#     db.session.commit()
#     return {'details': f'Home {home_id} "{home_name}" successfully deleted'}, 200