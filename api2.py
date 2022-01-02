from flask import Flask, jsonify, request
import csv

with open('FinalData.csv', newline="") as f:
  reader = csv.reader(f)
  planets_data = list(reader)

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": planets_data,
        "message": "success"
    }), 200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in planets_data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()