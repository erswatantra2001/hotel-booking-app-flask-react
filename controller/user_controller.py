from app import app
from model.user_model import user_model
from flask import request,send_file,jsonify
from datetime import datetime

obj=user_model()

@app.route("/singup",methods=["POST"])
def post_controller():
    val=request.get_json()
    return obj.user_post_model(val)



