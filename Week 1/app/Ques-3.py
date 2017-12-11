from flask import jsonify,Flask,make_response,request
app=Flask(__name__)

@app.route('/setcookie')
def setcookie():
    response=make_response('Setting cookie!')  
    response.set_cookie('name',value='Anshul')
    response.set_cookie('age',value='19')
    return response

if __name__== "__main__":
    app.run()
