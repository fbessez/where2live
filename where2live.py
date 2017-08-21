from flask import Flask, redirect, url_for, request, render_template, session
import costCalculator
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('homepage.html')

@app.route('/result/<amount>/<job>/<location>')
def result(job, location, amount):
	amount = int(amount)
	# fakeResults = {
	# 	"job": "Software Engineer",
	# 	"city": "San Francisco",
	# 	"state": "California",
	# 	"avgSalaryTeleport": "$50,000",
	# 	"avgSalaryIndeed": "$60,000",
	# 	"incomeAfterTaxes": "$43,000",
	# 	"annualCostTeleport": "$18,000",
	# 	"annualCostNomadlist": "$23,000",
	# 	"savings": "$23,000"
	# }
	#
	# fakeResults2 = {
	# 	"job": "Software Engineer",
	# 	"city": "New York",
	# 	"state": "New York",
	# 	"avgSalaryTeleport": "$85,000",
	# 	"avgSalaryIndeed": "$58,000",
	# 	"incomeAfterTaxes": "$53,000",
	# 	"annualCostTeleport": "$33,000",
	# 	"annualCostNomadlist": "$21,000",
	# 	"savings": "$23,152"
	# }

	if amount == 2:
		results2 = costCalculator.calculateCost(location, job)
		results = session.get('results', None)
		return render_template('result.html', results=fakeResults, results2=fakeResults2)
	elif amount == 1:
		results = costCalculator.calculateCost(location, job)
		session['results'] = results
		return render_template('result.html', results=fakeResults)
	else:
		return render_template('result.html')

@app.route('/search', methods = ['POST'])
def search():
	if request.method == 'POST':
		job = request.form.get('job')
		location = request.form.get('location')
		return redirect(url_for('result', job = job, location = location, amount = 1))
	return redirect('/')

@app.route('/searches', methods=['POST'])
def searches():
	if request.method == 'POST':
		job = request.form.get('job')
		location = request.form.get('location')
		return redirect(url_for('result', job=job, location = location, amount = 2)) # results=results
	return redirect('/')
app.secret_key = 'fab_-=z0j$cw@^@zw5*(uv%hh!1a29uxiq%#ws#ws_7=4znu(c%cewhere2live'

if __name__ == '__main__':
	app.run(debug=True)
