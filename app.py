from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data scientist',
    'location': 'Toronto Canada',
    'salary': 'CAD 120,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Kingston Jamaica',
    'salary': 'JDM 190,000'
  },
  {
    'id': 3,
    'title': 'FrontEnd Develoiper',
    'location': 'New York USA',
    'salary': 'USD 110,000'
  },
  {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'London Canada'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, companyName='Zillian')
  
@app.route('/api/jobs')
def jobs_api():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
