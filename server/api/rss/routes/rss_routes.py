from flask import Blueprint, jsonify, request
from ..controller import rss_controller as rss
import json

rss_api = Blueprint('rss_api', __name__)


# Gets random set of RSS articles
# Optional: Limit = Number returned (default 30)
@rss_api.route('/api/rss/articles', methods=['GET'])
def get_rss_articles():
    limit = request.args.get('limit', '30')
    if not limit.isdigit():
        return jsonify("Improper limit format!!")
    return jsonify(rss.get_articles(int(limit)))
