"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

MADLIBS = ['madlib.html', 'madlib2.html', 'madlib3.html']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    list_compliment = sample(AWESOMENESS, 3)

    for x in range(len(list_compliment)):
        if list_compliment[x] == list_compliment[-1]:
            list_compliment[x] = 'and ' + list_compliment[x] + '!'
        else:
            list_compliment[x] = list_compliment[x] + ','

    return render_template("compliment.html",
                           person=player,
                           compliments=list_compliment)


@app.route('/game')
def show_madlib_form():
    """Start the madlib game"""

    answer = request.args.get('answer')
    noun = request.args.get('noun')
    color = request.args.get('color')
    adjective = request.args.get('adjective')
    player = request.args.get("person")

    if answer == 'Yes':
        return render_template("game.html",
                               noun=noun,
                               person=player,
                               color=color,
                               adjective=adjective)
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Show the madlib"""

    noun = request.args.get('noun')
    color = request.args.get('color')
    adjective = request.args.get('adjective')
    player = request.args.get("person")
    madlib = choice(MADLIBS)

    return render_template(madlib,
                            noun=noun,
                            color=color,
                            adjective=adjective,
                            person=player)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
