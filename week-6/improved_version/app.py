from routes import bp, cursor, cnx
from flask import Flask
from time import time


app = Flask(
    __name__, 
    static_folder="files", 
    static_url_path='/'
)

app.secret_key = str(time())
app.register_blueprint(bp)

app.run(port=3000)

cursor.close()
cnx.close()
print("======== Sever Terminated ========")
