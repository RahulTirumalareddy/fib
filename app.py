from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
result=''
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

d={'fibonacci':fibonacci, 'square':'lambda x:x*x'}


@app.route('/')
def hello_world():
	return render_template('index.html',d=d,result=result)

@app.route('/add', methods=['POST'])
def add():
	global result
	if len(request.form['func_name'])>0:
		d[request.form['func_name']]=request.form['func_def']
		result='Function '+request.form['func_name']+' has been added.'
	else:
		result='The function name must be at least one character.'	
	return hello_world()

@app.route('/answer', methods = ['POST'])
def answer():
	global result
	errors=[]
	if not request.form['f'] in d:
		errors.append("'" + request.form['f'] + "'"+ " is not in the dictionary of methods.")
	
	if not request.form['n'].isdigit():
		errors.append("The input must be an integer.")
	
	if not errors:
		f=d[request.form['f']]
		n = request.form['n']
		result=request.form['f'] + '(' + n + ') = '
		if isinstance(d[request.form['f']],str):
			exp='('+f+')'+'('+n+')'
			result+=str(eval(exp))
			return hello_world()
		else:
			result+=str(f(int(n)))
			return hello_world()
	result=" | ".join(errors)
	return hello_world()

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 33507))
	app.run(host='0.0.0.0', port=port)
