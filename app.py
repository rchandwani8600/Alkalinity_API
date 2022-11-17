from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def home():
    return "HOME"

@app.route("/result/<float:volH>/<float:volS>/<float:N>", methods=['GET'])
@cross_origin(supports_credentials=True)

def similar_to(volH,volS,N):
    res = (volH*N*50*1000)/(volS)
    res =  jsonify(res)
    res.headers.add("Access-Control-Allow-Origin","*")
    print(res)
    return res


if  __name__ == "__main__":
    app.run(debug = True)