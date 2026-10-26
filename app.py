"""Run LingoWorld on your own computer:  python app.py  then open http://127.0.0.1:5000"""
from pathlib import Path

from flask import Flask, send_file

app = Flask(__name__)
PAGE = Path(__file__).parent / "index.html"


@app.route("/")
def home():
    return send_file(PAGE)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
