from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Accra, Ghana",
    "salary": "GH₵ 10,000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Kumasi, Ghana",
    "salary": "GH₵ 15,000"
  },
  {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Remote",
    "salary": "GH₵ 12,000"
  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Francisco, USA",
    "salary": "GH₵ 17,000"
  }
]

@app.route("/")
def hello_world():
  return render_template("home1.html", jobs = JOBS, company_name = "CKODON")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)

