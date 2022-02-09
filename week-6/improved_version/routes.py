from decouple import config
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
import mysql.connector


bp = Blueprint("bp", __name__)

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


@bp.route('/')
def index():
    return render_template("login.html")


@bp.route("/signin", methods=["POST"])
def sign_in():
    acct = request.form["acct"]
    pswd = request.form["pswd"]

    if not acct or not pswd:
        msg = "請輸入帳號、密碼"
        session["user_status"] = "未登入"
        return redirect(f"/error/?message={msg}")

    query_cmd = '''
        SELECT name, username, password
        FROM member 
        WHERE username=%(username)s;
    ''' 
    query_content = {
        "username": acct
    }
    cursor.execute(query_cmd, query_content)

    query_result = tuple(cursor)
    query_user, query_acct, query_pswd = query_result[0] \
                                         if query_result \
                                         else ('', '', '')
    if acct != query_acct or pswd != query_pswd:
        msg = "帳號、或密碼輸入錯誤"
        session["user_status"] = "未登入"
        return redirect(f"/error/?message={msg}")
    
    session["user_status"] = "已登入"
    session["user"] = query_user
    return redirect("/member/")


@bp.route("/signup", methods=["POST"])
def sign_up():
    user = request.form["user"]
    acct = request.form["acct"]
    pswd = request.form["pswd"]

    query_cmd = '''
        SELECT count(username) 
        FROM member 
        WHERE username=%(username)s;
    ''' 
    query_content = {
        "username": acct
    }
    cursor.execute(query_cmd, query_content)

    acct_exist_amount = tuple(cursor)[0][0]
    if acct_exist_amount:
        msg = "帳號已經被註冊"
        session["user_status"] = "未登入"
        return redirect(f"/error/?message={msg}")

    query_cmd = '''
        INSERT INTO member (name, username, password) 
                    values (%(name)s, %(username)s, %(password)s);
    ''' 
    query_content = {
        "name": user,
        "username": acct,
        "password": pswd
    }
    cursor.execute(query_cmd, query_content)

    cnx.commit()
    return redirect('/')


@bp.route("/signout", methods=["GET"])
def sign_out():
    session["user_status"] = "未登入"
    session["user"] = "使用者"
    return redirect('/')


@bp.route("/member/")
def member():
    user_status = session.get("user_status", "未登入")
    user = session.get("user", "使用者")
    if user_status == "已登入":
        return render_template(
            "member.html",
            name=user
        )
    return redirect('/')


@bp.route("/error/")
def error():
    msg = request.args.get("message", "帳號、或密碼輸入錯誤")
    return render_template(
        "error.html",
        error_msg=msg
    )
