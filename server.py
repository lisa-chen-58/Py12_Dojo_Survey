from flask import Flask, render_template, session, redirect,request
app = Flask(__name__)

app.secret_key="hi hi hello"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def user():
    print(request.form)
    
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    
    name=session['name']
    location=session['location']
    language=session['language']
    comment=session['comment']
    
    return redirect("/result")

@app.route('/result')
def result():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)