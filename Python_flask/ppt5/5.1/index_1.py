from flask import Flask
#注册app
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello ,I Love Imooc"

@app.route( "/my" )
def my():
    return "my page"



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)