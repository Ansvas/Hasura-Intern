from flask import jsonify,Flask,make_response,request,render_template
app=Flask(__name__)

@app.route('/html')
def showhtml():
    return render_template("profile.html")


if __name__== "__main__":
    app.run()
