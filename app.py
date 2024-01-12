from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "오늘 하루 화이팅!!"

#0.0.0.0 : 모든 IP를 허용
