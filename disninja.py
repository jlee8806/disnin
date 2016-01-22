from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "asdf"

myninjas = {'purple':"../static/imgs/donatello.jpg",'blue':'../static/imgs/leonardo.jpg','red':'../static/imgs/raphael.jpg','orange':'../static/imgs/michelangelo.jpg'}

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/ninja/')
def show():
	pizza=[]
	for i,h in myninjas.iteritems():
		pizza.append(h)

    	return render_template("all.html", pizza = pizza)

@app.route('/ninja/<ninja_type>')
def show_user_profile(ninja_type):
	
	pizza = []

	pizza.append(myninjas[ninja_type])

    	return render_template("all.html",  pizza = pizza )

@app.errorhandler(404)
def page_not_found(error):

	return render_template('ao.html')


app.run(debug=True)