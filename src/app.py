from flask import Flask, jsonify
from random_geometry_points.circle2d import Circle2D

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/circle")
def my_test():
    circle = Circle2D(1, 2, 3)
    points = circle.create_random_points(5)
    return jsonify(points)

if __name__ == "__main__":
    app.run(debug=True)
