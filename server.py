from flask import Flask, render_template, session, redirect,request
app = Flask(__name__)

app.secret_key="hi hi hello"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    if 'key' not in session:
        session['key'] = 0
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['comment'] = request.form['comment']
        session['location'] = request.form['location']
        session['language'] = request.form.getlist('language')
        print(request.form['language'])
        print("--------------------")

        # session['location'] =session['language'].append(request.form.getlist['language'])
        # print(session['language'])

    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)