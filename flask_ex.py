
from flask import Flask, render_template, request

app = Flask(__name__)

#saved info
#usually database 
Input = [
	{	'author' : 'Alfred Adams',
		'title'  : 'Text 1',
		'content': 'blah blah blah',
		'date'   : '12/12/2012'
	},
	{	'author' : 'Brent Brian',
		'title'  : 'Text 2',
		'content': 'blah',
		'date'   : '1/21/2017'
	}
]

#root
@app.route("/")
def root():
	return ("welcome to the root page")

@app.route("/loop1")
def loop1():
	return render_template('loop.html', info = Input, title = 'loop example without template inheritance')

@app.route("/loop2")
def loop2():
	return render_template('child_loop_layout.html', info = Input, title = 'loop example with template inheritance')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/input", methods=['GET', 'POST'])
def getInput():
	if request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		
		#debugger prints
		#print(first_name, last_name)
		#print(request.form.get('acceptance'))

		#check if checkmark is checked
		if request.form.get('acceptance') == 'on':
			return ("welcome to the root page " +
				 first_name + 
				 " " + 
				 last_name)
		#else if checkbox is not checked
		elif request.form.get('acceptance') == None:
			return ("welcome anonymous user")

	#debugger prints
	#print(request.method)
	return render_template('child_input.html', title = 'get an input and print to terminal')
	

@app.route("/ui")
def ui():
	return render_template('ui.html')

'''
@app.route("/sematic")
def sematic():
	return render_template('sematic.html')
'''

#if you don't want to to build everytime then set debug to True
#allow you to run without export flash and running it 
#you can run the script directly
if __name__ == '__main__':
	app.run(debug = True)