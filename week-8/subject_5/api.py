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

cnx_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "mypool",
    pool_size = 5,
    **CONFIG
)


def query(cmd, content):
    try:
        cnx = cnx_pool.get_connection()
        cursor = cnx.cursor()
        cursor.execute(cmd, content)
        return cursor.fetchone()
    finally:
        if cnx.is_connected():
            cursor.close()
        if cnx:
            cnx.close()


def update(cmd, content):
    try:
        cnx = cnx_pool.get_connection()
        cursor = cnx.cursor()
        cursor.execute(cmd, content)
        cnx.commit()
    except:
        cnx.rollback()
    finally:
        if cnx.is_connected():
            cursor.close()
        if cnx:
            cnx.close()


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
    query_result = query(query_cmd, query_content)
    
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
        update_cmd = '''
            UPDATE member 
            SET name=%(name)s 
            WHERE username=%(username)s;
        ''' 
        update_content = {
            "name": data["name"],
            "username": session["user_name"],
        }
        update(update_cmd, update_content)

        session["user"] = data["name"]
        res = {"ok": True}
    else:
        res = {"error": True}

    return jsonify(res)
