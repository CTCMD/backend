from flask import Blueprint, request

webhook_bp = Blueprint("webhook", __name__, url_prefix="/webhook/hotmart")

@webhook_bp.route("", methods=["POST"])
def hotmart():
    data = request.json
    # Aquí procesar webhook de Hotmart
    return {"status":"ok"}
