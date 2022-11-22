from flask import Flask
from flask import render_template

app = Flask(__name__)

from app.asm2204.st08 import bp as bp0408


bps = [
    ["[2204-08] Довиденков 2204", bp0408],
]

for i, (title, bp) in enumerate(sorted(bps), start=1):
    app.register_blueprint(bp, url_prefix=f"/st{i}")


@app.route("/")
def index():
    return render_template("index.tpl", bps=sorted(bps))
