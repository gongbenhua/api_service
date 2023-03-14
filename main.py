from setting import SERVER_PORT, SERVER_HOST
from flask import Flask,  jsonify

from flask_cors import CORS
from dynamic.student.student_controller import student_controller

app = Flask(__name__, static_folder='resources', static_url_path='/resources')
app.register_blueprint(student_controller, url_prefix='/backend/student')


# app.config["JSON_AS_ASCII"] = False  # jsonify return normal fonts
CORS(app, supports_credentials=True) #Allow request to be sent cookie


@app.route('/a', methods=['GET'])
def ping_pong():
    return jsonify('Hello World!')



if __name__ == '__main__':
    # host:Host IP address，port:Specify the port number for access，debug=True Set debugging mode on
    app.run(
        host=SERVER_HOST,
        port=SERVER_PORT,
        debug=True
    )

