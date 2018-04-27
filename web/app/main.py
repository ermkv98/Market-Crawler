from flask import Flask, render_template, jsonify, request
from db_consts import *
from backend.app_meta.models import db, AppMeta
from backend.crawler import crawl_webpage
import re

app = Flask(__name__, template_folder='static/templates')

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)
with app.app_context():
    db.create_all()


def is_data_exists(id_str, hl):
    meta = AppMeta.query.filter_by(id_str=id_str, hl=hl).first()
    return True if meta else False


def get_hl(app_url):
    return 'ru' if 'hl=ru' in app_url else 'en'


def get_id(app_url):
    # decomposing by splitting url near '?' and '&' signs
    url = re.sub(r'id=', '&', app_url)
    url_list = url.split(r'&')
    id_str = url_list[1]
    return id_str


@app.route('/post', methods=['POST'])
def index_post():
    if request.method == 'POST':
        json_data = request.get_json()
        app_url = json_data['url']
        id_str = get_id(app_url)
        hl = get_hl(app_url)
        if is_data_exists(id_str, hl):
            meta = AppMeta.query.filter_by(id_str=id_str,
                                           hl=hl).first()
        else:
            content, name = crawl_webpage(app_url)
            meta = AppMeta(id_str=id_str,
                           name=name,
                           hl=hl,
                           content=content)
            db.session.add(meta)
            db.session.commit()
        response = jsonify({'name': meta.name,
                            'content': meta.content})
        return response


@app.route('/', methods =['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
