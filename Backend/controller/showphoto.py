from flask import Blueprint, request, jsonify
from model.image_model import ImageModel

showphoto_bp = Blueprint('showphoto', __name__)

@showphoto_bp.route('/api/showphoto', methods=['GET'])
def show_photo():
    image_id = request.args.get('id')
    if not image_id:
        return jsonify({"error": "Image ID is required"}), 400

    image = ImageModel.get_image_by_id(image_id)
    if not image:
        return jsonify({"error": "Image not found"}), 404

    return jsonify({
        "id": image.id,
        "url": image.url,
        "title": image.title,
        "description": image.description
    }), 200