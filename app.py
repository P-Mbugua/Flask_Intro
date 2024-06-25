from flask import Flask, request, jsonify

app = Flask(__name__)

students = ["Peter", "Mary", "Jean"]

@app.route("/students", methods=["GET"])
def fetch_students():
    if len(students) == 0:
        return jsonify({"message": "No student found"}), 404
    return jsonify(students), 200 

@app.route("/students/<int:id>", methods=["GET"])
def fetch_student(id):
    if id < 0 or id >= len(students):
        return jsonify({"message": "No student found"}), 404
    return jsonify(students[id]), 200 

if __name__ == "__main__":
    app.run(debug=True)
