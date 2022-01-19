from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session


app = Flask(
    __name__, 
    static_folder="files", 
    static_url_path='/'
)

app.secret_key = "wehelp_week-4"
user_acct_pswd = {"test": "test"}


@app.route('/')
def index():
    return render_template("login.html")


@app.route("/signin", methods=["POST"])
def sign_in():
    acct = request.form["acct"]
    pswd = request.form["pswd"]

    if not acct or not pswd:
        msg = "請輸入帳號、密碼"
        session["user_status"] = "未登入"
        return redirect(f"/error/?message={msg}")
    elif acct not in user_acct_pswd or pswd != user_acct_pswd[acct]:
        msg = "帳號、或密碼輸入錯誤"
        session["user_status"] = "未登入"
        return redirect(f"/error/?message={msg}")
    
    session["user_status"] = "已登入"
    return redirect("/member/")


@app.route("/member/")
def member():
    user_status = session["user_status"]
    if user_status == "未登入":
        return redirect('/')
    return render_template("member.html")


@app.route("/error/")
def error():
    msg = request.args.get("message", "帳號或密碼輸入錯誤")
    return render_template(
        "error.html",
        error_msg=msg
    )


@app.route("/signout", methods=["GET"])
def sign_out():
    session["user_status"] = "未登入"
    return redirect('/')


app.run(port=3000)