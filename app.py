from db import db
from flask_migrate import Migrate
from resources.user import User

from models.user import UserModel
from flask import Flask, render_template, request
from settings import *
from flask_restful import Api
from flasgger import Swagger


app = Flask(__name__)
# api_bp = Blueprint('api', __name__)
# api = Api(api_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = P_DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger=Swagger(app)
db.init_app(app)

migrate = Migrate(app, db)



@app.route('/form')
# Your code
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_user = UserModel(name=name, age=age)
        # db.session.add(new_user)
        # db.session.commit()
        new_user.save_to_db()
        return f"Done!!"


# app.register_blueprint(todoitem_blue)


api2 = Api(app)
api2.add_resource(User, '/user', '/user/<string:name>')

if __name__ == '__main__':

    app.run(debug=True)
