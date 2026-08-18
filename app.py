from flask import Flask, request, g
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)

# Middleware para interpretar requisições JSON
@app.before_request
def parse_json():
    if request.is_json:
        g.json_data = request.get_json(silent=True)
    else:
        g.json_data = None

@app.route('/')
def home():
    return {"message": "API Connect funcionando!"}

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
