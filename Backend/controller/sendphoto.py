from flask import Blueprint, request, jsonify
from s3_config import s3, BUCKET_NAME
from model.wallpaper import wallpaper

sendphoto_bp = Blueprint('sendphoto', __name__)

@sendphoto_bp.route('/api/sendphoto', methods=['POST'])
def send_photo():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    wallpaper = wallpaper(filename=file.filename, content_type=file.content_type)

    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        wallpaper.s3_key,
        ExtraArgs={"ContentType": file.content_type}
    )

    return jsonify({
        "message": "File uploaded successfully",
        "file_url": wallpaper.url
    }), 200