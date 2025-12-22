from flask import Blueprint, request, jsonify
from model.photo import photo
from model.photometadata import photometadata
import uuid

ALLOWED_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/jpeg']

uploadphoto = Blueprint('uploadphoto', __name__)

@uploadphoto.route('/uploadphoto', methods=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    content_type = file.content_type
    if content_type not in ALLOWED_CONTENT_TYPES:
        return jsonify({'error': 'Unsupported file type'}), 400

    photo_id = str(uuid.uuid4())
    new_photo = photo(content_type=content_type)
    new_metadata = photometadata(photo_id=photo_id, filename=file.filename, content_type=content_type)

    # Here you would typically save the photo and metadata to your storage and database

    return jsonify({'message': 'Photo uploaded successfully', 'photo_id': photo_id}), 201