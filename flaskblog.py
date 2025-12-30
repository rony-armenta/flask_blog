from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Rony Armenta',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jun 11 2025'
    },

    {
        'author': 'Tony Montana',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Dec 04 2025'
    },
    {
        'author': 'Katia Arrayales',
        'title': 'Blog Post 3',
        'content': 'Second post content',
        'date_posted': 'Dec 05 2025'
    }

]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
def about():
    # return "<h1>About Page, welcome everybody</h1>"
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# To run this Flask application, you can use the following commands in your terminal:


# git push --set-upstream flask_blog dev
# git checkout -b dev
