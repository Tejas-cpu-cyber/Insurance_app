from flask import Flask, render_template, redirect, request
import pickle

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/check", methods=["GET", "POST"])
def check():
	#loading model with pickle
	with open("insurance_app.model", "rb") as f:
		model = pickle.load(f)
	age = int(request.form["age"])

	sex = request.form["sex"]
	if sex == "male":
		gen = 1;
	else:
		gen = 0;
	bmi = float(request.form["bmi"])

	child = int(request.form["children"])

	smoker = request.form["smoker"]
	if smoker == "yes":
		smok = 1;
	else:
		smok = 0;

	d = [[age, bmi, child, gen, smok]]
	print(d)
	res = model.predict(d)
	msg = "Your Charges Will be : " + str(res[0])
	return render_template("home.html", msg= msg)

@app.route("/bmi")
def bmi():
	return render_template("bmi.html")
@app.route("/bmi", methods=["GET", "POST"])
def cal():
	h =float(request.form["height"])

	w =float(request.form["weight"])

	bmi= w /(h/100)**2

	msg = " Your Body Mass Index Is : " + str(bmi)
	
	return render_template("bmi.html", msg1= msg)

@app.route("/info")
def info():
	return render_template("info.html")

@app.route("/feedback")
def feed():
	return render_template("feedback.html")


@app.route("/feedback", methods=["GET", "POST"])
def receive():
	firstname =  request.form["firstname"]
	lastname = request.form["lastname"]
	rating = request.form["Rating"]
	feed = request.form["feed"]
	msg2 = " Hurry! " + firstname + " " +  lastname + " Your Feedback has been sent to Project Owner i.e to Tejas More " + " "
	msg3 = "Rating : " + rating + " " + "Feedback :  "+ feed 
	f = open("FEEDBACK.txt", "a")
	f.writelines(["\nNew Feedback is Here : " + "\n" "\nFIRST NAME : " + firstname , "\nLAST NAME : " + lastname, "\nRating : " + rating + " " + "\nFeedback :  "+ feed + " \n " ])
	f.close()

	return render_template("feedback.html", msg2= msg2, msg3=msg3)


'''
	if bmi<18.5:
	
    		ans = print("Underweight")
	elif bmi>=18.5 and bmi<25:
    		ans = print("Normal")
	elif bmi>=25 and bmi<30:
    		ans = print("Overweight")
	else:
    		ans = print("Obesity")
	return render_template("home.html", msg2= ans)
	'''

if __name__=="__main__":
	app.run(debug=True)
