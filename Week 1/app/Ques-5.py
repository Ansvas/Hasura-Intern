from flask import jsonify,Flask,make_response,request,abort
app=Flask(__name__)

@app.route('/robots.txt')
def deny():
    return abort(404)
if __name__== "__main__":
    app.run()
