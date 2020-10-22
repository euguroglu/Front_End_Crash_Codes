from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True
    mylist = [1,2,3,4,5]
    puppies = ['Red','Blue','Orange']
    return render_template('Flask_template_03_Control_flow.html',mylist=mylist,puppies=puppies,
                            user_logged_in=user_logged_in)


if __name__ =='__main__':
    app.run(debug=True)
