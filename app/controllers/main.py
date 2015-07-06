from flask import request, abort, make_response, jsonify, Blueprint
import logging
from flask_restful import reqparse, abort
from app.models import User

logger = logging.getLogger(__name__)
main = Blueprint('main', __name__)

parser = reqparse.RequestParser()
parser.add_argument('user', type=str)
parser.add_argument('pass', type=str)


@main.route('/', methods=['GET', 'POST'])
def root():

    if request.method == 'POST':
        try:
            args = parser.parse_args()
            user = User(args['user'], args['pass'])
            if not user.insert_user():
                return jsonify({'status':'NOK', 'message':'User already exists'}), 400
            res = {'status':'OK', 'user':args['user'], 'password': args['pass']}

            return jsonify(res), 201

        except Exception as e:
            logger.info(e)
            print(e)
            abort(400)

        return "OK"

    if request.method == 'GET':
        try:
            args = parser.parse_args()
            user = User.query.filter_by(username=args['user']).one()
            res = {'status':'OK', 'user':user.username}
            return jsonify(res), 200
        except Exception as e:
            logger.info(e)
            print(e)
            return jsonify({'status':'NOK'}), 400


@main.route("/login", methods=["GET", "POST"])
def login():
    try:
        args = parser.parse_args()
        user = User.query.filter_by(username=args['user']).one()

        if not user:
            return jsonify({'status':'NOK', 'message':'Invalid user'}), 400

        if not (user.check_password(args['pass'])):
            return jsonify({'status':'NOK', 'message':'Wrong password'}), 400


        return jsonify({'status':'OK', 'message':'Logged in'}), 200
    except Exception as e:
        print(e)
        return jsonify({'status':'OK', 'message':str(e)}), 400