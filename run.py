from flask import Flask
from app.routes import bp_analysis

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_analysis)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
