import os
from flask import Flask
from flask import request
from processing import function

app = Flask(__name__)
@app.route("/<variable>", methods=['GET'])
def index(variable):
    if request.method == 'GET':
        
        return function(variable)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))        