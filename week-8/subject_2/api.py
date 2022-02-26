from decouple import config
from flask import Blueprint, jsonify
from flask import request
from flask import session
import mysql.connector


bp = Blueprint("api_bp", __name__)

CONFIG = {
    "user": config("USER"),
    "password": config("PASSWORD"),
    "host": config("HOST"),
    "database": config("DATABASE")
}

cnx = mysql.connector.connect(
    pool_name = "mypool",
    pool_size = 5,
    **CONFIG
)
cursor = cnx.cursor()


@bp.route("/api/members", methods=["GET"])
def get_members():
    username = request.args.get("username", None)
    
    query_cmd = '''
        SELECT id, name, username
        FROM member 
        WHERE username=%(username)s;
    ''' 
    query_content = {
        "username": username
    }
    cursor.execute(query_cmd, query_content)
    query_result = cursor.fetchone()
    
    data = {"data": None}
    if query_result:
        query_id, query_name, query_username = query_result
        data["data"] = {
            "id": query_id, 
            "name": query_name, 
            "username": query_username
        }
    
    return jsonify(data)


@bp.route("/api/member", methods=["POST"])
def set_name():
    data = request.json
    user_status = session.get("user_status", "未登入")

    if user_status == "已登入":
        try:
            update_cmd = '''
                UPDATE member 
                SET name=%(name)s 
                WHERE username=%(username)s;
            ''' 
            update_content = {
                "name": data["name"],
                "username": session["user_name"],
            }
            cursor.execute(update_cmd, update_content)
            cnx.commit()
        except:
            cnx.rollback()

        session["user"] = data["name"]
        res = {"ok": True}
    else:
        res = {"error": True}

    return jsonify(res)
