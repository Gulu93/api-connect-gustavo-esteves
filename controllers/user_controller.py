from flask import request, jsonify
from data import users as user_data


def create_user():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Os dados do usuário são obrigatórios"
        }), 400

    if not data.get("nome"):
        return jsonify({
            "error": "O campo nome é obrigatório"
        }), 400

    if not data.get("email"):
        return jsonify({
            "error": "O campo email é obrigatório"
        }), 400

    user = {
        "id": user_data.next_id,
        "nome": data.get("nome"),
        "email": data.get("email")
    }

    user_data.users.append(user)
    user_data.next_id += 1

    return jsonify({
        "data": user
    }), 201


def get_users():
    return jsonify(user_data.users), 200


def get_user_by_id(user_id):
    for user in user_data.users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({"error": "Usuário não encontrado"}), 404

def update_user(user_id):
    data = request.get_json()

    for user in user_data.users:
        if user["id"] == user_id:
            user["nome"] = data.get("nome", user["nome"])
            user["email"] = data.get("email", user["email"])

            return jsonify(user), 200

    return jsonify({"error": "Usuário não encontrado"}), 404

def delete_user(user_id):
    for index, user in enumerate(user_data.users):
        if user["id"] == user_id:
            user_data.users.pop(index)
            return "", 204

    return jsonify({"error": "Usuário não encontrado"}), 404