"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


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

    compliment = choice(AWESOMENESS)

    answer = request.args.get("answer")

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment,
                           answer=answer)

@app.route('/game')
def  show_madlib_form():
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

    return render_template("madlib.html",
                            noun=noun,
                            color=color,
                            adjective=adjective,
                            person=player)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
