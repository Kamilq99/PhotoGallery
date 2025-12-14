from flask import Blueprint, request, jsonify
from model.metadata import metadata

description_bp = Blueprint('description', __name__)

@description_bp.route('/api/description', methods=['POST'])
def description():
    data = request.get_json()
    photo_id = data.get('photo_id')
    
    if not photo_id:
        return jsonify({'error': 'photo_id is required'}), 400
    
    desc = metadata.get_description(photo_id)
    
    if desc is None:
        return jsonify({'error': 'Description not found'}), 404
    
    return jsonify({'photo_id': photo_id, 'description': desc}), 200