from config import app, db
from index import posts
from sorvete.sorvete_routes import sorvetes_blueprint
from categorias.categorias_routes import categorias_blueprint

app.register_blueprint(posts)
app.register_blueprint(sorvetes_blueprint)
app.register_blueprint(categorias_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port = app.config['PORT'], debug=app.config['DEBUG'])