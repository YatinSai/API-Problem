import csv
from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
with open('FinalData.csv', newline="") as f:
  reader = csv.reader(f)
  planets_data = list(reader)

with open('goldeylocks.csv', newline="") as i:
  reader1 = csv.reader(i)
  gold_data = list(reader1)
 
@app.route("/finaldata") 
def index():
    return jsonify({
        "data": planets_data,
        "message": "success"
    }), 200
 
@app.route("/goldplanets")
def gold():
    return jsonify({
        "data": gold_data,
        "message": "success"
    }), 200
 
if __name__ == "__main__":
    app.run()

    
