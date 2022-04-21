from flask import Flask
from flask import session
from flask import request
from flask import render_template
import random
from flask_session import Session

app = Flask(__name__)
app.config['secret_key'] = 'Secret_Key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = "my_session"

# Create and initialize the Flask-Session object AFTER `app` has been configured
server_session = Session(app)


def save_session(n_save, guess_count_save, guess_limit_save, number_save, tries_save, score_save, button_show_save):
    session['n'] = n_save
    session['guess_count'] = guess_count_save
    session['guess_limit'] = guess_limit_save
    session['number'] = number_save
    session['tries'] = tries_save
    session['score'] = score_save
    session['button_show'] = button_show_save


def score_increase():
    score = session.get('score')

    score += 1
    session['score'] = score
    return score


@app.route('/')
def home():
    session['n'] = 0
    session['guess_count'] = 0
    session['guess_limit'] = 5
    session['tries'] = 5
    session['score'] = 0
    session['button_show'] = 0

    return render_template("index.html")


@app.route('/continue')
def restart():
    session['n'] = 0
    session['guess_count'] = 0
    session['guess_limit'] = 5
    session['tries'] = 5
    session['button_show'] = 0

    return render_template("index.html")


@app.route('/', methods=['POST'])
def home_post():
    guess_count_post = session.get('guess_count')
    guess_limit_post = session.get('guess_limit')
    tries = session.get('tries')
    score = session.get('score')

    if guess_count_post < guess_limit_post:
        n = request.form['dan']

        if n == '':
            print('Nothing here')
            msg = 'Add a Value to Continue'
            return render_template("index.html", msg=msg)

        else:
            print('Something here')
            n = int(n)
            number = random.randint(1, n)
            session['number'] = number
            session['n'] = n
            button_show = 0
            return render_template("index2.html", n=n, tries=tries, score=score, button_show=button_show)


@app.route('/new')
def my_form():
    n = session.get('n')
    tries = session.get('tries')
    score = session.get('score')
    button_show = session.get('button_show')

    return render_template("index2.html", n=n, tries=tries, score=score, button_show=button_show)


@app.route('/new', methods=['GET', 'POST'])
def my_form_post():
    guess_count = session.get('guess_count')
    guess_limit = session.get('guess_limit')
    number = session.get('number')
    n = session.get('n')
    tries = session.get('tries')
    score = session.get('score')

    if guess_count <= guess_limit:
        guess = request.form['inputted']

        if guess == '':
            print('Nothing here')
            msg = 'Guess a Value'
            button_show = 0
            save_session(n, guess_count, guess_limit, number, tries, score, button_show)
            return render_template("index2.html", msg=msg, n=n, tries=tries, score=score, button_show=button_show)

        else:
            print('Something here')
            guess = int(guess)

            if guess != number:
                if guess < number:
                    msg = 'The Number is higher'
                    guess_count += 1
                    tries -= 1
                    button_show = 0
                    save_session(n, guess_count, guess_limit, number, tries, score, button_show)
                    return render_template("index2.html", msg=msg, n=n, tries=tries, score=score,
                                           button_show=button_show)

                if guess > number:
                    msg = 'The Number is lower'
                    guess_count += 1
                    tries -= 1
                    button_show = 0
                    save_session(n, guess_count, guess_limit, number, tries, score, button_show)
                    return render_template("index2.html", msg=msg, n=n, tries=tries, score=score, button_show=button_show)

            else:
                num = 'You Got it'
                numb = ''
                msg = ''
                button_show = 1
                score = score_increase()
                save_session(n, guess_count, guess_limit, number, tries, score, button_show)
                return render_template("index2.html", msg=msg, numG=num, numB=numb, n=n, tries=tries, score=score,
                                       button_show=button_show)

    else:
        numb = 'Out of guesses.The number was ' + str(number)
        numg = ''
        msg = ''
        button_show = 2
        save_session(n, guess_count, guess_limit, number, tries, score, button_show)
        return render_template("index2.html", msg=msg, numB=numb, n=n, numG=numg, tries=tries, score=score,
                               button_show=button_show)


if __name__ == '__main__':
    app.run(debug=True)
