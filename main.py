import os
from flask import Flask
from flask import request
from image.processing import function

app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return function()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))        