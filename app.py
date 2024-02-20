from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Austin, Tx',
    'salary': '$ 110,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Dallas, Tx',
    'salary': '$ 150,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'San Francisco, CA',
    'salary': '$ 80,000'
}]


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
