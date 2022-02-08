from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
import mysql.connector


bp = Blueprint("bp", __name__)

CONFIG = {
    "user": "root",
    "password": "12345678",
    "host": "localhost",
    "database": "website"
}

cnx = mysql.connector.connect(**CONFIG)
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

    cursor.execute(
        f'''
        SELECT name, username, password
        FROM member 
        WHERE username="{acct}";
        '''
    )
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

    cursor.execute(
        f'''
        SELECT count(username) 
        FROM member 
        WHERE username="{acct}";
        '''
    )
    acct_exist_amount = tuple(cursor)[0][0]
    if acct_exist_amount:
        msg = "帳號已經被註冊"
        session["user_status"] = "未登入"
        return redirect(f"/error/?message={msg}")

    cursor.execute(
        f'''
        INSERT INTO member (name, username, password) 
                    values ("{user}", "{acct}", "{pswd}");
        '''
    )
    cnx.commit()
    return redirect('/')


@bp.route("/signout", methods=["GET"])
def sign_out():
    session["user_status"] = "未登入"
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