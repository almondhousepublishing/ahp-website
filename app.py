from flask import Flask
from src.routes import site

app = Flask(__name__)
app.register_blueprint(site)

if __name__ == "__main__":
    app.run(debug=False)