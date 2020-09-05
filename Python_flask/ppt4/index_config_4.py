from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config/base_setting.py')
# 定义ops_config set ops_config
# app.config['DEBUG'] = True

@app.route ("/")

def hello ():
    return "hello, I Love Imooc"
if __name__ == "__main__":
    app.run(host='0.0.0.0')