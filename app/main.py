from flask import Flask
from flask import Response
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/100", methods = ['GET'])
def responce100():
    return Response("responce code 100", status=100, mimetype='application/json')

@app.route("/200", methods = ['GET'])
def responce200():
    return Response("responce code 200", status=200, mimetype='application/json')

@app.route("/300", methods = ['GET'])
def responce300():
    return Response("responce code 300", status=300, mimetype='application/json')

@app.route("/400", methods = ['GET'])
def responce400():
    return Response("responce code 400", status=400, mimetype='application/json')

@app.route("/500", methods = ['GET'])
def responce500():
    return Response("responce code 500", status=500, mimetype='application/json')

metrics.start_http_server(9000)
app.run(port = 8080, host = '0.0.0.0', debug=True)
