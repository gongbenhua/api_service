from setting import SERVER_PORT, SERVER_HOST
from flask import Flask,  jsonify, render_template
from utils.MysqlDb import db
from flask_cors import CORS
from dynamic.student_controller import student_controller
from auth import auth
from stud import stud
app = Flask(__name__, static_folder='resources', static_url_path='/resources')
app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY='dev')

app.register_blueprint(student_controller, url_prefix='/backend/student')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(stud, url_prefix='/stud')
# app.config["JSON_AS_ASCII"] = False  # jsonify return normal fonts
CORS(app, supports_credentials=True) #Allow request to be sent cookie

@app.route('/')
def index():
    """Show all the posts, most recent first."""
    posts = db.select_all('SELECT * FROM student')
    return render_template('system/index.html', posts=posts)


@app.route('/a', methods=['GET'])
def hello():
    return jsonify('Hello World!')



if __name__ == '__main__':
    # host:Host IP address，port:Specify the port number for access，debug=True Set debugging mode on
    app.run(
        host=SERVER_HOST,
        port=SERVER_PORT,
        debug=True
    )

