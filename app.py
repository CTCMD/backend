from flask import Flask
from flask_cors import CORS
from database.db import db
from routes.auth import auth_bp
from routes.calculator import calculator_bp
from routes.webhook_hotmart import webhook_bp
import config

app = Flask(__name__)
app.config.from_object(config)
CORS(app)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(webhook_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def health():
    return {"status": "Calculadora Autónomos PRO online"}

if __name__ == "__main__":
    app.run(debug=True)
