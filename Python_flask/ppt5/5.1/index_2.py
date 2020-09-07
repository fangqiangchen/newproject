from flask import Flask
#注册app
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello ,I Love Imooc"

@app.route( "/my/<user_name>")
def my( user_name ):
    return "my page:user %s" %(user_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)