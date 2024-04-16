from flask import Flask, request, redirect, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = request.form['guess']
        message = ''
        if int(guess) < int(session['low']) or int(guess) > int(session['high']):
            message = 'Please choose a number between ' + str(session['low']) + ' and ' + str(session['high'])
        if int(guess) > session['magic_number'] :
            message = 'Your guess is above the magic number'
            session['high'] = guess
        elif int(guess) < session['magic_number']:
            message = 'Your guess is below the magic number'
            session['low'] = guess
        elif int(guess) == session['magic_number']:
            message = 'You got it! The magic number is ' + str(session['magic_number']) + '.'
            session['still_guessing'] = False
        if session['still_guessing'] == False:
            return render_template('play_again.html', message = message)
        else:
            return render_template('index.html', message = message)
        
    else:
        low_value = 1
        high_value = 75
        session['still_guessing'] = True
        session['magic_number'] = random.randint(low_value, high_value)
        session['low'] = low_value
        session['high'] = high_value
        message = ''

    return render_template('index.html', message = message)

if __name__ == '__main__':
    app.run()
