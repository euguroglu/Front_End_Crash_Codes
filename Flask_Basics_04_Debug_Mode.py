from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>') # name here is dynamicall changing according to given variable
def puppy(name):
    return "<h1>This is a page for {}<h1/>".format(name)

@app.route('/upper/<name>') # name here is dynamicall changing according to given variable
def upper(name):
    return "100th letter: {}".format(name[100])


if __name__ == '__main__':
    app.run(debug=True)
