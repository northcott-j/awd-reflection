"""__init__ to setup Flask app and to import API routes"""
import os
from flask import Flask, send_from_directory, send_file
from api.rss.routes.rss_routes import rss_api
from api.goals.routes.goals_routes import goals_api

app = Flask(__name__)
ROOT_PATH = os.path.abspath(os.path.join(app.root_path, '..'))

# Add rss api routes
app.register_blueprint(rss_api)
app.register_blueprint(goals_api)


# Serves all content within the client folder as the root /
@app.route('/<path:path>')
def serve_frontend(path):
    from server import ROOT_PATH
    return send_from_directory(ROOT_PATH + '/client/', path)


@app.errorhandler(404)
def page_not_found(error):
    from server import ROOT_PATH
    return send_file(ROOT_PATH + '/client/' + 'index.html')


# Serves the index file
@app.route('/')
def serve_index():
    from server import ROOT_PATH
    return send_file(ROOT_PATH + '/client/' + 'index.html')
