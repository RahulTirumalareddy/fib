from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)
author='Rahul'
message='Enter n for fibonacci(n)'
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

@app.route('/')
def hello_world():
	return render_template('index.html',author=author,message=message)

@app.route('/answer', methods = ['POST'])
def answer():
	case = int(request.form['n'])
	if case.isdigit():
		return str(fibonacci(case))
	else:
		return render_template('index.html', author=author,message='Enter a valid integer please')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 33507))
	app.run(host='0.0.0.0', port=port)
