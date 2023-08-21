from flask import Flask,jsonify
from flask_cors import CORS  # Import Flask-CORS
import mysql.connector


app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your app

# try:
#     con = mysql.connector.connect(host="localhost", user="root", password="Swastika@123")
#     print("Connection successful")
#     con.autocommit = True
#     cur = con.cursor()

#     database_name = "hotelbooking_2"
#     cur.execute(f"CREATE DATABASE {database_name}")
#     cur.execute(f"USE {database_name}")

#     cur.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45), email VARCHAR(45), phone VARCHAR(20), password VARCHAR(255))")

# except mysql.connector.Error as err:
#     print("Error:", err)




@app.route("/")
def home():
    data = {
        "message": "This is a Flask server code running",
        "status": "success"
    }
    return jsonify(data)

import controller.user_controller as user_controller


if __name__ == "__main__":
    app.run(debug=True)
