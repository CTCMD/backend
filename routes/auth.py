from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    if email:
        return jsonify({"status": "ok", "email": email}), 200
    return jsonify({"status": "error"}), 401
