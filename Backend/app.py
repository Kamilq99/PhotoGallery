from flask import Flask
from config import init_elastic_config, init_elastic_index, s3_check_connection, list_s3_buckets
from controller.uploadphoto import uploadphoto


app = Flask(__name__)

# Initialize S3 configuration and buckets
s3_check_connection(app)
list_s3_buckets(app)

# Initialize Elasticsearch configuration and index
init_elastic_config(app)
init_elastic_index(app, 'photo_metadata')

# Register blueprints
app.register_blueprint(uploadphoto)

if __name__ == '__main__':
    app.run(debug=True, port=5000)