from flask import Flask, jsonify, request
from main import DAO, RequestHelper

myApp = Flask(__name__)


@myApp.route('/')
def index():
    return 'What do you want?'


@myApp.route('/data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    return jsonify({'response': DAO.read_data(data_id)})


@myApp.route('/data', methods=['POST'])
def put_data():
    DAO.write_data(RequestHelper.parse_request(request))
    return jsonify({'response': True})


if __name__ == '__main__':
    myApp.run(debug=True)
