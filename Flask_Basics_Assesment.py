from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin</h1>"

@app.route('/puppy_latin/<name>') # name here is dynamicall changing according to given variable
def puppy(name):
    if name[-1] == 'y':
        name = str(name)[:-1]+'ful'
    else:
        name = str(name)+'y'

    return "<h1>{}<h1/>".format(name)

if __name__ == '__main__':
    app.run()
