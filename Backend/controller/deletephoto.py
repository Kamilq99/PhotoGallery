from flask import Blueprint, request, jsonify
from model.wallpaper import wallpaper
from s3_config import s3, BUCKET_NAME

deletephoto_bp = Blueprint('deletephoto', __name__)

@deletephoto_bp.route('/api/deletephoto', methods=['POST'])
def delete_photo():
    data = request.get_json()
    photo_id = data.get('photo_id')
    
    if not photo_id:
        return jsonify({'error': 'photo_id is required'}), 400
    
    wp = wallpaper.get_by_id(photo_id)
    
    if wp is None:
        return jsonify({'error': 'Photo not found'}), 404
    
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=wp.s3_key)
        wallpaper.delete_by_id(photo_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'message': 'Photo deleted successfully'}), 200