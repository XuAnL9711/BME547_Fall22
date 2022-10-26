# server.py
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"

@app.route("/", methods=["GET"])
def information():
    x = "This is website will calculate blood cholesterol levels.\n"
    x += "It is written by Xuan Liu."
    return x

@app.route('/hdl_check', methods=['POST'])
def hdl_check_from_internet():
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    answer = check_HDL(hdl_value)
    return answer

@app.route("add_numbers", methods=["POST"])
def add_numbers():
    in_data = requests.get_json()
    answer = in_data["a"] + in_data["b"]
    return jsonify[answer]

@app.route("/add/<a>/<b>", methods=["GET"])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)

if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run()