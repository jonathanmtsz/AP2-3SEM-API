from flask import Blueprint
from config import app, db

posts = Blueprint('posts',__name__)
@posts.route('/', methods=['GET'])
def main():
    return 'Posts routes'


class User(db.Model):
    id = db.Column(db.Integer, primary_key =
True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))

def __init__(self, username, password):
    self.username = username
    self.password = password