from flask import Flask, render_template, jsonify

app= Flask(__name__)

JOBS= [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary':'Rs. 16,00,000'
  },

  {
    'id': 2,
    'title': 'Frontend Developer',
    'location': 'San Fransisco, USA',
    'salary': '$ 1,20,000',
  },

  {
    'id': 3,
    'title': 'Backend Developer',
    'location': 'New Delhi, India',
    'salary': 'Rs. 12,00,000',
  },

  {
    'id': 4,
    'title': 'Android Developer',
    'location': 'Remote',
    'salary': 'Rs. 15,00,000'
  }
]

@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, 
                                company_name= 'Jovian' )

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)


if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)
  