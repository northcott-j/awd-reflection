from flask import Blueprint, jsonify, request
from ..controller import goals_controller as goals

goals_api = Blueprint('goals_api', __name__)


# Returns list of Writing Program Learning Goals
@goals_api.route('/api/goals', methods=['GET'])
def get_goals():
    return jsonify(goals.list_goals())


# Gets list of inspiration entries for a goal
@goals_api.route('/api/goals/<goal>', methods=['GET'])
def get_goal_articles(goal):
    return jsonify(goals.get_goal_articles(goal))

