from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Replace with your desired database URI
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing ID
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.id}>"

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


@app.route("/users", methods=['GET', 'POST'])
def user_operations():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    elif request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('name'):
            return jsonify({'message': 'Missing required field: name'}), 400  # Bad request

        try:
            user = User(name=data['name'])
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'User created successfully'}), 201  # Created
        except IntegrityError:
            return jsonify({'message': 'User with that name already exists'}), 409  # Conflict
        
@app.route("/users/<int:user_id>", methods=["PUT", "DELETE"])
def user_details(user_id):
    if request.method == "PUT":
        user_details = User.query.get(user_id)
        user_details.name = request.json['name']
        db.session.commit()
        return jsonify({"message": "user updated successfully"}), 200

    elif request.method == "DELETE":
        user = User.query.get(user_id)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", user, user.to_dict(), user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":"Deleted successfully"})

if __name__ == '__main__':
    db.create_all()  # Create tables only if they don't exist
    app.run(debug=True)