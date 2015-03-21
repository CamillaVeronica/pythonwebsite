from flask import Flask
from flask import render_template
from flask import request
import mandrill

app = Flask(__name__)

@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/companies/signup")
def company_sign_up_page():
	return render_template('companysignup.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/complete",methods=['POST'])
def company_sign_up():
	form_data = request.form
	mandrill_client = mandrill.Mandrill('9FdJjzfupPJojkDcNiv4jA')
 	mandrill_client.messages.send(
    message={
        'html': '<p>Hello from Mandrill!</p>',
        'from_email': 'laura-gemmell@hotmail.com',
        'to': [{'email': form_data['email'], 'name': form_data['name'], 'type': 'to'}]
    }
)
	return "All OK"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000,debug=True)