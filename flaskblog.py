from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/about")
def about():
    return "<h1>About Page, welcome everybody</h1>"


if __name__ == '__main__':
    app.run(debug=True)
# To run this Flask application, you can use the following commands in your terminal:


# git push --set-upstream flask_blog dev
# git checkout -b dev
