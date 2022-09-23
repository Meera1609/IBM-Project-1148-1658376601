from flask import Flask,render_template,redirect,url_for,request,flash

app = Flask(__name__)
@app.route("/validate", methods=['POST'])
def validate():
    email=request.form['email']
    pwd=request.form['pwd']
    if not email:
        error="email required!"
    elif not pwd:
        error="password required"
    else:
        return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route("/")
def hello():
    return 'Hello, World!'

@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signup",methods=['GET','POST'])
def signup():
    if(request.method=='POST'):
        email=request.form['email']
        pwd=request.form['pwd']
        cpwd=request.form['cpwd']
        if not email:
            error="email required!"
        elif not pwd:
            error="password required"
        elif not cpwd:
            error="confirm password required"   
        else:
            if(pwd==cpwd):
                return redirect(url_for('home'))
            else:
                error="password dont match"
        return render_template('signup.html',error=error)
    else:  
        return render_template('signup.html')

@app.route("/login",methods=['GET'])
def login():
    return render_template('login.html')

