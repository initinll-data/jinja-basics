import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return flask.render_template("child.html", title="Maria's Server", body='body content', name='Dan')


if __name__ == "__main__":
    app.run(debug=True)
