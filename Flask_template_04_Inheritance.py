from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Flask_template_04_Inheritance_02.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('Flask_template_04_Inheritance_03.html',name=name)

if __name__=='__main__':
    app.run(debug=True)
