from flask import jsonify,Flask
import requests
app=Flask(__name__)
@app.route('/authors')
def index():
    r =requests.get("https://jsonplaceholder.typicode.com/users")
    return jsonify(r.json())
@app.route('/post')
def post():
    s =requests.get("https://jsonplaceholder.typicode.com/posts")
    return jsonify(s.json())

if __name__== "__main__":
    app.run()
