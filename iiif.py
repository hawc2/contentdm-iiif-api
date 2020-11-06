from flask import Flask, session, redirect
from flask_iiif import IIIF

app = Flask("myapp")
ext = IIIF(app=app)

from flask_restful import Api
api = Api(app=app)
ext.init_restful(api)

from flask import current_app, Blueprint
from flask_iiif.api import MultimediaImage

@blueprint.route('/serve/<string:uuid>/<string:size>')
def serve_thumbnail(uuid, size):
    \"\"\"Serve the image thumbnail.

    :param uuid: The document uuid.
    :param size: The desired image size.
    \"\"\"
    # Initialize the image with the uuid
    path = current_app.extensions['iiif'].uuid_to_path(uuid)
    image = IIIFImageAPIWrapper.from_file(path)
    # Resize it
    image.resize(size)
    # Serve it
    return send_file(image.serve(), mimetype='image/jpeg')
