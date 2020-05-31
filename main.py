import logging
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import configparser
from todo import ToDo


import mail

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


app = Flask(__name__, template_folder='./templates')


formatter = '%(asctime)s;%(name)s;%(message)s'
logging.basicConfig(format=formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/todo/register', methods=['POST'])
def todo_register():
    logger.debug({
        'action': 'todo_register',
        'request': request.json
    })
    todo = ToDo()
    todo.create_table()
    request_json = request.get_json(force=True)
    title = request_json['title']
    rank = int(request_json['rank'])
    deadline = request_json['deadline']
    if title is None:
        return jsonify({'message': 'invalid title'}), 400
    todo.insert_data(title=title, rank=rank, deadline=deadline)
    return jsonify({'message': 'success'}), 200


@app.route('/todo/get', methods=['GET'])
def todo_get():
    logger.debug({
        'action': 'todo_get',
    })
    todo = ToDo()
    data = todo.select_table()
    logger.debug({
        'action': 'todo_get',
        'data': data
    })
    return jsonify({'data': data}), 200


@app.route('/todo/delete', methods=['POST'])
def delete_todo():
    logger.debug({
        'action': 'todo_delete',
        'request': request
    })
    request_json = request.get_json(force=True)
    id = request_json['id']
    todo = ToDo()
    data = todo.delete_todo(id)
    logger.debug({
        'action': 'todo_delete',
        'data': data
    })
    return jsonify({'data': data}), 200


@app.route('/todo/send-mail')
def todo_send_mail():
    logger.debug({
        'action': 'send-mail',
    })
    todo = ToDo()
    data = todo.select_table()
    config = configparser.ConfigParser()
    config.read('config.ini')
    username = config['EMAIL']['username']
    password = config['EMAIL']['password']
    logger.info({
        'action': 'todo_send_mail',
        'username': username,
        'password': password
    })

    mailer = mail.Mailer(username, password)
    content = data
    mailer.send(recipient_address=username, content=content)
    return jsonify({'data': data}), 200


if __name__ == '__main__':
    app.run(host='localhost', port=8989, threaded=True, debug=True)
