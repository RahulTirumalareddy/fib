from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

def fibonacci(n):
	a,b=0,1
	if n==0:
		return a
	if n==1:
		return b
	while n>1:
		a,b=b,a+b
		n-=1
	return b

d={'fibonacci':fibonacci, 'square':'lambda x:x*x'}#different structure for lambda and def functions


@app.route('/')
def hello_world():
	return render_template('index.html',d=d)
#finish this
@app.route('/add', methods=['POST'])
def add():
	d[request.form['func_name']]=request.form['func_def']
	return hello_world()

@app.route('/answer', methods = ['POST'])
def answer():
	errors=[]
	if not request.form['f'] in d:
		errors.append("'" + request.form['f'] + "'"+ " is not in the dictionary of methods.")
	
	if not request.form['n'].isdigit():
		errors.append("The input must be an integer.")
	
	if not errors and isinstance(d[request.form['f']],str):
		f=d[request.form['f']]
		case = request.form['n']
		return str( eval( '('+f+')'+'('+ case+')' ) )
	elif not errors:
		f=d[request.form['f']]
		case = int(request.form['n'])
		return str(f(case))
	return " | ".join(errors)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 33507))
	app.run(host='0.0.0.0', port=port)
