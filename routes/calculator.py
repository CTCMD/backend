from flask import Blueprint, request, jsonify

calculator_bp = Blueprint("calculator", __name__, url_prefix="/calculator")

@calculator_bp.route("", methods=["POST"])
def calcular():
    data = request.json
    ingresos = float(data.get("ingresos",0))
    gastos = float(data.get("gastos",0))
    beneficio = ingresos - gastos
    irpf = beneficio * 0.15
    iva = beneficio * 0.21
    return jsonify({"beneficio": round(beneficio,2), "irpf": round(irpf,2), "iva": round(iva,2)})
