import routes 
import api
from flask import Flask
from time import time


app = Flask(
    __name__, 
    static_folder="files", 
    static_url_path='/'
)

app.secret_key = str(time())
app.register_blueprint(routes.bp)
app.register_blueprint(api.bp)

app.run(port=3000)
print("======== Sever Terminated ========")
