from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_07.html')
    # This home page should have the form.



# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.
    name = request.args.get('username')

    # HINTS:
    lower_letter = False
    upper_letter = False
    num_end = False

    lower_letter = any(i.islower() for i in name)
    upper_letter = any(i.isupper() for i in name)
    num_end = name[-1].isdigit()

    report = lower_letter and upper_letter and num_end



    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    return render_template('report_07.html',report=report,lower=lower_letter,upper=upper_letter,num_end=num_end)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
