from flask import jsonify,Flask,make_response,request
app=Flask(__name__)

@app.route('/set_cookie')
def setcookie():
    response=make_response('Setting cookie!')  
    response.set_cookie('name',value='Anshul')
    response.set_cookie('age',value='19')
    return response
@app.route('/getcookies')
def getcookie():
    name=request.cookies.get('name')
    age=request.cookies.get('age')
    return 'The value of first cookie is '+ name +' The value of second cookie is '+age

if __name__== "__main__":
    app.run()
