from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', title='Home Page')


@app.route("/about")
def about():
    # return "<h1>About Page, welcome everybody</h1>"
    return render_template('about.html', title='About Page')


if __name__ == '__main__':
    app.run(debug=True)
# To run this Flask application, you can use the following commands in your terminal:


# git push --set-upstream flask_blog dev
# git checkout -b dev
