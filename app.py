from flask import Flask
from flask import request
from flask import render_template
import random

n = 0
guess_count = 0
guess_limit = 5

app = Flask(__name__)


@app.route('/')
def home():
    global guess_count

    guess_count = 0

    return render_template("index.html")


@app.route('/', methods=['POST'])
def home_post():
    global guess_count
    global number
    global n

    if guess_count < guess_limit:
        n = request.form['dan']
        n = int(n)
        number = random.randint(1, n)

    return render_template("index2.html", n=n)


@app.route('/new')
def my_form():
    return render_template("index2.html", n=n)


@app.route('/new', methods=['GET', 'POST'])
def my_form_post():
    global guess_count
    global guess_limit

    if guess_count <= guess_limit:
        guess = request.form['inputted']
        guess = int(guess)

        if guess != number:
            if guess < number:
                msg = 'The Number is higher'
                guess_count += 1
                return render_template("index2.html", msg=msg, n=n)

            if guess > number:
                msg = 'The Number is lower'
                guess_count += 1
                return render_template("index2.html", msg=msg, n=n)

        else:
            num = 'You Got it'
            numb = ''
            msg = ''
            return render_template("index2.html", msg=msg, numG=num, numB=numb, n=n)

    else:
        num = 'Out of guesses.The number was ' + str(number)
        numb = ''
        msg = ''
        return render_template("index2.html", msg=msg, numB=num, n=n, numG=numb)


if __name__ == '__main__':
    app.run(debug=True)
