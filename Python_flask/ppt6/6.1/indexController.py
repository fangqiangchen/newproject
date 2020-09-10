from flask import Flask,Blueprint,request,make_response
app = Flask( __name__ )

index_page = Blueprint( "index_page",__name__ )

@index_page.route( "/" )
def index_page_index():
    return "index page"

@index_page.route( "/me" )
def hello():
    return "hello i love imooc"

@index_page.route("/get")
def get():
    var_a = request.args.get('a',"i love imooc")
    #变种
    req = request.values
    var_a = req['a'] if "a" in req else "i love imooc"

    return "request:%s,params:%s,var_a%s"%( request.method,request.args )

@index_page.route("/post",methods = [ "POST"])

def post():
    #三元表达式
    # var_a = request.form['a'] if "a" in request.form else ''
    #普通容易看懂的
    # var_a = ""
    # if "a" in request.form:
    #     var_a = request.form['a']
    req = request.values
    var_a = req['a'] if "a" in req else "i love imooc"
    return "request:%s,params:%s,var_a:%s"%( request.method,request.form,var_a )

@index_page.route("/upload",methods = [" POST "])
def upload():
    f = request.files['file'] if "file" in request.files else None
    return "request:%s,params:%s,file:%s"%(request.method,request.files,f)

@index_page.route("/text")
def text():
    return " text/html"
@index_page.route("/text_same")
def text_same():
    response = make_response( 'text/html',200)
    return response

@index_page.route("/json")
def json():
    import json
    data = {"a":"b"}
    response = make_response(json.dumps( data))
    response.headers["Content-Type"] = "application/json"
    return response